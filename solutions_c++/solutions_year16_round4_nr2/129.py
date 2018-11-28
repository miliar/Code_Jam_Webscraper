#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

int n, K;

double p[205];

double pp[205];

double dp[205][405];

int bs = 201;

double solve(int x) {
    int m = 0;
    for(int i = 0; i < x; ++ i) pp[m ++] = p[i];
    for(int i = 0; i < K - x; ++ i) pp[m ++] = p[n - 1 - i];
    memset(dp, 0, sizeof(dp));
    dp[0][bs] = 1;
    for(int i = 0; i < m; ++ i) {
        for(int j = -i; j <= i; ++ j) {
            dp[i + 1][j + bs + 1] += dp[i][j + bs] * pp[i];
            dp[i + 1][j + bs - 1] += dp[i][j + bs] * (1 - pp[i]);
        }
    }
    return dp[m][bs];
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("Bl.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &n, &K);
        for(int i = 0; i < n; ++ i) {
            scanf("%lf", p + i);
        }
        sort(p, p + n);
        double ans = 0;
        for(int i = 0; i <= K; ++ i) {
            ans = max(ans, solve(i));
        }
        printf("Case #%d: %.15f\n", cas, ans);
    }
    return 0;
}
