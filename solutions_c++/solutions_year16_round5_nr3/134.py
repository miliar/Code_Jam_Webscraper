#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,i,best,x[1010],y[1010],z[1010],vx[1010],vy[1010],vz[1010];
long long a[1010],r;
bool u[1010];
long long sqr(long long x) { return x*x; }
long long sd(int i, int j) {
  return sqr(x[i]-x[j])+sqr(y[i]-y[j])+sqr(z[i]-z[j]);
}
int main() {
  freopen("Cs.in","r",stdin);
  freopen("Cs.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    for (r=i=0; i<n; i++) {
      scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
      u[i]=(i==0);
    }
    for (i=1; i<n; i++) a[i]=sd(0,i);
    while (!u[1]) {
      best=-1;
      for (i=0; i<n; i++) if (!u[i] && (best==-1 || a[i]<a[best])) best=i;
      r=max(r,a[best]);
      u[best]=true;
      for (i=0; i<n; i++) if (!u[i]) a[i]=min(a[i],sd(best,i));
    }
    printf("Case #%d: %.8lf\n",t,sqrt(r));
    fprintf(stderr,"Case #%d\n",t);
  }
  return 0;
}
