#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdio>
#include <string>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef pair<int,int> pii;
int t,tt,p,q,n,i,j,k,e,l,r,cur,cc,h[102],g[102],f[102][1202][2];
int main() {
  freopen("Bl.in","r",stdin);
  freopen("Bl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d",&p,&q,&n);
    for (i=0; i<n; i++) scanf("%d%d",&h[i],&g[i]);
    memset(f,255,sizeof(f));
    f[0][0][0]=0;
    for (i=0; i<n; i++) for (j=0; j<=12*i; j++) for (k=0; k<2; k++) if (f[i][j][k]>=0) {
      for (e=0; e<=j; e++) {
        cur=h[i]-e*p;
        if (cur<=0) {
          f[i+1][j-e][k]=max(f[i+1][j-e][k],f[i][j][k]+g[i]);
          break;
        }
        for (l=k; ; l++) {
          cc=cur-l*q;
          if (cc<=0) {
            f[i+1][j-e+l-k][0]=max(f[i+1][j-e+l-k][0],f[i][j][k]);
            break;
          }
          if ((cc-1)%(p+q)<p) f[i+1][j-e+l-k][1]=max(f[i+1][j-e+l-k][1],f[i][j][k]+g[i]);
        }
      }
    }
    for (r=i=0; i<=12*n; i++) for (k=0; k<2; k++) r=max(r,f[n][i][k]);
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}
