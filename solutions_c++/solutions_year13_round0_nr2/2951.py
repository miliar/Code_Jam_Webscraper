#include <cstdio>
int m, n, a[110][110], mr[110], ml[110];
int main ()
{
    //freopen("a.out","r",stdin);
    //freopen("b.out","w",stdout);
    int cas, t = 0, ans, ok;
    scanf("%d",&cas);
    while(t++<cas)
    {
        ok = 1;
        scanf("%d%d",&m,&n);
        for(int i = 0; i < m; i++)
        {
            ans = 0;
            for(int j = 0; j < n; j++)
            {
                scanf("%d",&a[i][j]);
                int tt = a[i][j];
                ans = tt > ans ? tt : ans;
            }
            mr[i] = ans;
        }
        for(int i = 0; i < n; i++)
        {
            ans = 0;
            for(int j = 0; j < m; j++)
            {
                int tt = a[j][i];
                ans = tt > ans ? tt : ans;
            }
            ml[i] = ans;
        }
        for(int i = 0; i < m; i++) for (int j = 0; j < n; j++)
        if(a[i][j]!=mr[i]&&a[i][j]!=ml[j]) {ok = 0; break; }
        printf("Case #%d: %s\n",t,ok?"YES":"NO");
    }
    return 0;
}
