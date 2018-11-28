#include <bits/stdc++.h>

using namespace std;

const int N = 16+5;

double p[N];
double dp[N][N];
int n, K;
int a[N];

double solve() {
    double ans = 0;
    for(int i = 0;i < 1<<n; i++) {
        int sum = 0;
        for(int j = 0;j < n; j++) if(i>>j&1) {
            a[sum++] = j;
        }
        if(sum!=K) continue;
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for(int j = 0;j < sum; j++) {
            for(int k = 0;k <= j; k++) {
                dp[j+1][k] += dp[j][k]*(1-p[a[j]]);
                dp[j+1][k+1] += dp[j][k]*p[a[j]];
            }
        }
        ans = max(ans, dp[K][K/2]);
    }
    return ans;
}

int main() {
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d", &n, &K);
        for(int i = 0;i < n; i++) scanf("%lf", &p[i]);
        printf("Case #%d: %.10f\n", ++cas, solve());
    }
    return 0;
}
