#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cctype>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < n; ++i)
#define rrep(i,n) for(int i = 1; i <= n; ++i)
#define drep(i,n) for(int i = n-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}

const int MX = 100005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;

// Max flow
struct Maxflow {
  int n;
  vector<int> to, lim, next, head, dist, it;
  Maxflow(){}
  Maxflow(int n):n(n),head(n,-1),it(n){}
  void add(int a, int b, int c=1) {
    next.push_back(head[a]); head[a] = to.size(); to.push_back(b); lim.push_back(c);
    next.push_back(head[b]); head[b] = to.size(); to.push_back(a); lim.push_back(0); 
  }
  void bfs(int sv){
    dist = vector<int>(n,INF);
    queue<int> q;
    dist[sv] = 0; q.push(sv);
    while(!q.empty()){
      int v = q.front(); q.pop();
      for(int i = head[v]; i != -1; i = next[i]) {
        if(lim[i] && dist[to[i]] == INF){
          dist[to[i]] = dist[v]+1; q.push(to[i]);
        }
      }
    }
  }
  int dfs(int v, int tv, int nf=INF){
    if(v == tv) return nf;
    for(; it[v] != -1; it[v] = next[it[v]]){
      int u = to[it[v]], f;
      if(!lim[it[v]] || dist[v] >= dist[u]) continue;
      if(f = dfs(u, tv, min(nf, lim[it[v]])), f){
        lim[it[v]] -= f;
        lim[it[v]^1] += f;
        return f;
      }
    }
    return 0;
  }
  int solve(int sv, int tv){
    int flow = 0, f;
    while(1){
      bfs(sv);
      if(dist[tv] == INF) return flow;
      rep(i,n) it[i] = head[i];
      while(f = dfs(sv,tv), f) flow += f;
    }
  }
};
//

char inp[MX];

map<string,int> g;

struct Solver {
  int get(string& s) {
    if (g.count(s) == 0) g.insert({s,g.size()});
    return g[s];
  }
  void solve() {
    g.clear();
    int n;
    scanf("%d\n",&n);
    vvi s(n);
    rep(i,n) {
      fgets(inp, MX-5, stdin);
      istringstream is(inp);
      string now;
      while (is >> now) {
        s[i].pb(get(now));
      }
    }
    int w = sz(g);
    Maxflow mf(w*2+2);
    int sv = w*2, tv = sv+1;
    rep(i,n) {
      if (i == 0) {
        rep(j,sz(s[i])) mf.add(sv,s[i][j],INF);
      } else if(i == 1) {
        rep(j,sz(s[i])) mf.add(s[i][j]+w,tv,INF);
      } else {
        rep(j,sz(s[i]))rep(k,sz(s[i])) {
          if (j == k) continue;
          mf.add(s[i][j]+w,s[i][k],INF);
        }
      }
    }
    rep(i,w) mf.add(i,i+w,1);
    cout << mf.solve(sv,tv) << endl;
  }
};

int main(){
  int ts;
  scanf("%d",&ts);
  Solver solver;
  rrep(ti,ts) {
    printf("Case #%d: ",ti);
    solver.solve();
  }
  return 0;
}





