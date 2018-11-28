#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
  assert(scanf("%d", &CASES) == 1);
}

int print(const char *err, ...) {
  va_list pvar;
  va_start(pvar, err);
  vfprintf(stderr, err, pvar);
  return vfprintf(stdout, err, pvar);
}

int dprint(const char *err, ...) { 
  if (debug) {
    va_list pvar;
    va_start(pvar, err);
    return vfprintf(stderr, err, pvar);
  }
  return 0;
}

struct rect {
	int x0, y0, x1, y1;
};

typedef int Flow;

struct flow_edge {
  int dest, back;// back is index of back-edge in graph[dest]
  Flow c, f; // capacity and flow
  Flow r() { return c - f; } // used by ford fulkerson
  flow_edge() {}
  flow_edge(int _dest, int _back, Flow _c, Flow _f = 0)
    : dest(_dest), back(_back), c(_c), f(_f) { }
};

typedef vector<flow_edge> adj_list;
typedef adj_list::iterator adj_iter;

void flow_add_edge(adj_list *g, int s, int t, // add s -> t
		   Flow c, Flow back_c = 0) {
	//	printf("%d -> %d cap %d\n", s, t, c);
	assert(c == 1 && back_c == 0);
	g[s].push_back(flow_edge(t, g[t].size(), c));
	g[t].push_back(flow_edge(s, g[s].size() - 1, back_c));
}

#define MAXNODES 2050*1050*2

int mark[MAXNODES];
adj_list G[MAXNODES];

bool inc_flow_dfs(adj_list *g, int s, int t) {
	if (s == t) return true;
  //  printf("inc flow %d\n", s);
  mark[s] = 1;
  for (adj_iter it = g[s].begin(); it != g[s].end(); ++it)
	  if (!mark[it->dest] && it->r() > 0 && inc_flow_dfs(g, it->dest, t)) {
		  ++it->f;
		  --g[it->dest][it->back].f;
		  return true;
	  }
  return 0;
}

Flow max_flow(adj_list *graph, int n, int s, int t) {
	Flow flow = 0, inc = 0;
	do flow += inc, memset(mark, 0, sizeof(int)*n);
	while ((inc = inc_flow_dfs(graph, s, t)));
	return flow;
}


const int dx[] = {0, -1, 1, 0};
const int dy[] = {1, 0, 0, -1};
int grid[2500][1500];
int W, H;

int enc(int x, int y) {
	return 2*(y*W+x);
}

bool ok(int x, int y) {
	return x >= 0 && x < W && y >= 0 && y < H && !grid[y][x];
}


void solve(int P) {
	int B;
	scanf("%d%d%d", &W, &H, &B);
	rect b[2000];
	vi yc;
	for (int i = 0;i < B; ++i) {
		scanf("%d%d%d%d", &b[i].x0, &b[i].y0, &b[i].x1, &b[i].y1);
		b[i].x1++;
		b[i].y1++;
		assert(b[i].x0 < b[i].x1);
		assert(b[i].y0 < b[i].y1);
		//		yc.push_back(b[i].y0);
		//		yc.push_back(b[i].y1+1);
	}
	/*
	yc.push_back(0);
	yc.push_back(H);
	sort(yc.begin(), yc.end());
	yc.resize(unique(yc.begin(), yc.end())-yc.begin());
	map<int, int> yinv;
	for (int i = 0; i < yc.size(); ++i)
		yinv[yc[i]] = i;
	H = yc.size()-1;
	*/

	memset(grid, 0, sizeof(grid));
	for (int i = 0; i < B; ++i) {
		//		b[i].y0 = yinv[b[i].y0];
		//		b[i].y1 = yinv[b[i].y1+1];
		//		printf("box: [%d,%d] x [%d,%d]\n", b[i].x0, b[i].y0, b[i].x1, b[i].y1);
		for (int y = b[i].y0; y < b[i].y1; ++y) {
			for (int x = b[i].x0; x < b[i].x1; ++x) {
				grid[y][x] = 1;
			}
		}
	}
	/*
	for (int y = 0; y < H; ++y) {
		for (int x = 0; x < W; ++x) 
			printf("%c", grid[y][x] ? '#' : '.');
		printf("\n");
	}
	*/
	int V = 2*W*H+2;
	for (int i =0; i < V; ++i) G[i].clear();
	assert(V <= MAXNODES);
	int s = V-2, t = V-1;
	for (int i = 0; i < W; ++i) {
		if (ok(i, 0))
			flow_add_edge(G, s, enc(i, 0), 1);
		if (ok(i, H-1))
			flow_add_edge(G, enc(i, H-1)+1, t, 1);
	}
	//	printf("add cross\n");
	for (int y = 0; y < H; ++y)
		for (int x = 0; x < W; ++x) {
			if (!ok(x, y)) continue;
			flow_add_edge(G, enc(x,y), enc(x,y)+1, 1);
			for (int d = 0; d < 4; ++d) {
				int nx = x + dx[d], ny = y + dy[d];
				if (ok(nx, ny))
					flow_add_edge(G, enc(x, y)+1, enc(nx, ny), 1);
			}
		}
	int flow = max_flow(G, V, s, t);
	print("Case #%d: %d\n", P, flow);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
