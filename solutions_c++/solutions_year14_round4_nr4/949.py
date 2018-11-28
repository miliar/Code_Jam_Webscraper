#include <bits/stdc++.h>

using namespace std;

struct trie {
    bool m;
    trie* p[26];
    int c;

    trie() : m(false), c(0) {
        memset(p, 0, sizeof(p));
    }

};

void ins(trie*& t, const char* str, int& cn) {
    if (!t) {
        t = new trie;
        ++cn;
    }
    if (!*str) {
        t->m = true;
        return;
    }
    int c = *str - 'A';
    if (!t->p[c]) {
        ++t->c;
    }
    ins(t->p[c], str+1, cn);
}

void del(trie*& t, const char* str, int& cn) {
    if (!*str) {
        t->m = false;
    } else {
        int c = *str - 'A';
        del(t->p[c], str+1, cn);
        if (!t->p[c]) --t->c;
    }
    if (t->c == 0 && !t->m) {
        delete t;
        t = 0;
        --cn;
    }
}

pair<int, int> go(vector<string>& strs, int i, int n, vector<trie*> trs, int& tot) {
    if (i == strs.size()) {
        return make_pair(tot, 1);
    }
    pair<int, int> r(0, 0);
    for (int j = 0; j < n; ++j) {
        int f = tot;
//        cerr << "INSERTING " << strs[i] << " ; " << tot << ',';
        ins(trs[j], strs[i].c_str(), tot);
//        cerr << tot << endl;
        pair<int, int> q = go(strs, i+1, n, trs, tot);
        del(trs[j], strs[i].c_str(), tot);
        assert(f == tot);
        if (q.first > r.first) {
            r = q;
        } else if (q.first == r.first) {
            r.second += q.second;
        }
    }
    return r;
}

void t() {
    static int c = 1;
    cout << "Case #" << c++ << ": ";

    int m, n;
    cin >> m >> n;
    vector<string> strs(m);
    for (int i = 0; i < m; ++i) cin >> strs[i];

    vector<trie*> trs(n, (trie*)0);

    int tot = 0;
    pair<int, int> r = go(strs, 0, n, trs, tot);
    cout << r.first << ' ' << r.second << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) t();
}
