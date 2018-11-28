#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }


void print_case(int test_case) { printf("Case #%d: ", test_case); }

char in[1111];
int n;
int can[111], best;
int order[111];
int possible(int pos, int used) {
    if (pos == n) return 1;
    int one = 0;
    for (int i = 0; i < n; ++i) if (order[pos] >> i & 1) if (~used >> i & 1) {
        one = 1;
        if (!possible(pos + 1, used + (1 << i))) return 0;
    }
    if (one == 0) return 0;
    return 1;
}

void solve(int pos, int cost) {
    if (cost >= best) return;
    if (pos == n) {
        for (int i = 0; i < n; ++i) order[i] = can[i];
        sort(order, order + n);
        do {
            if (!possible(0, 0)) return;
        } while (next_permutation(order, order + n));
        chmin(best, cost);
        return;
    }
    int p = can[pos];
    for (int h = 0; h < 1 << n; ++h) {
        int ok = 1, add = 0;
        for (int i = 0; i < n; ++i) {
            if (can[pos] >> i & 1) {
                if (~h >> i & 1) {
                    ok = 0;
                    break;
                }
            } else {
                if (h >> i & 1) {
                    add++;
                }
            }
        }
        if (!ok) continue;
        can[pos] = h;
        solve(pos + 1, cost + add);
        can[pos] = p;
    }
}

void solve_case() {
    int i, j;
    n = getint();
    for (i = 0; i < n; ++i) {
        getstr(in);
        can[i] = 0;
        for (j = 0; j < n; ++j) if (in[j] == '1') {
            can[i] += 1 << j;
        }
    }
    best = n * n;
    solve(0, 0);
    cout << best << endl;

    return;
}

int main () {
    int test_count, test_case = getint();
    for (test_count = 0; test_count < test_case; test_count++) {
        print_case(test_count + 1);
        solve_case();
    }
    return 0;
}
