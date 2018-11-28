#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXN 20
using namespace std;

int a[MAXN+1],b[MAXN+1],u[MAXN+1],x[MAXN+1],f[MAXN+1],g[MAXN+1];
int n;

int check()
{
    int i,j;
    for(i=n;i>=1;i--)
    {
        g[i]=1;
        for(j=i+1;j<=n;j++)
        {
            if(x[i]>x[j])
            {
                g[i]=max(g[i],g[j]+1);
            }
        }
        if(g[i]!=b[i])
        {
            return 0;
        }
    }
    return 1;
}

int DFS(int i)
{
    int j,v;
    if(i>n)
    {
        return check();
    }
    for(v=1;v<=n;v++)
    {
        if(u[v]==0)
        {
            x[i]=v;
            f[i]=1;
            for(j=1;j<i;j++)
            {
                if(x[i]>x[j])
                {
                    f[i]=max(f[i],f[j]+1);
                }
            }
            if(f[i]==a[i])
            {
                u[v]=1;
                if(DFS(i+1)==1)
                {
                    return 1;
                }
                u[v]=0;
            }
        }
    }
    return 0;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int c,t,i;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        memset(u,0,sizeof(u));
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
        }
        for(i=1;i<=n;i++)
        {
            scanf("%d",&b[i]);
        }
        DFS(1);
        printf("Case #%d:",c+1);
        for(i=1;i<=n;i++)
        {
            printf(" %d",x[i]);
        }
        printf("\n");
    }
    return 0;
}
