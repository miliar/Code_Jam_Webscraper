#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

typedef pair<int,int> pairii;
typedef long long llong;

#define pb push_back
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

const int MAXN=10005;
int n,m;
vector<string> gd;
vector<int> nodes;
bool vis[MAXN];
int cyc[MAXN];
int res;

bool dfs(int x, int y) {
  int idx=x*m+y;
  vis[idx]=true;
  int si=0,sj=0;
  if (gd[x][y]=='^') si=-1;
  else if (gd[x][y]=='v') si=1;
  else if (gd[x][y]=='<') sj=-1;
  else sj=1;
  int i=x+si,j=y+sj;
  while (i>=0&&i<n&&j>=0&&j<m) {
    if (gd[i][j]!='.'){
      int u=i*m+j;
      if (vis[u]) {
        if (cyc[u]==2) {
          cyc[idx]=2;
          return true;
        }
        else if (cyc[u]==1) {
          cyc[idx]=1;
          return false;
        }
        else {
          cyc[idx]=2;
          return true;
        }
      }
      bool tmpr=dfs(i,j);
      if (tmpr) cyc[idx]=2;
      else cyc[idx]=1;
      return tmpr;
    }
    i+=si;
    j+=sj;
  }
  res++;
  return false;
}

bool check() {
  FORZ(i,n) FORZ(j,m) {
    if (gd[i][j]=='.') continue;
    bool valid=false;
    FORZ(k,m) {
      if (k!=j&&gd[i][k]!='.') {
        valid=true;
        break;
      }
    }
    if (valid) continue;
    FORZ(k,n) {
      if (k!=i&&gd[k][j]!='.') {
        valid=true;
        break;
      }
    }
    if (!valid) {
      return false;
    }
  }
  return true;
}

void solve() {
  cin>>n>>m;
  gd.clear();
  gd.resize(n);
  nodes.clear();
  memset(cyc, 0, sizeof cyc);
  memset(vis,0,sizeof vis);
  res=0;
  FORZ(i,n) cin>>gd[i];
  FORZ(i,n) FORZ(j,m) {
    if (gd[i][j]!='.') {
      nodes.pb(i*m+j);
    }
  }
  if (nodes.size()>0) {
    if (!check()) {
      cout<<"IMPOSSIBLE\n";
      return;
    }
  }
  FORZ(i,nodes.size()) {
    int x=nodes[i]/m;
    int y=nodes[i]%m;
    if (!vis[nodes[i]]&&gd[x][y]!='.') dfs(x,y);
  }
  cout<<res<<"\n";
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
