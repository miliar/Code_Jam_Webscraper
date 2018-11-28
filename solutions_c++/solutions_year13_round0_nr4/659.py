#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <ctime>
#include <vector>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;


int f[50][220];
int need[50];
int g[2000000];
int k,n;
bool pd(int i,int j)
{
    int x=f[0][need[j]];
    for (int k=1;k<=n;k++)
    if (i&(1<<(k-1)))
    {
        if (need[k]==need[j]) x--;
        x+=f[k][need[j]];
    }
    if (x>0) return true;
    return false;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=1;
    while (T--)
    {
        memset(f,0,sizeof(f));

        scanf("%d%d",&k,&n);
        for (int i=1;i<=k;i++)
        {
            int x;
            scanf("%d",&x);
            f[0][x]++;
        }
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&need[i]);
            int kk;
            scanf("%d",&kk);
            for (int j=1;j<=kk;j++)
            {
                int x;
                scanf("%d",&x);
                f[i][x]++;
            }
        }
        memset(g,-1,4*(1<<n));
        g[(1<<n)-1]=0;
        for (int i=(1<<n)-1;i>=0;i--)
        {
            for (int j=1;j<=n;j++)
            if ((i&(1<<(j-1)))==0 && pd(i,j))
            {
                if (g[i]!=-1 || g[i+(1<<(j-1))]==-1) continue;
                g[i]=j;
               // cout<<i<<'#'<<(i&(1<<(j-1)))<<endl;
            }
        }
        printf("Case #%d:",cas++);
        if (g[0]==-1)
        printf(" IMPOSSIBLE\n");
        else
        {
            int x=0;
            for (int i=1;i<=n;i++)
            {
                printf(" %d",g[x]);
                x=x+(1<<(g[x]-1));
            }
            printf("\n");
        }
    }
    return 0;
}
