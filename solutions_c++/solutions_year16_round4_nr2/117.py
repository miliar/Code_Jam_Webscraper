#include <cstdio>
#include <algorithm>
using namespace std;

int tc;
int n, k;
double a[202], ca[202];
double dp[202][202];

int main(){
    freopen("Bl.in", "r", stdin);
    freopen("Bl.out", "w", stdout);
    scanf("%d", &tc);
    for(int ttc = 1; ttc <= tc; ttc++){
        scanf("%d%d", &n, &k);
        for(int i = 1; i <= n; i++){
            scanf("%lf", a + i);
        }
        sort(a + 1, a + n + 1);
        double ans = 0;
        for(int q = 0; q <= k; q++){
            int cnt = 1;
            for(int i = 1; i <= q; i++) ca[cnt++] = a[i];
            for(int i = q + n - k + 1; i <= n; i++) ca[cnt++] = a[i];
            dp[0][0] = 1;
            for(int i = 1; i <= k; i++){
                for(int j = 0; j <= k; j++){
                    dp[i][j] = ca[i] * ((j == 0) ? 0 : dp[i - 1][j - 1]) + (1 - ca[i]) * dp[i - 1][j];
                    //printf("%.2f ", dp[i][j]);
                }//puts("");
            }
            ans = max(ans, dp[k][k / 2]);
        }
        printf("Case #%d: %.12f\n", ttc, ans);
    }
}
