#define NDEBUG
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <utility>
#include <vector>
using namespace std;

#define ZERO(v) memset((v), 0, sizeof (v))
#define MINUSONE(v) memset((v), -1, sizeof (v))

struct Building {
  int x1, y1, x2, y2;
};

class DinicFlow {
  typedef short flow_t;
  typedef int vertex_id_t;
  typedef short edge_id_t;        // within an adjacency list
  static const flow_t INF = std::numeric_limits<flow_t>::max();
  struct Edge { vertex_id_t b; edge_id_t opposite; flow_t cap, origcap; };

public:
  DinicFlow(vertex_id_t V) : V(V), adj(V), adjptr(V), level(V) { }

  void add_symmetric_edge(vertex_id_t a, vertex_id_t b, flow_t cap1, flow_t cap2=0) {
    edge_id_t a_id = adj[a].size();
    edge_id_t b_id = adj[b].size();
    adj[a].push_back((Edge){b, b_id, cap1, cap1});
    adj[b].push_back((Edge){a, a_id, cap2, cap2});
  }

  template<typename Result=flow_t>
  Result calcflow(vertex_id_t src, vertex_id_t sink) {
    Result total = 0;
    while (bfs(src, sink)) {
      flow_t aug;
      fill(adjptr.begin(), adjptr.end(), 0);
      while ((aug = dfs(src, sink, INF)) > 0) {
        total += aug;
      }
    }
    return total;
  }

private:
  bool bfs(vertex_id_t src, vertex_id_t sink) {
    bfsq.clear();
    fill(level.begin(), level.end(), -1);

    level[src] = 0;
    bfsq.push_back(src);

    while (!bfsq.empty()) {
      vertex_id_t a = bfsq.front(); bfsq.pop_front();
      if (a == sink) break;

      for (edge_id_t i=0; i<(edge_id_t)adj[a].size(); ++i) {
        const Edge &e = adj[a][i];
        if (e.cap != 0 && level[e.b] == -1) {
          level[e.b] = level[a] + 1;
          bfsq.push_back(e.b);
        }
      }
    }
    return level[sink] != -1;
  }

  flow_t dfs(vertex_id_t a, vertex_id_t sink, flow_t inflow) {
    if (a == sink) {
      return inflow;
    }

    for (edge_id_t &i=adjptr[a]; i<(edge_id_t)adj[a].size(); ++i) {
      Edge &e = adj[a][i];
      if (e.cap != 0 && level[e.b] == level[a]+1) {
        flow_t x = dfs(e.b, sink, min(inflow, e.cap));
        if (x > 0) {
          e.cap -= x;
          adj[e.b][e.opposite].cap += x;
          return x;
        }
      }
    }
    return 0;
  }

  int V;
  vector<vector<Edge> > adj;
  vector<edge_id_t> adjptr;
  vector<vertex_id_t> level;
  deque<vertex_id_t> bfsq;
};

int solve1() {
  int W, H, B;
  cin >> W >> H >> B;
  vector<Building> buildings(B);
  // map<int, int> ys;
  // ys.insert(make_pair(0, 0));
  // ys.insert(make_pair(H-1, 0));
  for (Building &b : buildings) {
    cin >> b.x1 >> b.y1 >> b.x2 >> b.y2;
    // ys.insert(make_pair(b.y1-1, 0));
    // ys.insert(make_pair(b.y1, 0));
    // ys.insert(make_pair(b.y2, 0));
    // ys.insert(make_pair(b.y2+1, 0));
  }
  // int ynext = 0;
  // for (auto& entry : ys) {
  //   if (entry.first >= 0 && entry.first < H) {
  //     entry.second = ynext++;
  //   }
  // }
  // for (Building &b : buildings) {
  //   b.y1 = ys[b.y1];
  //   b.y2 = ys[b.y2];
  // }
  // H = ynext;

  static char map[4006][1001];
  ZERO(map);
  assert(H <= 4005);
  for (int y=0; y<H; ++y) {
    memset(map[y], 1, W);
  }
  for (const Building &b : buildings) {
    for (int y=b.y1; y<=b.y2; ++y) {
      for (int x=b.x1; x<=b.x2; ++x) {
        map[y][x] = 0;
      }
    }
  }
  static pair<int, int> vxid[4005][1000];
  MINUSONE(vxid);
  int V = 0;
  int src = V++, sink = V++;
  for (int y=0; y<H; ++y) {
    for (int x=0; x<W; ++x) {
      if (map[y][x]) {
        vxid[y][x].first = V++;
        vxid[y][x].second = V++;
      }
    }
  }
  DinicFlow flow(V);
  for (int x=0; x<W; ++x) {
    if (map[0][x])   { flow.add_symmetric_edge(src, vxid[0][x].first, 1); }
    if (map[H-1][x]) { flow.add_symmetric_edge(vxid[H-1][x].second, sink, 1); }
  }
  for (int y=0; y<H; ++y) {
    for (int x=0; x<W; ++x) {
      if (map[y][x]) {
        flow.add_symmetric_edge(vxid[y][x].first, vxid[y][x].second, 1);
        if (map[y+1][x]) {
          flow.add_symmetric_edge(vxid[y][x].second, vxid[y+1][x].first, 1);
          flow.add_symmetric_edge(vxid[y+1][x].second, vxid[y][x].first, 1);
        }
        if (map[y][x+1]) {
          flow.add_symmetric_edge(vxid[y][x].second, vxid[y][x+1].first, 1);
          flow.add_symmetric_edge(vxid[y][x+1].second, vxid[y][x].first, 1);
        }
      }
    }
  }
  return flow.calcflow(src, sink);
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: %d\n", tt, solve1());
  }
}
