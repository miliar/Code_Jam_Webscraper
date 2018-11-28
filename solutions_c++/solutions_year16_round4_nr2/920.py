#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
/*
double solve_test(int n, int k, vector <double> & p) {
    int t = k / 2;
    vector < vector < vector < double> > > dp(n + 1, vector < vector < double > > (n + 1, vector < double > (n + 1, 0)));
    for (int i = 0; i <= n; ++i) {
        dp[i][0][0] = 1;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][0] * (1 - p[i - 1]));
            for (int v = 1; v <= j; ++v) {
                double yes = p[i - 1], no = (1 - p[i - 1]);
                dp[i][j][v] = max(dp[i - 1][j][v], max(dp[i - 1][j - 1][v - 1] * yes, dp[i - 1][j - 1][v] * no));
            }
        }
    }
    return dp[n][k][t];
} */

double get_poss(vector <double> &p) {
    int n = p.size();
    vector < double > d(n + 1, 0), t(n + 1, 0);
    d[0] = 1;
    for (int i = 0; i < n; ++i) {
        t[0] = d[0] * (1 - p[i]);
        for (int j = 1; j <= n; ++j) {
            t[j] = d[j] * (1 - p[i]) + d[j - 1] * (p[i]);
        }
        d = t;
    }
    return d[n / 2];
}

void solve() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, k;
        cin >> n >> k;
        vector <double> p(n);
        for (double & x : p) {
            cin >> x;
        }
        double res = 0;
        for (int m = 1; m < (1LL << n); ++m) {
            if (__builtin_popcount(m) == k) {
                vector <double> r;
                for (int v = 0; v < n; ++v) {
                    if (m & (1 << v)) {
                        r.push_back(p[v]);
                    }
                }
                res = max(res, get_poss(r));
            }
        }
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
}

int main() {
#ifdef ALEXEY
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
#endif
    solve();
    return 0;
}