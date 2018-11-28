#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define min(a,b) ((a)<(b)?(a):(b))

int g[105][105],bigest[105][105][2];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int n,m,tc,ti,i,j,k;
    scanf("%d",&tc);
    for(ti=1;ti<=tc;ti++)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",g[i]+j);
                bigest[i][j][0]=bigest[i][j][1]=1;
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                for(k=0;k<n;k++)
                {
                    if(g[k][j]>g[i][j])
                    {
                        bigest[i][j][1]=0;
                    }
                }
                for(k=0;k<m;k++)
                {
                    if(g[i][j]<g[i][k])
                    {
                        bigest[i][j][0]=0;
                    }
                }
            }
        }
        int flag=1;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(bigest[i][j][0]+bigest[i][j][1]==0)
                {
                    flag=0;
                    break;
                }
            }
            if(!flag)break;
        }
        if(flag)printf("Case #%d: YES\n",ti);
        else printf("Case #%d: NO\n",ti);
    }
    return 0;
}
