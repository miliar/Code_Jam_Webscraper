#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <string>
#include <set>
#include <bitset>
#include <map>
#include <ctime>
#include <bitset>
#include <cmath>
#include <cassert>
#include <numeric>
#include <algorithm>
using namespace std;

#define N 100
#define M 13303
#define ll long long
#define ul unsigned long
#define inf 0x7fffffff
#define lson (id<<1)
#define rson (id<<1|1)

#define eps 1e-5
#define type int
#define pii pair<int,int>
#define pdd pair<double,int>
#define MP(i,j) make_pair(i,j)
#define mod 1000000007

int dp[N][N], e, r, n, v[N];

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    clock_t start = clock();
    int cas, pcas = 1;
    scanf("%d", &cas);
    while (cas--) {
        scanf("%d%d%d", &e, &r, &n);
        for (int i = 1; i <= n; i++)
            scanf("%d", &v[i]);
        memset(dp, -1, sizeof(dp));
        dp[0][e] = 0;
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= e; j++) {
                if (dp[i - 1][j] == -1)
                    continue;
                for (int k = 0; k <= j; k++) {
                    int last = min(e, j - k + r);
                    dp[i][last] = max(dp[i][last], dp[i - 1][j] + k * v[i]);
                    ans = max(dp[i][last], ans);
                }
            }
        }
        printf("Case #%d: %d\n", pcas++, ans);
    }
    return 0;
}