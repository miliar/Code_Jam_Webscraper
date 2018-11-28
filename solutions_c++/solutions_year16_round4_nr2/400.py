#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <cstdlib>
using namespace std;
int n, k;
double a[222];
double dp[222][222];
vector<double> g;
int main() {
    int T;
    int cas = 0;
    cin >> T;
    while(T--) {
        cin >> n >> k;
        for(int i = 0; i < n; i++) cin >> a[i];
        sort(a, a + n);
        double ans = 0;
        for(int m = 0; m <= k; m++) {
            g.clear();
            for(int j = 0; j < m; j++) {
                g.push_back(a[j]);
            }
            int ot = k - m;
            for(int j = n - 1; ; j--) {
                if (ot == 0) break;
                g.push_back(a[j]);
                ot--;
            }
            for(int i = 0; i <= k; i++) {
                for(int j = 0; j <= k; j++) dp[i][j] = 0;
            }
            dp[1][1] = g[0];
            dp[1][0] = 1.0 - g[0];
            for(int i = 1; i < k; i++) {
                for(int j = 0; j <= i; j++) {
                    dp[i + 1][j + 1] += dp[i][j] * g[i];
                    dp[i + 1][j] += dp[i][j] * (1.0 - g[i]);
                }
            }
            ans = max(ans, dp[k][k / 2]);        
        }
        printf("Case #%d: %.8f\n", ++cas, ans);
    }

    return 0;
}
