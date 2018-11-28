#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAXE 1000
#define MAXN 1000

int E, R, n, v[MAXN];
int dp[MAXN][MAXE];

int solve(int idx, int e) {
    if (idx == n)
        return dp[idx][e] = 0;
    int ret = 0;
    for (int i = 0; i <= e; i++)
        ret = max(ret, solve(idx+1, min(E, e - i + R)) + i * v[idx]);
    return dp[idx][e] = ret;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        memset(dp, -1, sizeof(dp));
        scanf("%d %d %d", &E, &R, &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &v[i]);
        int ans = solve(0, E);
        printf("Case #%d: %d\n", t, ans);
    }
}
