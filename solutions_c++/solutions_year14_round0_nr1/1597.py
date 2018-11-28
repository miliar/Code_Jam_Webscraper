#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#define ll long long
int vis[20];
int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int cas, x, n, ans, t=0;
    scanf("%d", &cas);
    while (cas--) {
        scanf("%d", &n);
        memset(vis, 0, sizeof(vis));
        for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++) {
            scanf("%d", &x);
            if (i==n)
                vis[x]=1;
        }
        ans=0;
        scanf("%d", &n);
        for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++) {
            scanf("%d", &x);
            if (i==n&&vis[x]&&!ans)
                ans=x;
            else if (i==n&&vis[x])
                ans=-1;
        }
        printf("Case #%d: ", ++t);
        if (ans==-1) puts("Bad magician!");
        else if (!ans) puts("Volunteer cheated!");
        else printf("%d\n", ans);
    }
    return 0;
}
