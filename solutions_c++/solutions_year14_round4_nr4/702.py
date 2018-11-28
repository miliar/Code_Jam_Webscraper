#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

struct node {
    node *nxt[30];
    node () {
        memset(nxt, 0, sizeof nxt);
    }
    ~node () {
        for (int i = 0; i < 30; ++i) {
            if (nxt[i])
                delete(nxt[i]);
        }
    }
};

int szz(node *n) {
    int cnt = 1;
    for (int i = 0; i < 30; ++i) {
        if (n->nxt[i])
            cnt += szz(n->nxt[i]);
    }
    return cnt;
}

void shw(node *n, int tab = 4) {
    int i, j;
    for (i = 0; i < tab; ++i)
        cout << " ";
    cout << "node\n";

    for (j = 0; j < 30; ++j) {
        if (n->nxt[j]) {
            for (i = 0; i < tab; ++i)
                cout << " ";
            cout << (char)(j + 'A') << ":\n";
            shw(n->nxt[j], tab + 4);
        }
    }
}

struct trie {
    node *root;
    trie () {
        root = new node();
    }
    void add (string s) {
        node *cur = root;
        for (int i = 0; i < s.size(); ++i) {
            if (!cur->nxt[s[i] - 'A'])
                cur->nxt[s[i] - 'A'] = new node();
            cur = cur->nxt[s[i] - 'A'];
        }
    }
    int sz () {
        return szz(root);
    }
    void show () {
        shw(root, 0);
    }
    void clear () {
        delete root;
    }
};

vector <string> S;
vector <int> G;

int ans, ans_cnt;

void update(int n) {
    /*cout << "gen: ";
    for (int tm = 0; tm < G.size(); ++tm) {
        cout << G[tm] << " ";
    }
    cout << endl;*/
    //cout << "ex\n";
    vector <trie> T(n);
    int cnt = 0, siz, i;
    for (i = 0; i < n; ++i) {
        T[i] = trie();
    }
    for (i = 0; i < S.size(); ++i) {
        T[G[i]].add(S[i]);
    }
    //cout << "show\n";
    //cout << T[0].root << " " << T[1].root << endl;
    //cout << endl;
    for (i = 0; i < n; ++i) {
        siz = T[i].sz();
        //cout << siz << " ";
        if (siz == 1) {
            //cout << endl;
            for (i = 0; i < n; ++i) {
                T[i].clear();
            }
            return;
        }
        cnt += siz;
    }
    if (cnt > ans) {
        ans = cnt;
        ans_cnt = 1;
    }
    else if (cnt == ans) {
        ans_cnt++;
    }
    for (i = 0; i < n; ++i) {
        T[i].clear();
    }
}

void gen(int v, int n) {
    if (v == G.size()) {
        update(n);
        return;
    }
    //cerr << "N: " << n << endl;
    for (int i = 0; i < n; ++i) {
        G[v] = i;
        gen(v + 1, n);
    }
}

void solve_slow() {
    ans = -1;
    ans_cnt = -1;
    int m, n, i;
    cin >> m >> n;
    G.resize(m);
    S.resize(m);
    for (i = 0; i < m; ++i)
        cin >> S[i];
    gen(0, n);
    cout << ans << " " << ans_cnt << endl;
    cerr << "Done.\n";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, T;
    cin >> T;
    for (t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve_slow();
    }
    return 0;
}