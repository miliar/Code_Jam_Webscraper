#include <bits/stdc++.h>

using namespace std;


string s[10];
int a[10];
int m, n;


int maVal;
int maCnt;

inline bool check() {
    int cnt[n];
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < m; ++i) {
        cnt[a[i]]++;
    }
    for (int i = 0; i < n; ++i) {
        if (!cnt[i]) {
            return false;
        }
    }
    return true;
}

struct S {
    int nxt[26];
    S() {
        memset(nxt, 255, sizeof(nxt));
    }
};


struct Trie {
    vector<S> q;
    Trie() {
        q.assign(1, S());
    }

    void add(const string &str) {
        int v = 0;
        for (int i = 0; i < (int)str.length(); ++i) {
            if (q[v].nxt[str[i] - 'A'] == -1) {
                q[v].nxt[str[i] - 'A'] = q.size();
                q.push_back(S());
            }

            v = q[v].nxt[str[i] - 'A'];
        }
    }

    int size() const {
        return q.size();
    }
};

inline void calc() {
    int ret = 0;

    Trie tr[n];
    for (int i = 0; i < m; ++i) {
        tr[a[i]].add(s[i]);
    }
    for (int i = 0; i < n; ++i) {
        ret += tr[i].size();
    }

    if (ret == maVal) {
        ++maCnt;
    } else {
        if (ret > maVal) {
            maVal = ret;
            maCnt = 1;
        }
    }
}


void rec(int pos = 0) {
    if (pos == m) {
        if (check()) {
            calc();
        }
        return;
    }

    for (int i = 0; i < n; ++i) {
        a[pos] = i;
        rec(pos + 1);
    }
}

inline void solve(int test) {
    cin >> m >> n;
    for (int i = 0; i < m; ++i) {
        cin >> s[i];
    }
    maVal = 0;
    maCnt = 0;

    rec();
    cout << "Case #" << test << ": " << maVal << " " << maCnt << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }

    return 0;
}
