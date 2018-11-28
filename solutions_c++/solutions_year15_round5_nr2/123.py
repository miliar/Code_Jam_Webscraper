#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,i,mx,d,e,a[1010],r[1010];
vector<int> g[1010];
long long s,c;
int main() {
  freopen("Bs.in","r",stdin);
  freopen("Bs.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    for (i=0; i<m; i++) {
      g[i].clear();
      g[i].push_back(0);
    }
    for (i=0; i<=n-m; i++) scanf("%d",&a[i]);
    for (i=0; i<n-m; i++) {
      r[i]=a[i+1]-a[i]+g[i%m].back();
      g[i%m].push_back(r[i]);
    }
    for (s=mx=i=0; i<m; i++) {
      sort(g[i].begin(),g[i].end());
      r[i]=g[i].back()-g[i][0];
      mx=max(r[i],mx);
      s-=g[i][0];
    }
    for (c=i=0; i<m; i++) c+=mx-r[i];
    d=((a[0]-s)%m+m)%m-c;
    e=(d>0)?(d+n-1)/n:0;
    printf("Case #%d: %d\n",t,mx+e);
    fprintf(stderr,"Case #%d\n",t);
  }
  return 0;
}
