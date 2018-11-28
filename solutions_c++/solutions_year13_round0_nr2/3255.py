#include <stdio.h>
#include <string.h>

int map[105][105];

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int i,j,n,m,cnt=1,k,T;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                scanf("%d",&map[i][j]);
            }
        }
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                for (k=0;k<n;k++)
                {
                    if (map[i][j]<map[k][j]) break;
                }
                if (k==n) continue;
                for (k=0;k<m;k++)
                {
                    if (map[i][j]<map[i][k]) break;
                }
                if (k==m) continue;
                break;
            }
            if (j<m) break;
        }
        printf("Case #%d: ",cnt++);
        if (i<n) printf("NO\n");
        else printf("YES\n");
    }
    return 0;
}
