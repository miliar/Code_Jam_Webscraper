#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
using namespace std;

const int INF = 0x3f3f3f3f;
int dp[1 << 10];
char s[100];

int solve() {
    memset(dp,INF,sizeof(dp));
    int n = strlen(s);
    int m = 0;
    for (int i = 0; i < n; ++ i) if (s[i] == '-') m |= 1 << i;
    dp[m] = 0;
    queue<int> que;
    que.push(m);
    while (!que.empty()) {
        int m = que.front();
        que.pop();
        for (int i = 0; i < n; ++ i) {
            int tm=m>>i+1<<i+1;
            for (int j = 0; j <= i; ++ j) if (~m >> j & 1) tm|=1<<i-j;
            if (dp[tm] == INF) {
                dp[tm]=dp[m]+1;
                que.push(tm);
            }
        }
    }
    return dp[0];
}

int main() {
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int ca = 1; ca <= cas; ca++) {
        scanf("%s",s);
        printf("Case #%d: %d\n",ca,solve());
    }
    return 0;
}
