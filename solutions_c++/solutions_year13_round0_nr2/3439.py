#include <stdio.h>
using namespace std;
int n,m,a[105][105],maxh[105],maxl[105],i,j,k,cas;
bool can;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    for (k=1;k<=cas;k++)
    {
    scanf("%d%d",&n,&m);
    for (i=1;i<=n;i++)
    for (j=1;j<=m;j++)
    scanf("%d",&a[i][j]);
    for (i=1;i<=n;i++)
    {
        maxh[i]=0;
        for (j=1;j<=m;j++)
        if (a[i][j]>maxh[i])
        maxh[i]=a[i][j];
    }
    for (j=1;j<=m;j++)
    {
        maxl[j]=0;
        for (i=1;i<=n;i++)
        if (a[i][j]>maxl[j])
        maxl[j]=a[i][j];
    }
    can=true;
    for (i=1;i<=n;i++)
    for (j=1;j<=m;j++)
    {
        if (a[i][j]<maxh[i]&&a[i][j]<maxl[j])
        can=false;
    }
    printf("Case #%d: ",k);
    if (can)
    printf("YES\n");
    else
    printf("NO\n");
    }
}
