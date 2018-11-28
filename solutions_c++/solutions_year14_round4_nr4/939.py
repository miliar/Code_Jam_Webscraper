#include <iostream>
#include <string>
#include <map>

using namespace std;

int T, M, N, X, Y;
string s[100];
bool cc[50];

class Node {
    public:
        map<char, Node *> content;
        bool ch[26];
        Node () {
            memset(ch, false, sizeof(ch));
        }
};

int ans;

int bel[100];

void insert(Node * root, string s) {
    for (int i = 0; i < s.length(); ++i) {
        if (!root->ch[s[i] - 'A']) {
            ans++;
            root->ch[s[i] - 'A'] = true;
            root->content[s[i]] = new Node();
        }
        root = root->content[s[i]];
    }
}

void calc() {
    Node * root[10];
    for (int i = 0; i < N; ++i) {
        root[i] = new Node;
        cc[i] = false;
    }

    ans = 0;
    for (int i = 0; i < M; ++i) {
        if (!cc[bel[i]]) { ans++; }
        cc[bel[i]] = true;
        insert(root[bel[i]], s[i]);
    }
    if (ans > X) {
        X = ans;
        Y = 1;
    } else if (ans == X) {
        Y++;
    }
}

void split(int m) {
    if (m < M) {
        for (int i = 0; i < N; ++i) {
            bel[m] = i;
            split(m + 1);
        }
    } else {
        calc();
    }
}

void solve() {
    split(0);
}

int main(int argc, char *argv[]) {
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        std::cin >> M >> N;
        for (int j = 0; j < M; ++j) {
            std::cin >> s[j];
        }
        X = Y = 0;
        solve();
        std::cout << "Case #" << i + 1<< ": " << X << " " << Y << endl;
    }
    return 0;
}
