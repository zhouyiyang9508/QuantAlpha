from flask import Flask, jsonify

app = Flask(__name__)

# Static data for demonstration purposes
HOT_SEARCHES = [
    "iPhone 14",
    "Tesla Model Y",
    "Flask tutorials",
    "OpenAI GPT-4"
]

@app.route('/api/hot-searches', methods=['GET'])
def get_hot_searches():
    return jsonify(HOT_SEARCHES), 200


if __name__ == '__main__':
    app.run(debug=True)
