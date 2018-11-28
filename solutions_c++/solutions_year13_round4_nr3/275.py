#include<cstdio>
#include<algorithm>
using namespace std;

int a[1000],b[1000],c[1000];
int n;

bool dfs(int dep)
{
    if (dep==n+1) return 1;
    for (int i=1;i<=n;i++)
    if (!c[i])
    {
        c[i]=dep;
        int x,y;
        int f[25],g[25];
        for (int ii=1;ii<=i;ii++)
        {
            f[ii]=c[ii]>0;
            for (int j=1;j<ii;j++)
            if (c[j] && c[j]<c[ii]) f[ii]=max(f[ii],f[j]+1);
        }
        for (int ii=n;ii;ii--)
        {
            g[ii]=c[ii]>0;
            for (int j=ii+1;j<=n;j++)
            if (c[j] && c[j]<c[ii]) g[ii]=max(g[ii],g[j]+1);
        }
        if (f[i]==a[i] && g[i]==b[i])
        {
            if (dfs(dep+1)) return 1;
        }
        c[i]=0;
    }
    return 0;
}

int main()
{
    int t,id;
    scanf("%d",&t);
    for (int id=1;id<=t;id++)
    {
        scanf("%d",&n);
        for (int i=1;i<=n;i++) scanf("%d",&a[i]);
        for (int i=1;i<=n;i++) scanf("%d",&b[i]);
        dfs(1);
        printf("Case #%d: ",id);
        for (int i=1;i<=n;i++) printf("%d%c",c[i],i==n?'\n':' ');
        for (int i=1;i<=n;i++) c[i]=0;
    }
}
