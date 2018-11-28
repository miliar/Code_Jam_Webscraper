#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <queue>

using namespace std;

#define TRACE(x) cout << #x << " = " << x << endl
#define REP(i, n) for (int i = 0; i < (n); ++i)

typedef long long llint;

typedef pair< int, int > edge;
#define b first
#define d second

const int MAXN = 200000;
const int inf = 1000000000;

class Dinic {
  vector< edge > E[MAXN];
  vector< int > cap[MAXN];
  int dist[MAXN];
  int bio[MAXN];
  int sh[MAXN];
  int cookie, s, t;
  
  queue<int> Q;

  int bfs() {
    cookie++;
    while (!Q.empty()) Q.pop();
    
    bio[s] = cookie;
    dist[s] = 0;
    Q.push(s);
    while (!Q.empty()) {
      int x = Q.front();
      Q.pop();
      
      for (int i = 0; i < (int)E[x].size(); ++i) {
        int y = E[x][i].b;
        if ((bio[y] != cookie || y == t) && cap[x][i] != 0) {
          dist[y] = dist[x]+1;
          bio[y] = cookie;
          if(y != t) Q.push(y);
        }
      }
    }
    return bio[t] == cookie;
  }
  
  int augment(int x, int c) {
    if (x == t) return c;
    
    for (int i = sh[x]; i < (int)E[x].size(); ++i, ++sh[x]) {
      int y = E[x][i].b;
      if (cap[x][i] > 0 && bio[y] == cookie && ( y == t || dist[y] == dist[x]+1)) {
        int v = augment(y, c = min(c, cap[x][i]));
        if (v > 0) { cap[x][i] -= v, cap[y][E[x][i].d] += v; return v; }
      }
    }
    return 0;
  }
  
public:
  void init(int n) {
    REP(i, n) {
      E[i].clear();
      cap[i].clear();
      dist[i] = bio[i] = sh[i] = 0;
    }
  }
  
  void add_edge(int a, int b, int cab, int cba) {
    E[a].push_back(edge(b, E[b].size()));
    E[b].push_back(edge(a, E[a].size()-1));
    cap[a].push_back(cab);
    cap[b].push_back(cba);
  }
  
  int maxflow(int S, int T) {
    s = S, t = T;
    int ans = 0;
    while (bfs()) {
      int f;
      memset(sh, 0, (T+1)*4);
      while ((f = augment(s, inf))) ans += f;
    }
    return ans;
  }
} D;

bool b[1000][1000];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp) {
    int w, h, n;
    scanf("%d %d %d", &w, &h, &n);
    REP(i, w+1) REP(j, h+1)  b[i][j] = false;
    REP(k, n) {
      int x1, y1, x2, y2;
      scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
      for (int i = x1; i <= x2; ++i)
        for (int j = y1; j <= y2; ++j)
          b[i][j] = true;
    }
    
    D.init(2*w*h + 2);

    auto inNode = [&] (int x, int y) { return (h*x + y)*2; };
    auto outNode = [&] (int x, int y) { return (h*x + y)*2 + 1; };

    REP(i, w) REP(j, h)
      if (!b[i][j]) D.add_edge(inNode(i, j), outNode(i, j), 1, 0);
    REP(i, w) REP(j, h) {
      if (i+1 < w) D.add_edge(outNode(i, j), inNode(i+1, j), 1, 0);
      if (j+1 < h) D.add_edge(outNode(i, j), inNode(i, j+1), 1, 0);
      if (i-1 >= 0) D.add_edge(outNode(i, j), inNode(i-1, j), 1, 0);
      if (j-1 >= 0) D.add_edge(outNode(i, j), inNode(i, j-1), 1, 0);

    }

    int s = 2*w*h;
    int t = s + 1;
    REP(i, w) D.add_edge(s, inNode(i, 0), 1, 0);
    REP(i, w) D.add_edge(outNode(i, h-1), t, 1, 0);

    printf("Case #%d: ", tp);
    printf("%d\n", D.maxflow(s, t));
  }
  return 0;
}
