#include <climits>
#include <iostream>
#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

#define IN(x,s,g) ((x) >= (s) && (x) < (g))
#define ISIN(x,y,w,h) (IN((x),0,(w)) && IN((y),0,(h)))

struct Edge{
  int cap; // capacity
  int to;
  int rev; // reverse edge id

  Edge(){}
  Edge(int c, int t, int r) :
    cap(c), to(t), rev(r){}
};

template<class E> // Edge type
class Graph{
public:
typedef std::vector<std::vector<E> > G;

private:
G g;

public:
  Graph(int n) : g(G(n)) {}

  void addEdge(int from, int to, int cap){
    g[from].push_back(E(cap, to, g[to].size()));
    g[to].push_back(E(0, from, g[from].size() - 1));
  }

  void addEdge(int from, int to, int cap, int cost){
    g[from].push_back(E(cap, to, cost, g[to].size()));
    g[to].push_back(E(0, from, -cost, g[from].size() - 1));
  }

  G &getRowGraph(){
    return g;
  }
};

const int _dx[] = {0,1,0,-1};
const int _dy[] = {-1,0,1,0};

int bld[500][100];

int idx(int x, int y, int w, int h){
  return 2 * (y * w + x);
}

template<class E>
class Dinic{
  typedef typename Graph<E>::G G;
  G &g;
  std::size_t n; // size of graph

  std::vector<int> level;
  std::vector<int> iter;

  // other utilities

  // search length of shortest path from s
  void bfs(int s){
    std::queue<int> que;
    level = std::vector<int>(n, -1);

    level[s] = 0;
    que.push(s);

    while(!que.empty()){
      int v = que.front(); que.pop();
      for(int i = 0; i < (int)g[v].size(); i++){
	E &e = g[v][i];
	if(e.cap > 0 && level[e.to] < 0){
	  level[e.to] = level[v] + 1;
	  que.push(e.to);
	}
      }
    }
  }

  // search path
  int dfs(int v, int t, int f){
    if(v == t) return f;
    for(int &i = iter[v]; i < (int)g[v].size(); i++){
      E &e = g[v][i];
      if(e.cap > 0 && level[v] < level[e.to]){
	int d = dfs(e.to, t, min(f, e.cap));
	if(d > 0){
	  e.cap -= d;
	  g[e.to][e.rev].cap += d;
	  return d;
	}
      }
    }
    return 0;
  }

public:
  Dinic(Graph<E> &graph) : g(graph.getRowGraph()){
    n = g.size();
  }

  // Max flow of the flow from s to t.
  int solve(int s, int t){
    int flow = 0;
    while(true){
      int f;
      bfs(s);
      if(level[t] < 0) return flow;
      iter  = std::vector<int>(n, 0);
      while((f = dfs(s, t, INT_MAX)) > 0){
	flow += f;
      }
    }
  }
};

template<class E>
int dinic(Graph<E> &g, int s, int d){
  return Dinic<E>(g).solve(s, d);
}

int main(){
  const int T = getInt();
  REP(cc, T){
    const int w = getInt();
    const int h = getInt();
    const int b = getInt();

    REP(i,h) REP(j,w) bld[i][j] = 0;

    REP(_,b){
      const int x0 = getInt();
      const int y0 = getInt();
      const int x1 = getInt();
      const int y1 = getInt();
      for(int i = y0; i <= y1; i++)
	for(int j = x0; j <= x1; j++)
	  bld[i][j] = 1;
    }

    Graph<Edge> g(2 * h * w + 2);
    const int from = 2 * h * w;
    const int to = 2 * h * w + 1;

    REP(y,h) REP(x,w){
      if(bld[y][x] == 0)
	g.addEdge(idx(x, y, w, h), idx(x, y, w, h) + 1, 1);

      REP(d,4){
	const int xx = x + _dx[d];
	const int yy = y + _dy[d];

	if(ISIN(xx, yy, w, h)){
	  g.addEdge(idx(x, y, w, h) + 1, idx(xx, yy, w, h), 1);
	}
      }
    }

    REP(i,w){
      g.addEdge(from, idx(i, 0, w, h), 1);
      g.addEdge(idx(i, h - 1, w, h) + 1, to, 1);
    }

    const int ans = dinic(g, from, to);
    printf("case #%d: %d\n", cc + 1, ans);
  }

  return 0;
}
