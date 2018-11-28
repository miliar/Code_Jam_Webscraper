#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,M,i,j,a[202];
double p[202],f[202][414],r;
double solve() {
  memset(f,0,sizeof(f));
  f[0][M]=1;
  for (int i=0; i<M; i++) for (int j=0; j<=2*M; j++) if (f[i][j]) {
    double cur=p[a[i+1]];
    f[i+1][j+1]+=f[i][j]*cur;
    if (j==0) puts("!!");
    f[i+1][j-1]+=f[i][j]*(1.-cur);
  }
  return f[M][M];
}
int main() {
  freopen("Bl.in","r",stdin);
  freopen("Bl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    cin>>n>>m; M=m; r=0;
    for (i=1; i<=n; i++) cin>>p[i];
    sort(p+1,p+n+1);
    for (j=0; j<=m; j++) {
      for (i=1; i<=j; i++) a[i]=i;
      for (i=j+1; i<=m; i++) a[i]=n-(m-i);
      r=max(r,solve());
    }
    printf("Case #%d: %.10f\n",t,r);
    fprintf(stderr,"Case #%d: %.10f\n",t,r);
  }
  return 0;
}
