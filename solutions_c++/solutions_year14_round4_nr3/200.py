/*
 * 
 * File:   DontBreakTheNile.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on May 31, 2014, 10:28:00 AM
 */

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <complex>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

using namespace std;

namespace DontBreakTheNile {
template <class Flow, size_t MAXV, size_t MAXE> struct MaxFlow {
  Flow cap[MAXE << 1], flow[MAXE << 1], limit[MAXV];
  int last[MAXV], to[MAXE << 1], next[MAXE << 1];
  int prev[MAXV], cur[MAXV], height[MAXV], cnt[MAXV + 1];
  int edgecnt, vertices;

  void resetflow() {
    fill(flow, flow + edgecnt, 0);
  }

  void init() {
    memset(last, -1, sizeof(last));
    vertices = edgecnt = 0;
  }

  void _addedge(int a, int b, Flow c) {
    flow[edgecnt] = 0;
    to[edgecnt] = b;
    cap[edgecnt] = c;
    next[edgecnt] = last[a];
    if (last[a] == -1)
      vertices++;
    last[a] = edgecnt++;
  }

  void addedge(int start, int end, Flow capacity, bool directed = true) {
    _addedge(start, end, capacity);
    _addedge(end, start, directed ? 0 : capacity);
  }

  Flow go(int source, int sink) {
    const Flow INF = numeric_limits<Flow>::max();
    Flow maxflow = 0;
    memset(prev, -1, sizeof(prev));
    memset(cur, -1, sizeof(cur));
    memset(height, 0, sizeof(height));
    memset(cnt, 0, sizeof(cnt));
    fill(limit, limit + MAXV, 0);
    cnt[0] = vertices;
    int at = source, e = -1;
    limit[at] = INF;
    while (height[source] < vertices) {
      for (e = cur[at]; e > -1; e = next[e])
        if (flow[e] < cap[e] && height[to[e]] + 1 == height[at])
          break;
      if (e > -1) {
        cur[at] = prev[to[e]] = e;
        limit[to[e]] = min(limit[at], cap[e] - flow[e]);
        at = to[e];
        if (at == sink)
          for (maxflow += limit[sink]; at != source; at = to[prev[at] ^ 1])
            flow[prev[at]] += limit[sink], flow[prev[at] ^ 1] -= limit[sink];
      } else {
        if (--cnt[height[at]] == 0)
          break;
        height[at] = vertices;
        for (e = last[at]; e > -1; e = next[e])
          if (flow[e] < cap[e] && height[to[e]] + 1 < height[at])
            height[at] = height[to[e]] + 1, cur[at] = e;
        cnt[height[at]]++;
        if (at != source)
          at = to[prev[at] ^ 1];
      }
    }
    return maxflow;
  }
};

MaxFlow<int, 111000, 555000> net;
int W, H, B, x1[10], y1[10], x2[10], y2[10];

inline int encode(int x, int y) {
  return x * H + y;
}

void solve(int test_num) {
  scanf("%d %d %d", &W, &H, &B);
  for (int i = 0; i < B; i++)
    scanf("%d %d %d %d", x1 + i, y1 + i, x2 + i, y2 + i);
  net.init();
  const int N = W * H;
  for (int x = 0; x < W; x++) {
    for (int y = 0; y < H; y++) {
      bool ok = true;
      for (int i = 0; i < B; i++)
        ok &= !(x1[i] <= x && x <= x2[i] && y1[i] <= y && y <= y2[i]);
      if (ok) {
        net.addedge(encode(x, y), encode(x, y) + N, 1);
        if (x > 0)
          net.addedge(encode(x, y) + N, encode(x - 1, y), 1);
        if (y > 0)
          net.addedge(encode(x, y) + N, encode(x, y - 1), 1);
        if (x + 1 < W)
          net.addedge(encode(x, y) + N, encode(x + 1, y), 1);
        if (y + 1 < H)
          net.addedge(encode(x, y) + N, encode(x, y + 1), 1);
      }
    }
  }
  const int SRC = N + N, SINK = SRC + 1;
  for (int x = 0; x < W; x++) {
    net.addedge(SRC, encode(x, 0), 1);
    net.addedge(encode(x, H - 1) + N, SINK, 1);
  }
  const int res = net.go(SRC, SINK);
  printf("Case #%d: %d\n", test_num, res);
}

void solve() {
#ifdef AZN
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  freopen("azn.txt", "w", stderr);
#endif
  int tests;
  scanf("%d", &tests);
  for (int i = 1; i <= tests; i++)
    solve(i);
}
}

int main() {
  DontBreakTheNile::solve();
  return 0;
}
