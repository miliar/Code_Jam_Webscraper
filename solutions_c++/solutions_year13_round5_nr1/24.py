#include <cstdio>
#include <algorithm>
using namespace std;
long long n,l,r,h,c,z,a[39];
int t,tt,m,i,j;
double res;
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%I64d%d",&n,&m);
	for (i=0; i<37; i++) a[i]=0;
	for (i=0; i<m; i++) scanf("%I64d",&a[i]);
	sort(a,a+37);
	for (res=i=0; i<37; i++) {
	  l=a[i]; r=a[i]+n;
	  while (l<r) {
	    h=(l+r)/2;
		for (c=j=0; j<=i; j++) c+=h-a[j];
		for (; j<37; j++) c+=max(0LL,h+1-a[j]);
		if (c<=n) l=h+1; else r=h;
	  }
	  h=r-1;
	  if (h>=a[i]) {
	    for (c=z=j=0; j<=i; j++) { c+=h-a[j]; z+=h-a[j]; }
		for (; j<37; j++) c+=max(0LL,h+1-a[j]);
	    res=max(res,(36.*z)/(i+1.)-c);
	  }
	}
    printf("Case #%d: %.10lf\n",t,res);
  }
  return 0;
}
