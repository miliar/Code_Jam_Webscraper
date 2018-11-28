#include<cstdio>
#include<map>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
int solve()
{
    int n,m,i,j,a[101][101],r[101],c[101],p;
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)
    for(j=1;j<=m;j++)
    {
        r[i]=c[j]=0;
        scanf("%d",&a[i][j]);
    }
    for(i=1;i<=n;i++)
    for(j=1;j<=m;j++)
    {
        r[i]=max(r[i],a[i][j]);
        c[j]=max(c[j],a[i][j]);
    }
    for(i=1;i<=n;i++)
    for(j=1;j<=m;j++)
    if(a[i][j]<r[i] && a[i][j]<c[j])
    {
        printf("NO\n");
        return 0;
    }
    printf("YES\n");
}
int main()
{
    int i,t;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
}
