/*
 * c-small.cpp
 *
 *  Created on: May 31, 2014
 *      Author: istrandjev
 */

#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#include <unordered_set>
#include <unordered_map>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

typedef int dintype;
struct edge {
  edge(int t_ = 0, int n_ = 0, dintype c_ = 0) {
    to = t_;
    next = n_;
    cap = c_;
  }
  int to, next;
  dintype cap;
};
const int max_edges = 731010;
const int max_nodes = 160010;
const dintype inf = 2000000000;
edge e[max_edges];
int first[max_edges];
int edges_num = 0;
int vis[max_nodes], used[max_nodes];
int source, sink;
inline void add_edge(int from, int to, dintype cap) {
  if (edges_num == 0) {
    memset(first, -1, sizeof(first));
  }
  e[edges_num].to = to;
  e[edges_num].cap = cap;
  e[edges_num].next = first[from];
  first[from] = edges_num++;

  e[edges_num].to = from;
  e[edges_num].cap = 0;
  e[edges_num].next = first[to];
  first[to] = edges_num++;
}
dintype dfs(int node, dintype cap) {
  dintype r;
  if (node == sink) {
    return cap;
  }
  for (int index = first[node]; index != -1; index = e[index].next) {
    if (!used[e[index].to] && e[index].cap > 0
        && vis[node] == vis[e[index].to] + 1) {
      r = dfs(e[index].to, min(cap, e[index].cap));
      if (r != -1) {
        e[index].cap -= r;
        e[index ^ 1].cap += r;
        return r;
      }
    }
  }
  used[node] = 1;
  return -1;
}
dintype dinitz(const vector<vector<pair<int, dintype> > >& nt, int so, int si) {
  memset(used, 0, sizeof(used));
  memset(vis, 0, sizeof(vis));
  edges_num = 0;
  int n = (int)nt.size();
  source = so;
  sink = si;
  dintype flow = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < (int)nt[i].size(); j++) {
      add_edge(i, nt[i][j].first, nt[i][j].second);
    }
  }
  while (true) {
    queue<int> tc;
    memset(vis, -1, sizeof(vis));
    tc.push(sink);
    vis[sink] = 0;
    while (!tc.empty() && vis[source] == -1) {
      int c = tc.front();
      tc.pop();
      for (int index = first[c]; index != -1; index = e[index].next) {
        if (e[index ^ 1].cap > 0 && vis[e[index].to] == -1) {
          tc.push(e[index].to);
          vis[e[index].to] = vis[c] + 1;
          if (e[index].to == source)
            break;
        }
      }
    }
    if (vis[source] == -1) {
      break;
    }
    memset(used, 0, sizeof(used));
    bool updated = false;
    while (1) {
      dintype f = dfs(so, inf);
      if (f == -1)
        break;
      flow += f;
      updated = true;
    }
    if (!updated)
      break;
  }
  return flow;
}
int move3[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
int solve(const vector<vector<char> >& a) {
  int n = (int)a.size();
  int m = (int)a[0].size();
  int so = n * m * 2;
  int si = so + 1;
  vector<vector<pair<int, dintype> > > ne(n * m * 2 + 2);

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (a[i][j] == 0) {
        continue;
      }
      ne[i * m + j].push_back(make_pair(n * m + i * m + j, 1));
      for (int l = 0; l < 4; ++l) {
        int tx = i + move3[l][0];
        int ty = j + move3[l][1];
        if (tx < 0 || tx >= n || ty < 0 || ty >= m || a[tx][ty] == 0) {
          continue;
        }
        ne[n * m + i * m + j].push_back(make_pair(tx * m + ty, 1));
      }
    }
  }
  for (int j = 0; j < n; ++j) {
    if (a[j][0] != 0) {
      ne[so].push_back(make_pair(j * m, 1));
    }
    if (a[j][m - 1] != 0) {
      ne[n * m + j * m + m - 1].push_back(make_pair(si, 1));
    }
  }
  return dinitz(ne, so, si);
}

int main() {
  freopen("google.in", "r", stdin);
  freopen("google.out", "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<char> > a(n, vector<char>(m, 1));
    for (int i = 0; i < k; ++i) {
      int x0, y0, x1, y1;
      scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
      for (int j = x0; j <= x1; ++j) {
        for (int l = y0; l <= y1; ++l) {
          a[j][l] = 0;
        }
      }
    }

    cout << "Case #" << it << ": " << solve(a) << endl;
  }
  return 0;
}

