#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
using namespace std;

typedef long long LL;
#define CLR(a,b) memset(a,b,sizeof(a))
const int N = (200)+5;
int n;
int k;
double p[N];
int use[N];
double dp[N][N];
void solve()
{
    sort(p, p + n);
    double ans = 0;
    for (int small = 0; small <= k; ++small) {
        for (int i = 1; i <= small; ++i) {
            use[i] = i-1;
        }
        for (int i = small + 1; i <= k; ++i) {
            int idx = i - small;
            use[i] = n-idx;
        }
        CLR(dp, 0);
        dp[0][0] = 1;
        for (int j = 1; j <= k; ++j) {
            for (int m = 0; m <= j; ++m) {
                dp[j][m] += dp[j-1][m-1] * p[use[j]] + dp[j-1][m] * (1-p[use[j]]);
            }
        }
        ans = max(ans, dp[k][k/2]);
    }
    printf("%.10f\n", ans);
}
int main()
{
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++cas);
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i) {
            scanf("%lf", &p[i]);
        }
        solve();
        
    }
    return 0;
}