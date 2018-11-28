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
}

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
*/
void solve() {
    int te;
    cin >> te;
    for (int ij = 0; ij < te; ++ij) {
        int n;
        cin >> n;
        vector <string> p(n);
        for (string & x : p) {
            cin >> x;
        }
        int res = n * n + 10;
        for (int m = 0; m < (1 << (4 * n)); ++m) {
            int cost = __builtin_popcount(m);
            vector < vector <int> > tp(n, vector <int> (n, 0));
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (p[i][j] == '1') {
                        tp[i][j] = 1;
                    }
                    if (m & (1 << (4 * i + j))) {
                        tp[i][j] = 1;
                    }
                }
            }
            int cnt = 1;
            vector <int> order(n, 0);
            for (int i = 0; i < n; ++i) {
                order[i] = i;
                cnt = cnt * (i + 1);
            }
            bool can = true;
            for (int pi = 0; pi < cnt && can; ++pi) {
                vector<int> s, t;
                s.push_back(0);
                for (int i = 0; i < n && s.size() > 0 && can; ++i) {
                    int ind = order[i];
                    t.clear();
                    for (int j = 0; j < s.size() && can; ++j) {
                        bool now = false;
                        for (int f = 0; f < n; ++f) {
                            if (tp[ind][f] == 1) {
                                int v1 = (1 << f);
                                if ((v1 & s[j]) == 0) {
                                    t.push_back(s[j] | v1);
                                    now = true;
                                }
                            }
                        }
                        if (!now) {
                            can = false;
                        }
                    }
                    s = t;
                }
                if (s.size() == 0) {
                    can = false;
                }
                next_permutation(order.begin(), order.end());
            }
            if (can) {
                res = min(res, cost);
            }
        }
        cout << "Case #" << ij + 1 << ": " << res << endl;
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