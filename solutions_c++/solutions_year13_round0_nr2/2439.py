#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;
const int N=200;
int a[N][N],r[N],c[N];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    int o,m,n,i,j,cas=0;
    scanf("%d",&o);
    while (o--)
    {
        scanf("%d%d",&m,&n);
        memset(r,-1,sizeof(r));
        memset(c,-1,sizeof(c));
        for (i=1; i<=m; i++)
         for (j=1; j<=n; j++)
         {
             scanf("%d",&a[i][j]);
             r[i]=max(r[i],a[i][j]);
             c[j]=max(c[j],a[i][j]);
         }
        int t=1;
        for (i=1; i<=m; i++)
         for (j=1; j<=n; j++)
          if (a[i][j]!=min(r[i],c[j]))
           t=0;
        if (t) printf("Case #%d: YES\n",++cas);
        else printf("Case #%d: NO\n",++cas);
    }
}
