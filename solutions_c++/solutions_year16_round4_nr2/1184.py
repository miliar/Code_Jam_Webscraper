#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <functional>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

long double calc(const vector<long double>& a) {
   int n = sz(a);
   vector<vector<long double>> dp(n, vector<long double> (n + 1, 0));
   dp[0][0] = 1.0 - a[0];
   dp[0][1] = a[0];
   for (int i = 1; i < n; ++i) {
       for (int j = 0; j <= n; ++j) {
           dp[i][j] = dp[i - 1][j] * (1.0 - a[i]);
           if (j > 0) {
               dp[i][j] += dp[i - 1][j - 1] * a[i];
           }
       }
   }
   return dp[n - 1][n / 2];
}

void solve() {
    int n, k;
    cin >> n >> k;
    vector<long double> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(all(a));
    long double ans = 0;
    for (int i = 0; i <= k; ++i) {
        vector<long double> b;
        for (int j = 0; j < i; ++j) b.pb(a[j]);
        for (int j = 0; j < k - i; ++j) b.pb(a[n - j - 1]);
        ans = max(ans, calc(b));
    }
    printf("%.12lf\n", (double)ans);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
