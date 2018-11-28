#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
typedef long long ll;
using namespace std;
int tt;
char S[201];
ll dp[201][2];
ll get() {
    int N = strlen(S);
    dp[0][0] = dp[0][1] = 0;
    for(int i = 0; i < N; i++) {
        if(S[i] == '+') {
            dp[i + 1][0] = min(dp[i][1] + 1, dp[i][0]);
            dp[i + 1][1] = min(dp[i][1] + 2, dp[i][0] + 1);
        } else {
            dp[i + 1][0] = min(dp[i][1] + 1, dp[i][0] + 2);
            dp[i + 1][1] = min(dp[i][1], dp[i][0] + 1);
        }
    }
    return min(dp[N][0], dp[N][1] + 1);
}
void solve() {
    scanf("%s", S);
    ll ans = get();
    printf("Case #%d: ", tt);
    printf("%lld\n", ans);
}
int main() {
    int t = 1; scanf("%d", &t);
    for(tt = 1; tt <= t; tt++) solve();
}
