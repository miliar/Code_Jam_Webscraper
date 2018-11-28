#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

int nxt[3][3], n, r, p, s, m;
int opp[3];

void sort_res(vector<int>& res) {
    for (int i = 0; i < n; ++i) {
        int step = 1 << i + 1;
        for (int j = 0; j < m; j += step) {
            int fst = j;
            int snd = j + step / 2;
            vector<int> a1;
            vector<int> a2;
            for (int k = j; k < snd; ++k) a1.push_back(res[k]);
            for (int k = snd; k < j + step; ++k) a2.push_back(res[k]);
            if (a2 < a1) swap(a1, a2);
            for (int k = 0; k < a1.size(); ++k) res[k + fst] = a1[k];
            for (int k = 0; k < a2.size(); ++k) res[k + snd] = a2[k];
        }
    }
}

int solve(int won, vector<int>& res) {
    vector<int> as(1);
    as[0] = won;
    for (int i = 0; i < n; ++i) {
        vector<int> bs;
        for (int j = 0; j < as.size(); ++j) {
            int t = as[j], u = opp[as[j]];
            if (t > u) swap(t, u);
            bs.push_back(t), bs.push_back(u);
        }
        as.swap(bs);
    }
    int rr = 0, pp = 0, ss = 0;
    for (auto c: as) {
        if (c == 0) pp++;
        if (c == 1) rr++;
        if (c == 2) ss++;
    }
    if (pp != p || rr != r || ss != s) return 0;
    res = as;
    sort_res(res);
    return 1;
}

void solve_case() {
    int i, j;
    n = getint(), r = getint(), p = getint(), s = getint(), m = 1 << n;
    vector<int> res, ts;
    if (solve(0, ts)) res = ts;
    if (solve(1, ts)) {
        if (res.empty()) res = ts;
        chmin(res, ts);
    }
    if (solve(2, ts)) {
        if (res.empty()) res = ts;
        chmin(res, ts);
    }
    if (res.empty()) {
        puts("IMPOSSIBLE");
    } else {
        for (auto c: res) {
            if (c == 0) putchar('P');
            if (c == 1) putchar('R');
            if (c == 2) putchar('S');
        }
        puts("");
    }
    return;
}

int main () {
    memset(nxt, ~0, sizeof(nxt));
    opp[0] = 1;
    opp[1] = 2;
    opp[2] = 0;
    // P R S
    nxt[0][1] = nxt[1][0] = 0;
    nxt[1][2] = nxt[2][1] = 1;
    nxt[2][0] = nxt[0][2] = 2;
    int test_count, test_case = getint();
    for (test_count = 0; test_count < test_case; test_count++) {
        print_case(test_count + 1);
        solve_case();
    }
    return 0;
}
