#include <iostream>
#include <queue>
#include <string>
#include <map>

using namespace std;

struct node {
    int level;
    string state;

    node(int l, string s) {
        level = l;
        state = s;
    }
};

map<string, bool> is_visit;
queue<node> node_queue;

string lift(string state, int top_n) {
    int begin = 0, end = top_n;
    while (begin <= end) {
        char tmp = state[begin];
        if(state[end] == '+') {
            state[begin] = '-';
        } else {
            state[begin] = '+';
        }
        if(tmp == '+') {
            state[end] = '-';
        } else {
            state[end] = '+';
        }
        begin++;
        end--;
    }

    return state;
}

bool is_finish(string state) {
    for (int i = 0; i < state.size(); i++) {
        if (state[i] == '-') {
            return false;
        }
    }
    return true;
}

int bfs(string init) {
    node begin(0, init);
    is_visit[begin.state] = true;
    node_queue.push(begin);

    while (!node_queue.empty()) {
        node top_node = node_queue.front();
        node_queue.pop();
        if (is_finish(top_node.state)) {
            return top_node.level;
        }

        for (int i = 0; i < top_node.state.size(); i++) {
            string new_state = lift(top_node.state, i);
            if (is_visit[new_state]) {
                continue;
            }
            is_visit[new_state] = true;
            node next(top_node.level + 1, new_state);
            node_queue.push(next);
        }
    }

    return 0;
}


int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        is_visit.clear();
        while (!node_queue.empty()) {
            node_queue.pop();
        }

        string init;
        cin >> init;

        cout << "Case #" << i << ": " << bfs(init) << endl;
    }
    return 0;
}