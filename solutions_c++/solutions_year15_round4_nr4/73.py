#include <bits/stdc++.h>
using namespace std;
const int md=1000000007;
int t,tt,n,m,i,j,r,nok,f[222][13][2];
long long cnt;
int main() {
  freopen("Dl.in","r",stdin);
  freopen("Dl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    memset(f,0,sizeof(f));
    f[0][1][0]=f[0][1][1]=1;
    for (i=0; i<=n; i++) for (j=1; j<=12; j++) {
      //printf("%d %d %d = %d\n",i,j,0,f[i][j][0]);
      //printf("%d %d %d = %d\n",i,j,1,f[i][j][1]);
      f[i+2][j][1]=(f[i+2][j][1]+f[i][j][0])%md;
      f[i+1][j][0]=(f[i+1][j][0]+f[i][j][1])%md;
      if (m%4==0) {
        cnt=__gcd(4,j);
        nok=4*j/cnt;
        f[i+3][nok][0]=(f[i+3][nok][0]+f[i][j][1]*cnt)%md;
      }
      if (m%6==0) {
        cnt=__gcd(6,j);
        nok=6*j/cnt;
        f[i+2][nok][0]=(f[i+2][nok][0]+f[i][j][1]*cnt)%md;
      }
      if (m%3==0) {
        cnt=__gcd(3,j);
        nok=3*j/cnt;
        f[i+2][nok][0]=(f[i+2][nok][0]+f[i][j][1]*cnt)%md;
      }
    }
    for (r=i=0; i<=12; i++) for (j=0; j<2; j++) r=(r+f[n][i][j])%md;
    printf("Case #%d: %d\n",t,r);
    fprintf(stderr,"Case #%d\n",t);
  }
  return 0;
}
