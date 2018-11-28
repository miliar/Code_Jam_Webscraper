#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
#define maxn 1010
double a[maxn],b[maxn];
int n,vis[maxn],match[maxn],g[1010][1010];
int makepair(int u)
{
    for(int i=0;i<n;i++)if(g[u][i])
    {
        if(!vis[i])
        {
            vis[i]=1;
            if(match[i]==-1||makepair(match[i]))
            {
                match[i]=u;
                return 1;
            }
        }
    }
    return 0;
}
int main()
{
    int i,j,ncase,tt=0;
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&ncase);
    while(ncase--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        int ans1=0;
        memset(vis,0,sizeof(vis));
        sort(b,b+n);
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)if(!vis[j]&&b[j]>a[i])
            {
                ans1++;
                vis[j]++;
                break;
            }
        }
        memset(match,-1,sizeof(match));
        memset(g,0,sizeof(g));
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                if(a[i]>b[j])
                    g[i][j]=1;
        int tot=0;
        for(i=0;i<n;i++)
        {
            memset(vis,0,sizeof(vis));
            if(makepair(i))
                tot++;
        }
        printf("Case #%d: %d %d\n",++tt,tot,n-ans1);
    }
}
