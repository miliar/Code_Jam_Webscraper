#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,i,j,k,ns,a[10100],b[10100],c[1100100];
map<int,int> d;
vector<int> v;
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n); ns=0;
    for (i=0; i<n; i++) scanf("%d",&a[i]);
    for (i=0; i<n; i++) {
      scanf("%d",&b[i]);
      ns+=b[i];
    }
    v.clear(); d.clear(); m=1;
    for (j=0; j<22; j++) if ((1<<j)==b[0]) {
      for (i=0; i<j; i++) {
        v.push_back(0);
        for (k=0; k<m; k++) c[k+m]=c[k];
        m*=2;
      }
      break;
    }
    for (i=1; i<n; i++) while (b[i]-d[a[i]]>0) {
      v.push_back(a[i]);
      for (k=0; k<m; k++) {
        c[k+m]=c[k]+a[i];
        d[c[k+m]]++;
      }
      m*=2;
    }
    sort(v.begin(),v.end());
    printf("Case #%d:",t);
    for (i=0; i<v.size(); i++) printf(" %d",v[i]);
    puts("");
    fprintf(stderr,"Case #%d\n",t);
    if ((1<<int(v.size()))!=ns) fprintf(stderr,"!!!!!!!!!!! #%d\n",t);
  }
  return 0;
}
