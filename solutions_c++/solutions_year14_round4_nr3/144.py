#include <algorithm>
#include <array>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <forward_list>
#include <functional>
#include <initializer_list>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <regex>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>
#include <cassert>
using namespace std;

#define FOR(it,L) for(auto it=(L).begin(); it!=(L).end(); ++it)
#define FORR(it,L) for(auto it=(L).rbegin(); it!=(L).rend(); ++it)
#define FORI(i,n) for(int i=0; i<(int)(n); ++i)
#define FORIB(i,b,n) for(int i=(int)(b); i<(int)(n); ++i)
#define FORIR(i,n) for(int i=(int)((n)-1); i>=0; --i)
#define FORIBR(i,b,n) for(int i=(int)((n)-1); i>=(int)(b); --i)
#define MP(a,b) make_pair(a,b)
#define MT(a...) make_tuple(a)
#define ALL(L) (L).begin(),(L).end()
#define ALLR(L) (L).rbegin(),(L).rend()
#define SZ(L) (L).size()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define SORTED_PAIR(a,b) MIN(a,b),MAX(a,b)
#define INF (1<<29)
#define EPS (1e-9)

struct Edge {
  uint u, v;
  int c;
  Edge(uint u, uint v, int c = 1) : u(u), v(v), c(c) {}
  bool operator<(const Edge& rhs) {
    return c < rhs.c;
  }
};

typedef unsigned int uint;
typedef unsigned long long ull;
typedef signed long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef pair<int,int> pii;
typedef vector<pii> vii;

typedef vector<list<Edge> > Graph;
typedef list<uint> Path;
typedef vector<pair<int, int> > SPResult;
typedef vector<Edge*> EdgeList;
typedef vector<vector<bool> > AdjacencyMatrix;
typedef vector<vector<int> > WeightedAdjacencyMatrix;

void addUdEdge(Graph& g, uint u, uint v, int c = 1) {
  g[u].push_back(Edge(u, v, c));
  g[v].push_back(Edge(v, u, c));
}

void addEdge(Graph& g, uint u, uint v, int c = 1) {
  g[u].push_back(Edge(u, v, c));
}

void Dijkstra_stl(const Graph& g, uint s, SPResult& dists) {
  uint n = g.size();
  typedef pair<uint, uint> puu;
  priority_queue<puu, vector<puu>, std::greater<puu> > q;
  dists = SPResult(n, MP(INF, -1));
  vector<bool> opened(n, true);
  q.push(MP(0, s));
  dists[s] = MP(0, -1);
  while (!q.empty()) {
    uint u = q.top().second;
    q.pop();
    if (opened[u]) {
      opened[u] = false;
      FOR(it, g[u])
        if (dists[u].first + it->c < dists[it->v].first) {
          dists[it->v].first = dists[u].first + it->c;
          dists[it->v].second = u;
          q.push(MP(dists[u].first + it->c, it->v));
        }
    }
  }
}

struct Buld {
	int x0, y0, x1, y1;
};

int dist(Buld b1, Buld b2) {
	int dx, dy;
	if(b1.x0 <= b2.x0) {
		dx = b2.x0 - b1.x1;
	} else {
		dx = b1.x0 - b2.x1;
	}
	if(b1.y0 <= b2.y0) {
		dy = b2.y0 - b1.y1;
	} else {
		dy = b1.y0 - b2.y1;
	}
	assert(dx > 0 || dy > 0);
	return max(dx, dy) - 1;
}

void calc(int T) {
  int W, H, B;
  cin >> W >> H >> B;
  
  Graph g(B + 2);
  
  vector<Buld> bs;
  FORI(i, B) {
	Buld b;
	cin >> b.x0 >> b.y0 >> b.x1 >> b.y1;
	bs.push_back(b);
	addUdEdge(g, i, B, bs[i].x0);
	addUdEdge(g, i, B + 1, W - bs[i].x1 - 1);
  }
  addUdEdge(g, B, B + 1, W);
  
  FORI(i, B) {
	FORI(j, B) {
		if(i == j) continue;
		addUdEdge(g, i, j, dist(bs[i], bs[j]));
	}
  }
  
  SPResult res;
  Dijkstra_stl(g, B, res);
  int dist = res[B + 1].first;
  assert(dist <= W);
  
  printf("Case #%d: %d\n", T + 1, dist);
}

int main() {
  int T;
  cin >> T;
  FORI(t, T) calc(t);
}
