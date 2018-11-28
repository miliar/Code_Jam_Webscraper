#include <cstdio>
#include <cassert>

#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x" = " << x << endl
#define _ << " _ " <<

typedef long long llint;

namespace Dinic {
  const int MAXV = 10000000;
  const int MAXE = 10000000;
  const int oo = 1000000000;

  int V, E;
  int last[MAXV], dist[MAXV], curr[MAXV];
  int next[MAXE], cap[MAXE], adj[MAXE];

  void init(int n) {
    V = n;
    E = 0;
    REP(i, V) last[i] = -1;
  }

  void edge(int x, int y, int c1, int c2) {
    adj[E] = y; cap[E] = c1; next[E] = last[x]; last[x] = E++;
    adj[E] = x; cap[E] = c2; next[E] = last[y]; last[y] = E++;
  }

  int push(int x, int sink, int flow) {
    if (x == sink) return flow;

    for (int &e = curr[x]; e != -1; e = next[e]) {
      int y = adj[e];

      if (cap[e] && dist[x] + 1 == dist[y])
        if (int f = push(y, sink, min(flow, cap[e])))
          return cap[e] -= f, cap[e^1] += f, f;
    }
    return 0;
  }

  int run(int src, int sink) {
    int ret = 0;

    for (;;) {
      REP(i, V) curr[i] = last[i];
      REP(i, V) dist[i] = -1;

      queue<int> Q;
      Q.push(src), dist[src] = 0;

      while (!Q.empty()) {
        int x = Q.front(); Q.pop();

        for (int e = last[x]; e != -1; e = next[e]) {
          int y = adj[e];
          if (cap[e] && dist[y] == -1) Q.push(y), dist[y] = dist[x] + 1;
        }
      }
      if (dist[sink] == -1) break;

      while (int f = push(src, sink, oo)) ret += f;
    }

    return ret;
  }
}

const int dx[4] = { 1, 0 };
const int dy[4] = { 0, 1 };

int W, H, B;
bool wall[600][600];

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    scanf("%d%d%d", &W, &H, &B);

    REP(x, W) REP(y, H) wall[x][y] = false;

    REP(i, B) {
      int x1, y1, x2, y2;
      scanf("%d%d", &x1, &y1);
      scanf("%d%d", &x2, &y2);
      for (int x = x1; x <= x2; ++x)
        for (int y = y1; y <= y2; ++y)
          wall[x][y] = true;
    }

    int V = W*H * 2;
    int src = V++;
    int sink = V++;
    Dinic::init(V);

    REP(x, W) REP(y, H) {
      int p = x * H + y;
      if (wall[x][y]) continue;

      REP(i, 2) {
        int xx = x + dx[i];
        int yy = y + dy[i];

        if (xx >= W || yy >= H) continue;
        if (wall[xx][yy]) continue;

        int q = xx * H + yy;
        Dinic::edge(p+W*H, q, 1, 0);
        Dinic::edge(q+W*H, p, 1, 0);
      }

      Dinic::edge(p, p+W*H, 1, 0);
      if (y == 0) Dinic::edge(src, p, 1, 0);
      if (y == H-1) Dinic::edge(p+W*H, sink, 1, 0);
    }

    printf("Case #%d: %d\n", tt, Dinic::run(src, sink));
  }
  return 0;
}
