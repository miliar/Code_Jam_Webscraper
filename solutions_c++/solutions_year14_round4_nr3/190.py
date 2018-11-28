#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int t,tt,w,h,i,j,n,cur,inf,xa[1010],ya[1010],xb[1010],yb[1010],g[1010][1010],p[1010];
bool was[1010];
void edge(int i, int j, int w) {
  g[i][j]=g[j][i]=w;
}
int main() {
  freopen("Cl.in","r",stdin);
  freopen("Cl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d",&w,&h,&n);
    edge(n,n+1,w);
    for (i=0; i<n; i++) {
      scanf("%d%d%d%d",&xa[i],&ya[i],&xb[i],&yb[i]);
      edge(n,i,xa[i]);
      edge(i,n+1,w-xb[i]-1);
      for (j=0; j<i; j++) {
        if (xb[i]<xa[j]) {
          cur=xa[j]-xb[i]-1;
        } else if (xb[j]<xa[i]) {
          cur=xa[i]-xb[j]-1;
        } else cur=0;
        if (yb[i]<ya[j]) {
          cur=max(cur,ya[j]-yb[i]-1);
        } else if (yb[j]<ya[i]) {
          cur=max(cur,ya[i]-yb[j]-1);
        }
        edge(i,j,cur);
      }
    }
    inf=2000000000;
    for (i=0; i<=n+1; i++) {
      was[i]=false;
      p[i]=int(i!=n)*inf;
    }
    while (true) {
      j=n+1;
      for (i=0; i<=n+1; i++) if (!was[i] && p[i]<p[j]) j=i;
      if (j==n+1) break;
      was[j]=true;
      for (i=0; i<=n+1; i++) p[i]=min(p[i],p[j]+g[j][i]);
    }
    printf("Case #%d: %d\n",t,p[n+1]);
  }
  return 0;
}
