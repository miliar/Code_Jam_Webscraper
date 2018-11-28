/*
#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif
*/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <time.h>
#include <vector>
// #include <sys/time.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define x first
#define y second
#define fi(n) fo(i, n)
#define fj(n) fo(j, n)
#define fk(n) fo(k, n)
#define fd(i,n) for(int i=(int)(n)-1;i>=0;--i)
#define fo(i,n) fr(i,0,n)
#define fr(i,a,b) for(int i=(int)(a); i<(int)(b); i++)
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define srt(x) sort(all(x))
//#define lgLowestBit(x) __builtin_ctz(x)
//#define bitCount(x) __builtin_popcount(x)
//#define foreach(it, a) for(__typeof((a).begin()) it=(a).begin(); it != (a).end(); it++)
//#define me (*this)
//#define PQ(t) priority_queue< t, vector< t >, greater< t > >
//#define CLR(a, v) memset(a, v, sizeof(a))
//#define UNIQUE(a) srt(a), a.resize(unique(all(a))-a.begin())
//#define RAND (((double)rand()/RAND_MAX) + ((double)rand()/RAND_MAX/RAND_MAX))
//#define assert(cond,msg) if(!(cond)){ fprintf(stderr, "assert failed at line %d: %s\n", __LINE__, msg); exit(1); }
/*
char systemBuffer[1<<10];
#define execute(...) {\
  sprintf(systemBuffer, __VA_ARGS__); \
  system(systemBuffer); \
}

#ifdef LOCAL
  #define debug(msg, ...) fprintf(stderr, msg, __VA_ARGS__)
#else
  #define debug(msg, ...)
#endif
*/
typedef long long ll;
typedef pair<int, int> ii;
typedef vector< ii > vii;
typedef vector< vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;
typedef vector< string > vs;
typedef vector< double > vd;
typedef vector< vd > vvd;
typedef vector< ll > vll;
typedef vector< bool > vb;

const int INF = 1000*1000*1000+7;
const double EPS = 1e-9;
const double PI = acos(-1.0);
template<class T> int chmin(T &t, T f){ return (t>f) ? (t=f, 1) : 0; }
template<class T> int chmax(T &t, T f){ return (t<f) ? (t=f, 1) : 0; }

/* 
struct timeval startTime, finishTime;
double timeElapsed(){
  gettimeofday(&finishTime, NULL);
  int top = finishTime.tv_sec-startTime.tv_sec-(startTime.tv_usec > finishTime.tv_usec);
  int bot = finishTime.tv_usec-startTime.tv_usec;
  if(bot < 0)
    bot += 1e6;
  return top+bot/1e6;
}
*/
inline int getint() {
  int a;
  return scanf("%d", &a) ? a : (fprintf(stderr, "trying to read\n"),-1);
}

inline double getdouble() {
  double a;
  return scanf("%lf", &a) ? a : (fprintf(stderr, "trying to read\n"),-1);
}




struct edge {
  int v, rid, c, f;
  edge(int _v, int _c, int _r) : v(_v), rid(_r), c(_c), f(0) {}
};
struct flow_graph {
  vector< vector<edge> > adj;
  vector<int> p;
  flow_graph(int n) : adj(n), p(n) {}
  void add_edge(int u, int v, int c) {
    // doesn't handle loops
    adj[u].pb(edge(v, c, adj[v].size()));
    adj[v].pb(edge(u, 0, adj[u].size() - 1));
  }
  bool find_flows(int s, int t) {
    fill(p.begin(), p.end(), -1);
    p[s] = -2;
    queue<int> q;
    for (q.push(s); !q.empty(); q.pop()) {
      int v = q.front();
      for (int i = 0; i < sz(adj[v]); i++) {
        edge e = adj[v][i];
        if (p[e.v] == -1 && e.c) {
          p[e.v] = e.rid;
          q.push(e.v);
        }
      }
    }
    return p[t] != -1;
  }

  int augment_flows(int s, int t) {
    int res = 0;
    for (int i = 0; i < sz(adj[t]); i++) {
      int v = adj[t][i].v, vid = adj[t][i].rid;
      if (adj[v][vid].c && p[v] != -1) {
        int f = adj[v][vid].c;
        for (int u = v; u != s; u = adj[u][p[u]].v) {
          int x = adj[u][p[u]].v, xid = adj[u][p[u]].rid;
          f = min(f, adj[x][xid].c);
        }
        if (!f) continue;
        adj[v][vid].c -= f;
        adj[t][i].c += f;
        for (int u = v; u != s; u = adj[u][p[u]].v) {
          int x = adj[u][p[u]].v, xid = adj[u][p[u]].rid;
          adj[x][xid].c -= f;
          adj[u][p[u]].c += f;
        }
        res += f;
      }
    }
    return res;
  }

  int max_flow(int s, int t) {
    int res = 0;
    while (find_flows(s, t)) {
      res += augment_flows(s, t);
    }
    return res;
  }
};

int board[100][500], w, h, b;
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};
int onboard(int i, int j){ return i>=0 && i<w && j>=0 && j<h; }

void myCode() {

  int ttt=getint();
  fo(tt,ttt){
    fprintf(stderr, "tt = %d\n", tt);
    w=getint(), h=getint(), b=getint();
    int s=2*w*h, half=w*h;
    flow_graph fg(s+2);
    fi(w)
      fj(h)
        board[i][j] = 1;
    fi(b){
      int x0=getint(), y0=getint(), x1=getint(), y1=getint();
      fr(j,x0,x1+1)
        fr(k,y0,y1+1)
          board[j][k] = 0;
    }
    fi(w)
      fj(h)
        if(board[i][j]){
          fk(4)
            if(onboard(i+di[k], j+dj[k]) && board[i+di[k]][j+dj[k]])
              fg.add_edge(half + j*w+i, (j+dj[k])*w+(i+di[k]), 1);
          fg.add_edge(j*w+i, half + j*w+i, 1);
        }
    fi(w){
      if(board[i][0])
        fg.add_edge(s, i, 1);
      if(board[i][h-1])
        fg.add_edge(half + (h-1)*w+i, s+1, 1);
    }
    printf("Case #%d: %d\n", tt+1, fg.max_flow(s, s+1));
  }

}

int main() {
/*
  // seed the random number generator with microseconds
  gettimeofday(&startTime, NULL);
  srand(startTime.tv_usec);
*/
  myCode();
  return 0;
}










