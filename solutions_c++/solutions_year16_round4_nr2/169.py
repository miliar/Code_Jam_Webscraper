#include <bits/stdc++.h>
using namespace std;



typedef double DB;
typedef long long LL;

const int N = 1e5 + 7;


double dp[205][405];


double calc(double p[], int n) {
    memset(dp, 0, sizeof(dp));
    dp[0][n] = 1.0;
    for (int i = 0; i < n; i++)
    for (int j = 0; j <= n + n; j++) {
        if (j) dp[i + 1][j - 1] += dp[i][j] * (1 - p[i]);
        dp[i + 1][j + 1] += dp[i][j] * p[i];
    }
    return dp[n][n];
}

int n, m;
double p[205], pp[205];

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int CAS;
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%lf", &p[i]);
        sort(p, p + n);
        double ans = 0.0;
        for (int i = 0; i <= m; i++) {
            int k = 0;
            for (int j = 0; j < i; j++)
                pp[k++] = p[j];
            for (int j = n - 1; j >= n - (m - i); j--)
                pp[k++] = p[j];
            ans = max(ans, calc(pp, m));
        }
        printf("Case #%d: %.8f\n", cas, ans);
    }
}
