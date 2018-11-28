#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


const int maxn = 222;

int n, K;
//double dp[maxn][maxn][maxn];
double p[maxn * 2];

double dp[222][222];

double check(const vector<double>& p) {
    int n = static_cast<int>(p.size());
    for (int i = 0; i <= n + 1; ++i) {
        for (int j = 0; j <= n + 1; ++j) {
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= i; ++j) {
            if (j > 0) dp[i][j] += dp[i - 1][j - 1] * p[i - 1];
            dp[i][j] += dp[i - 1][j] * (1 - p[i - 1]);
        }
    }
    return dp[n][n / 2];
}

int main() {
    freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        cin >> n >> K;
        for (int i = 1; i <= n; ++i) {
            cin >> p[i];
        }
        sort(p + 1, p + n + 1);
        for (int i = n + 1; i <= 2 * n; ++i) {
            p[i] = p[i - n];
        }
        double ans = 0;
        //
        for (int l = 1; l <= 2 * n - K + 1; ++l) {
            int r = l + K - 1;
            vector<double> vec;
            for (int i = l; i <= r; ++i) {
                vec.push_back(p[i]);
            }
            double val = check(vec);
            ans = max(ans, val);
        }
        //
        /*for (int mask = 0; mask < 1 << n; ++mask) {
            int bit = 0;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i) & 1) {
                    ++bit;
                }
            }
            if (bit != K) continue;
            vector<double> vec;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i) & 1) {
                    vec.push_back(p[i + 1]);
                }
            }
            double val = check(vec);
            ans = max(ans, val);
        }
         */
        
        printf("Case #%d: %.8lf\n", ++ca, ans);
    }
    return 0;
}