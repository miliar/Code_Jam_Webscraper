#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 210;
double a[N * 2];

double cal(int x, int y) {
    double dp[N], f[N];
    memset(dp, 0, sizeof(dp));
    memset(f, 0, sizeof(f));
    dp[0] = 1;
    for (int i = x; i <= y; i++) {
        for (int j = 0; j <= y - x + 1; j++) f[j] = dp[j];
        for (int j = y - x + 1; j >= 0; j--) {
            dp[j] = (j - 1 >= 0 ? f[j - 1] * a[i] : 0)  + f[j] * (1 - a[i]);
        }
    } 
    return dp[(y - x + 1) / 2];
}

            
int main()
{
    freopen("B-large-.in","r",stdin);
    freopen("B-large-.out","w",stdout);
    int t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++) scanf("%lf", &a[i]);
        sort(a + 1, a + n + 1);
        for (int i = 1; i <= n; i++) a[i + n] = a[i];
        double ans = 0;
        for (int i = 1; i + m - 1 <= n * 2; i++) ans = max(ans, cal(i, i + m - 1));
        printf("Case #%d: %.20lf\n", cas, ans);
    }
    return 0;
}
