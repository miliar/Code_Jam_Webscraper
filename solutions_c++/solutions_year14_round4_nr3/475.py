#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(a) (int((a).size()))
#define all(a) (a).begin(), (a).end()

#define For(it,c) for(typeof(c) it = ((c).begin()); it != ((c).end()) ; ++it)

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

typedef complex<int> cI;
typedef complex<double> cD;

typedef pair<int,int> pI;
typedef pair<ll, ll> pL;

const int INF = 1e9;

int inv[550][550], num[550][550];
int Sink, cnt;

struct edge{
  int to, cap, nxt;
  edge(){}
  edge(int a, int b, int c){
    to = a, cap = b,  nxt = c;
  }
};

int G[150000];
vector< edge > E;
int iter[150000], d[150000];

void init(){
  E.clear();
  for(int i=0;i<cnt+cnt;i++) G[i] = -1;
}
void add_edge(int u, int v){
  E.pb(edge(v, 1, G[u]));
  G[u] = sz(E) -1;
  E.pb(edge(u, 0, G[v]));
  G[v] = sz(E)-1;
}

void bfs(int S){
  for(int i=0;i<cnt+cnt;i++)d[i] = -1;
  d[S] = 0;
  queue<int> Q;
  Q.push(S);
  while(sz(Q)){
    int u = Q.front(); Q.pop();
    for(int i=G[u];i!=-1;i = E[i].nxt){
      if(E[i].cap > 0 && d[E[i].to] < 0){
        d[E[i].to] = d[u] + 1;
        Q.push(E[i].to);
      }
    }
  }
}

int dfs(int S, int T, int c){
  if(S==T) return c;
  for(int &i = iter[S]; i!=-1 ; i = E[i].nxt){
    edge &e = E[i];
    if(e.cap > 0 && d[S] < d[e.to]){
      int t;
      if((t = dfs(e.to, T, min(c, e.cap)))>0){
        e.cap -= t;
        E[i^1].cap += t;
        return t;
      }
    }
  }
  return 0;
}


int main()
{
  int ans;
  int T;
  int W, H, B;
  int x0, x1, y0, y1;
  cin >> T;
  for(int z=1;z<=T;z++){
    cin >> W >> H >> B;
    for(int i=0;i<W;i++)
      for(int j=0;j<H;j++)
        inv[i][j] = 0;
    while(B--){
      cin >> x0 >> y0 >> x1 >> y1;
      for(int i=x0;i<=x1;i++)
        for(int j=y0;j<=y1;j++)
          inv[i][j] = 1;
    }
    cnt = 1;
    for(int i=0;i<W;i++){
      for(int j=0;j<H;j++){
        if(!inv[i][j]){
          num[i][j] = cnt++;
        }
      }
    }
    Sink = cnt++;
    init();
    for(int i=0;i<W;i++){
      if(!inv[i][0]){
        add_edge(0, num[i][0]);
      }
      if(!inv[i][H-1]){
        add_edge(num[i][H-1]+cnt, Sink);
      }
    }
    for(int i=0;i<W;i++){
      for(int j=0;j<H;j++){
        if(!inv[i][j]){
          add_edge(num[i][j], num[i][j]+cnt);
          if(i+1<W && inv[i+1][j]==0){
            add_edge(num[i][j]+cnt, num[i+1][j]);
            add_edge(num[i+1][j]+cnt, num[i][j]);
          }
          if(j+1<H && inv[i][j+1]==0){
            add_edge(num[i][j]+cnt, num[i][j+1]);
            add_edge(num[i][j+1]+cnt, num[i][j]);
          }
        }
      }
    }
    ans = 0;
    while(1){
      bfs(0);
      if(d[Sink]<0)break;
      for(int i=0;i<cnt+cnt;i++)iter[i] = G[i];
      int a;
      while((a=dfs(0, Sink, INF))) ans += a;
    }
    printf("Case #%d: %d\n", z, ans);
  }
  return 0;
}
