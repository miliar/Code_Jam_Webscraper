#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

#define REP(i, n) FOR(i, 0, n)
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

int dist1(int a, int b, int c, int d) {
  if (b <= c) return c-b;
  if (d <= a) return a-d;
  return 0;
}

struct Blok {
  int x1, x2, y1, y2;

  friend int mydist(Blok a, Blok b) {
    int dx = dist1(a.x1, a.x2, b.x1, b.x2);
    int dy = dist1(a.y1, a.y2, b.y1, b.y2);
    return max(dx, dy);
  }
};

int main(void)
{
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    vector<Blok> blocks;
    int w, h, nb; scanf("%d %d %d", &w, &h, &nb);

    REP(i, nb) {
      int x1, y1, x2, y2; scanf("%d %d %d %d", &x1, &y1, &x2, &y2); ++x2; ++y2;
      blocks.push_back({x1, x2, y1, y2});
    }

    int source = nb, sink = nb+1; nb += 2;
    blocks.push_back({0, 0, 0, h});
    blocks.push_back({w, w, 0, h});

    const llint inf = 1e15;
    vector<llint> dist(nb, inf);
    vector<char> bio(nb, false);

    for (dist[source] = 0; ; ) {
      int ex = -1;
      REP(i, nb) if (!bio[i] && dist[i] < inf) if (ex == -1 || dist[i] < dist[ex]) ex = i;
      if (ex == -1) break;
      bio[ex] = true;

      REP(i, nb) {
        if (bio[i]) continue;
        llint val = dist[ex] + mydist(blocks[ex], blocks[i]);
        dist[i] = min(dist[i], val);
      }
    }

    printf("Case #%d: %lld\n", tc+1, dist[sink]);
    fflush(stdout);
  }
  return 0;
}
