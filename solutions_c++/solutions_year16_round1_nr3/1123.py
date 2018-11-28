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

const int MAXN=1005;
set<int> hf;
int n, ar[MAXN];
vector<vector<int>>br;
bool vis[MAXN];
int depth[MAXN];

int bfs(int u) {
  int res=0;
  int xx=ar[u];
  queue<pairii> q;
  q.push(pairii(u,0));
  while (!q.empty()) {
    pairii p=q.front();
    q.pop();
    int v=p.first, d=p.second;
    if (v==xx) continue;
    res=max(res,d);
    for (int c:br[v]) q.push(pairii(c,d+1));
  }
  return res;
}

void dfs(int r, int d, int& mx) {
  vis[r]=true;
  depth[r]=d;
  if (vis[ar[r]]) {
    mx=max(mx,d-depth[ar[r]]+1);
    return;
  }
  else dfs(ar[r],d+1,mx);
}

void solve() {
  hf.clear();
  br.clear();
  memset(vis,0,sizeof vis);
  cin>>n;
  br.resize(n);
  FORZ(i,n) {
    int x;
    cin>>x;
    x--;
    ar[i]=x;
    br[x].pb(i);
  }
  FORZ(i,n) {
    if (i==ar[ar[i]]) {
      hf.insert(i);
      hf.insert(ar[i]);
    }
  }
  int res=0;
  for (int u:hf) {
    res+=bfs(u);
  }
  res+=hf.size();
  FORZ(i,n) {
    int tmp=1;
    memset(vis,0,sizeof vis);
    dfs(i,1,tmp);
    res=max(tmp,res);
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
