//shjj-Lawnmower

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;
int a[100+3][100+3],heng[100+3],shu[100+3];
int n,m;

int main()
{
//freopen("B.in","r",stdin);
//freopen("B.out","w",stdout);
int Test,TT=0;scanf("%d",&Test);
for (;Test--;)
{
scanf("%d%d",&n,&m);
for (int i=1;i<=n;i++)
  for (int j=1;j<=m;j++) scanf("%d",&a[i][j]);
for (int i=1;i<=n;i++)
  {
  heng[i]=a[i][1];
  for (int j=1;j<=m;j++) heng[i]=max(heng[i],a[i][j]);
  }
for (int j=1;j<=m;j++)
  {
  shu[j]=a[1][j];
  for (int i=1;i<=n;i++) shu[j]=max(shu[j],a[i][j]);
  }
bool flag=1;
for (int i=1;i<=n;i++)
  for (int j=1;j<=m;j++) flag&=(heng[i]<=a[i][j]||shu[j]<=a[i][j]);
printf("Case #%d: ",++TT);
if (flag) printf("YES\n");else printf("NO\n");
}
}