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
const int inf=1000000000;
int t,tt,n,i,x,r,c,now,sta,stb,a[88],d[88][88];
vector<int> g[88];
void dfs(int i, int cur) {
  d[sta][i]=cur;
  for (int j=0; j<g[i].size(); j++) {
    int k=g[i][j];
    if (d[sta][k]==-1) dfs(k,cur+1);
  }
}
int ff(int i, int j) {
  int r=-inf;
  for (int ii=0; ii<g[i].size(); ii++) {
    int ki=g[i][ii];
    if (d[sta][ki]!=d[sta][i]+1) continue;
    if (d[stb][j]==d[stb][i]+1+d[ki][j]) continue;
    if (d[stb][j]==d[stb][ki]+1+d[i][j]) continue;
    int c=inf;
    for (int jj=0; jj<g[j].size(); jj++) {
      int kj=g[j][jj];
      if (d[stb][kj]!=d[stb][j]+1) continue;
      if (d[sta][ki]==d[sta][j]+1+d[kj][ki]) continue;
      if (d[sta][ki]==d[sta][kj]+1+d[j][ki]) continue;
      int now=ff(ki,kj);
      if (d[stb][j]!=d[stb][ki]+d[ki][j]) now+=a[ki];
      if (d[sta][ki]!=d[sta][kj]+d[kj][ki]) now-=a[kj];
      c=min(c,now);
    }
    if (c==inf) {
      int now=ff(ki,j);
      if (d[stb][j]!=d[stb][ki]+d[ki][j]) now+=a[ki];
      c=min(c,now);
    }
    r=max(r,c);
  }
  if (r==-inf) {
    int c=inf;
    for (int jj=0; jj<g[j].size(); jj++) {
      int kj=g[j][jj];
      if (d[stb][kj]!=d[stb][j]+1) continue;
      if (d[sta][i]==d[sta][j]+1+d[kj][i]) continue;
      if (d[sta][i]==d[sta][kj]+1+d[j][i]) continue;
      int now=ff(i,kj);
      if (d[sta][i]!=d[sta][kj]+d[kj][i]) now-=a[kj];
      c=min(c,now);
    }
    if (c==inf) c=0;
    r=max(r,c);
  }
  return r;
}
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n);
    for (i=1; i<=n; i++) {
      scanf("%d",&a[i]);
      g[i].clear();
    }
    for (i=1; i<n; i++) {
      scanf("%d",&x);
      g[x].push_back(i);
      g[i].push_back(x);
    }
    memset(d,255,sizeof(d));
    for (sta=1; sta<=n; sta++) dfs(sta,0);
    for (r=-inf, sta=1; sta<=n; sta++) {
      for (c=inf, stb=1; stb<=n; stb++) {
        now=ff(sta,stb);
        now+=a[sta];
        if (sta!=stb) now-=a[stb];
        c=min(c,now);
        //printf("%d %d = %d %d\n",sta,stb,c,now);
      }
      r=max(r,c);
    }
    printf("Case #%d: %d\n",t,r);
  }
  return 0;
}
