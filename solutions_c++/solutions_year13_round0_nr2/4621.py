#include<stdio.h>
#include<algorithm>
  
  using namespace std;
  int a[105][105],b[105],c[105];
  
main()
{
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  
  int T,t,i,j,n,m,x;
  
  scanf("%d",&T);
  for(t=1;t<=T;t++)
  {
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)
      for(j=1;j<=m;j++)
        scanf("%d",&a[i][j]);
    for(i=1;i<=n;i++)
    {
      b[i]=a[i][1];
      for(j=1;j<=m;j++)
        b[i]=max(b[i],a[i][j]);
    }
    for(i=1;i<=m;i++)
    {
      c[i]=a[1][i];
      for(j=1;j<=n;j++)
        c[i]=max(c[i],a[j][i]);
    }
    x=0;
    for(i=1;i<=n;i++)
    {
      for(j=1;j<=m;j++)
        if(a[i][j]<b[i] && a[i][j]<c[j]){x=1;i=n+1;break;}
    }
    if(x==1)printf("Case #%d: NO\n",t);
      else printf("Case #%d: YES\n",t);
  }
}  
