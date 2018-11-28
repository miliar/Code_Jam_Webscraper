#include <cstdio>
#include <string>
#include <algorithm>
#include <utility>
using namespace std;

double p[200];
double q[200];
double dp[201][201];

double solve(int n) {
    dp[0][0] = 1.0;
    for(int i = 1; i <= n; i++)
        for(int k = 0; k <= i; k++)
            dp[i][k] = q[i - 1] * dp[i - 1][k - 1] + (1 - q[i - 1]) * dp[i - 1][k];
    return dp[n][n / 2];
}

double solve(int n, int m) {
    copy_n(p, m, q);
    double ans = solve(m);
    for(int i = 0; i < m; i++) {
        q[m - i - 1] = p[n - i - 1];
        ans = max(ans, solve(m));
    }
    return ans;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int n, k;
        scanf("%d %d", &n, &k);
        for(int j = 0; j < n; j++)
            scanf("%lf", p + j);
        sort(p, p + n);
        printf("Case #%d: %.9f\n", i, solve(n, k));
    }
}

