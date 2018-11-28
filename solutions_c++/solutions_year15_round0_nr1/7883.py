#include<cstdio>

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        int n, ans = 0, cnt = 0;
        scanf("%d", &n);
        for(int i=0; i<=n; i++) {
            int s;
            scanf("%1d", &s);
            if(!s) continue;
            if(i > cnt) {
                ans += i - cnt;
                cnt = i;
            }
            cnt += s;
        }
        printf("Case #%d: %d\n", ca++, ans);
    }
    return 0;
}
