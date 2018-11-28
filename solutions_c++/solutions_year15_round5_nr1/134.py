#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,M,As,Cs,Rs,Am,Cm,Rm,i,r,cnt,a[1000100],d[2000200];
vector<int> g[1000100];
void dfs(int i, int lo, int hi) {
  if (a[i]<lo) lo=a[i];
  if (a[i]>hi) hi=a[i];
  if (hi-lo>m) return;
  d[hi]++;
  d[lo+m+1]--;
  for (int j=0; j<g[i].size(); j++) {
    int k=g[i][j];
    dfs(k,lo,hi);
  }
}
int main() {
  freopen("As.in","r",stdin);
  freopen("As.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    scanf("%d%d%d%d",&a[0],&As,&Cs,&Rs);
    scanf("%d%d%d%d",&M,&Am,&Cm,&Rm);
    for (i=0; i<n; i++) g[i].clear();
    for (i=1; i<n; i++) {
      a[i]=(1LL*a[i-1]*As+Cs)%Rs;
      M=(1LL*M*Am+Cm)%Rm;
      g[M%i].push_back(i);
    }
    memset(d,0,sizeof(d));
    dfs(0,a[0],a[0]);
    for (r=cnt=i=0; i<=2000000; i++) {
      cnt+=d[i];
      r=max(r,cnt);
    }
    printf("Case #%d: %d\n",t,r);
    fprintf(stderr,"Case #%d\n",t);
  }
  return 0;
}
