#include <iostream>
#include <vector>
#include <cstdio>
#include <iomanip>
#include <algorithm>

#define inf 1e13
#define maxn 16
#define ll unsigned long long
using namespace std;

double prob[210];

double solve(vector<int> v) {
    vector<vector<double> > dp(v.size() + 1, vector<double>(v.size() + 1));
    dp[0][0] = 1;
    for (int i = 1; i <= v.size(); ++i) {
        int x = v[i-1];
        for (int j = 0; j <= i; ++j) {
            dp[i][j] = 0;
            if (j > 0)
                dp[i][j] += prob[x] * dp[i-1][j-1];
            dp[i][j] += (1 - prob[x]) * dp[i-1][j];
        }
    }

    return dp[v.size()][v.size()/2];
}

void solve() {
    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; ++i) {
        cin >> prob[i];
    }

    sort(prob+1, prob+n+1);

    double ans = 0;

    for (int i = 0; i <= k; ++i) {
        vector<int> v;
        for (int j = 1; j <= i; ++j) {
            v.push_back(j);
        }
        for (int j = n-(k-i)+1; j <= n; ++j) {
            v.push_back(j);
        }

        ans = max(ans, solve(v));
    }

    cout << fixed << setprecision(10) << ans;
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int tests;

    cin >> tests;

    for (int k = 1;k <= tests; ++k) {
        cout << "Case #" << k << ": ";
        solve();
        cout << "\n";
    }
}
