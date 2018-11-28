/*
 * Code Jam Round 2 2013
 * File:   pATicketSwapping.cpp
 * Author: Andy Y.F. Huang
 * Created on June 1, 2013, 10:37 AM
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

#ifdef AZN
#include "Azn.cpp"
#endif

using namespace std;

namespace pATicketSwapping {
#define MOD 1000002013
template <class Flow, class Cost, size_t MAXV, size_t MAXE> struct MinCostFlow {
  int last[MAXV], to[MAXE << 1], next[MAXE << 1], queue[8 * MAXV], prev[MAXV];
  Flow cap[MAXE << 1], flow[MAXE << 1], amount[MAXV];
  Cost cost[MAXE << 1], dist[MAXV];
  bool vis[MAXV];
  int edgecnt;

  void init() {
    memset(last, -1, sizeof (last));
    edgecnt = 0;
  }

  void __addedge(int s, int t, Flow f, Cost c) {
    to[edgecnt] = t;
    next[edgecnt] = last[s];
    cap[edgecnt] = f;
    flow[edgecnt] = 0;
    cost[edgecnt] = c;
    last[s] = edgecnt++;
  }

  void addedge(int from, int to, Flow flow, Cost cost) {
    __addedge(from, to, flow, cost);
    __addedge(to, from, 0, -cost);
  }

  pair<Flow, Cost> go(int source, int sink) {
    Flow maxflow = 0;
    Cost mincost = 0;
    const Flow INF_FLOW = numeric_limits<Flow>::max();
    const Cost INF_COST = numeric_limits<Cost>::max();
    while (true) {
      fill(dist, dist + MAXV, INF_COST);
      memset(vis, false, sizeof (vis));
      prev[source] = -2;
      dist[source] = 0;
      amount[source] = INF_FLOW;
      int qf = 0, qb = 0;
      queue[qb++] = source;
      vis[source] = true;
      for (; qf < qb; qf++) {
        int at = queue[qf];
        Cost cdist = dist[at];
        for (int id = last[at], v; id != -1; id = next[id]) {
          v = to[id];
          if (flow[id] < cap[id] && cdist + cost[id] < dist[v]) {
            dist[v] = cdist + cost[id];
            prev[v] = id;
            amount[v] = min(amount[at], cap[id] - flow[id]);
            if (!vis[v])
              vis[queue[qb++] = v] = true;
          }
        }
        vis[at] = false;
      }
      if (dist[sink] == INF_COST) break;
      Flow by = amount[sink];
      maxflow += by;
      mincost += dist[sink] * by;
      for (int e = prev[sink]; e > -1; e = prev[to[e ^ 1]])
        flow[e] += by, flow[e ^ 1] -= by;
    }
    return make_pair(maxflow, mincost);
  }

} ;

template <size_t MAXSIZE> struct DisjointSet {
  int tree[MAXSIZE];

  void makeset(int size = MAXSIZE) {
    memset(tree, -1, sizeof (int) * size);
  }

  void unite(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return;
    if (tree[a] > tree[b]) tree[a] = b;
    else {
      if (tree[a] == tree[b]) tree[a]--;
      tree[b] = a;
    }
  }

  int find(int node) {
    return tree[node] < 0 ? node : (tree[node] = find(tree[node]));
  }
} ;

#define INF (1 << 30)
typedef long long llong;
int start[1111], end[1111], cnt[1111];
MinCostFlow<int, llong, 2222, 1000111> net;
DisjointSet<1111> dsu;
int len, trips;

llong cost(int a, int b) {
  return llong(b - a) * len - (b - a) * (b - a - 1LL) / 2;
}

void solve(int test_num) {
  cin >> len >> trips;
  for (int i = 0; i < trips; i++)
    cin >> start[i] >> end[i] >> cnt[i];
  llong total = 0;
  dsu.makeset();
  for (int i = 0; i < trips; i++) {
    total += cnt[i] * cost(start[i], end[i]);
    for (int j = i + 1; j < trips; j++)
      if (start[i] <= end[j] && start[j] <= end[i])
        dsu.unite(i, j);
  }
  net.init();
  for (int i = 0; i < trips; i++) {
    net.addedge(i, i + trips, INF, cost(start[i], end[i]));
    for (int j = i + 1; j < trips; j++) {
      if (start[i] <= end[j] && start[j] <= end[i]) {
        //intersect
        net.addedge(i, j + trips, INF, cost(start[i], end[j]));
        net.addedge(j, i + trips, INF, cost(start[j], end[i]));
      }
      else if (dsu.find(i) == dsu.find(j)) {
        if (start[i] <= end[j])
          net.addedge(i, j + trips, INF, cost(start[i], end[j]));
        else
          net.addedge(j, i + trips, INF, cost(start[j], end[i]));
      }
    }
  }
  int src = trips + trips, sink = src + 1;
  for (int i = 0; i < trips; i++) {
    net.addedge(src, i, cnt[i], 0);
    net.addedge(i + trips, sink, cnt[i], 0);
  }
  pair<int, llong> res = net.go(src, sink);
  printf("Case #%d: %lld\n", test_num, total - res.second);
  //cout << total - res.second << endl;
  //pln(total);
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
  pATicketSwapping::solve();
  return 0;
}

