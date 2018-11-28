#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>

using namespace std;
typedef long long li;
typedef pair <li, li> pi;
#define rep(i, n) for(int i = 0; i < (int)(n); ++i)

double calc(vector<double> v) {
    const int k = v.size();
    vector<vector<double>> dp(k + 1, vector<double>(k + 1, 0.));
    dp[0][0] = 1.;
    rep(_i, k) {
        int i = _i + 1;
        rep(c, i+1) {
            double calc = 0;
            if (c < i) {
                calc += dp[i - 1][c] * (1. - v[i-1]);
            }
            if (c > 0) {
                calc += dp[i - 1][c - 1] * v[i-1];
            }
            dp[i][c] = calc;
        }
    }
    return dp[k][k / 2];
}
void solve() {
    int n, k;
    cin >> n >> k;
    vector<double> prob(n);
    rep(i, n) {
        cin >> prob[i];
    }
    double ans = 0;
    sort(prob.begin(), prob.end());
    rep(ul, k + 1) {
        int uh = k - ul;
        vector<double> v;
        rep(i, ul) {
            v.push_back(prob[i]);
        }
        int st = n - uh;
        rep(i, uh) {
            v.push_back(prob[st + i]);
        }
        ans = max(ans, calc(v));
    }

    cout.precision(12);
    cout << fixed << ans << endl;
}

int main() {
    int t;
    cin >> t;
    rep(i, t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
