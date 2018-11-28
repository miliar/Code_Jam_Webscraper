/* Written by Filip Hlasek 2014 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

#define MAXN 1111
int W, H, B;
int X1[MAXN], Y1[MAXN], X2[MAXN], Y2[MAXN];
int dist[MAXN];

priority_queue<pair<int, int> > pq;
void add(int d, int b) {
  if (dist[b] <= d) return;
  dist[b] = d;
  pq.push(make_pair(-d, b));
}

int get_dist(int b1, int b2) {
  int vdist = 0, hdist = 0;
  if (X1[b1] > X2[b2]) vdist = X1[b1] - X2[b2] - 1;
  if (X1[b2] > X2[b1]) vdist = X1[b2] - X2[b1] - 1;
  if (Y1[b1] > Y2[b2]) hdist = Y1[b1] - Y2[b2] - 1;
  if (Y1[b2] > Y2[b1]) hdist = Y1[b2] - Y2[b1] - 1;
  return max(vdist, hdist);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  REP(t, T) {
    scanf("%d%d", &W, &H);
    scanf("%d", &B);
    REP(b, B) {
      int x1, y1, x2, y2;
      scanf("%d%d%d%d", X1 + b, Y1 + b, X2 + b, Y2 + b);
      dist[b] = W + 1;
      add(X1[b], b);
    }
    while (!pq.empty()) {
      int d = -pq.top().first, b = pq.top().second;
      pq.pop();
      if (dist[b] != d) continue;
      // printf("b: %d d: %d\n", b, d);
      REP(bb, B) add(d + get_dist(b, bb), bb);
    }

    int ans = W;
    REP(b, B) ans = min(ans, dist[b] + (W - 1 - X2[b]));
    printf("Case #%d: %d\n", t + 1, ans);
  }
  return 0;
}
