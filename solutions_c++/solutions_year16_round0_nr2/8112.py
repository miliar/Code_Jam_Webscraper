#include <bits/stdc++.h>

const int INF = 0x3f3f3f3f;
int dp[1 << 10];

int main() {
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int cas,ca = 0;
    scanf("%d",&cas);
    while (cas--) {
        char s[10 + 5];
        scanf("%s",s);
        int n = strlen(s);
        int mask = 0;
        for (int i = 0; i < n; ++ i) {
            if (s[i] == '-') {
                mask |= 1 << i;
            }
        }
        memset(dp,INF,sizeof(dp));
        dp[mask] = 0;
        std::queue<int> que;
        que.push(mask);
        while (!que.empty()) {
            int mask = que.front(); que.pop();
            for (int i = 0; i < n; ++ i) {
                int t_mask = mask >> i + 1 << i + 1;
                for (int j = 0; j <= i; ++ j) {
                    if (~mask >> j & 1) {
                        t_mask |= 1 << i - j;
                    }
                }
                if (dp[t_mask] == INF) {
                    dp[t_mask] = dp[mask] + 1;
                    que.push(t_mask);
                }
            }
        }
        printf("Case #%d: %d\n",++ca,dp[0]);
    }
}
