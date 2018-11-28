#include <iostream>
#include <cstdio>
using namespace std;
#define N 111
int s[N][N],ans[N][N];
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas = 0;
    int n,m;
    while (T--)
    {
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            {
                scanf("%d",&ans[i][j]);
            }
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            {
                s[i][j] = 101;
            }
        for (int i=0;i<n;i++)
        {
            int ma = -1;
            for (int j=0;j<m;j++) ma = max(ma,ans[i][j]);
            for (int j=0;j<m;j++) s[i][j] = min(s[i][j],ma);
        }
        for (int j=0;j<m;j++)
        {
            int ma = -1;
            for (int i=0;i<n;i++) ma = max(ma,ans[i][j]);
            for (int i=0;i<n;i++) s[i][j] = min(s[i][j],ma);
        }
        bool flag = true;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            {
                if (ans[i][j]!=s[i][j])
                {
                    flag = false;
                    break;
                }
            }
        printf("Case #%d: ",++cas);
        if (flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
