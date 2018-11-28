#include <cstdio>
#include <cstring>
int kase, n;
bool vis[10];
bool check() {
    for (int i=0; i<10; i++)
        if (!vis[i])
            return false;
    return true;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &kase);
    for (int cas=1; cas<=kase; cas++) {
        memset(vis, false, sizeof(vis));
        scanf("%d", &n);
        if (n==0) {
            printf("Case #%d: INSOMNIA\n", cas);
            continue;
        }
        int t=n;
        while (true) {
            int temp=n;
            vis[temp%10]=true;
            temp/=10;
            while (temp) {
                vis[temp%10]=true;
                temp/=10;
            }
            if (check())
                break;
            n+=t;
        }
        printf("Case #%d: %d\n", cas, n);
    }
    return 0;
}
