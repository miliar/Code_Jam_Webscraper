#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
double getdouble() { unsigned int c; double x = 0, t = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getdouble(); if (c == '.') break; if (!~c) exit(0); } do { if (c == '.') t = 1; else { x = x * 10 + (c - '0'); if (t > 0) t *= 10; } } while (((c = gc()) - '0') < 10 or c == '.'); if (t > 0) return x / t; return x; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

int n, k;

double ps[333];

double probs[222][222];

double prob(vector<double>& as) {
    for (int i = 0; i <= k; ++i) for (int j = 0; j <= k; j++) probs[i][j] = 0;
    probs[0][0] = 1;
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j <= k; ++j) {
            probs[i + 1][j + 1] += probs[i][j] * as[i];
            probs[i + 1][j] += probs[i][j] * (1 - as[i]);
        }
    }
    return probs[k][k / 2];
}

void solve_case() {
    int i, j;
    n = getint(), k = getint();
    for (i = 0; i < n; ++i) ps[i] = getdouble();

    vector<int> use(n, 0);
    for (i = 0; i < k; ++i) use[i] = 1;
    sort(use.begin(), use.end());

    double res = 0;
    do {
        vector<double> as;
        for (i = 0; i < use.size(); ++i) if (use[i] == 1) {
            as.push_back(ps[i]);
        }
        double p = prob(as);
        chmax(res, p);
    } while (next_permutation(use.begin(), use.end()));

    printf("%.10f\n", res);
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
