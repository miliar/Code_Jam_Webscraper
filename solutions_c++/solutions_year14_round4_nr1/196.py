#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,n,m,r,i,j,a[10100];
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    for (i=0; i<n; i++) scanf("%d",&a[i]);
    sort(a,a+n);
    r=n; j=n-1;
    for (i=0; i<j; i++) {
      while (j>i && a[j]+a[i]>m) j--;
      if (i<j) {
        r--; j--;
      }
    }
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}
