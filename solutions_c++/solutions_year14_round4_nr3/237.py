#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
// Network Flow (Directed and Undirected) -- O(fm) where f = max flow
// To recover flow on an edge, it's in the flow field provided is_real == true.
// Note: if you have an undirected network. simply call add_edge twice
// with an edge in both directions (same capacity).  Note that 4 edges
// will be added (2 real edges and 2 residual edges).  To discover the
// actual flow between two vertices u and v, add up the flow of all
// real edges from u to v and subtract all the flow of real edges from
// v to u.

struct Edge;
typedef vector<Edge>::iterator EdgeIter;

struct Edge {
  int to, cap, flow;
  bool is_real;
  pair<int,int> part;
  EdgeIter partner;
  
  int residual() const { return cap - flow; }
};

struct Graph {
  vector<vector<Edge> > nbr;
  int num_nodes;
  Graph(int n) : nbr(n), num_nodes(n) { }
  
  // No check for duplicate edges!
  // Add (or remove) any parameters that matter for your problem
  void add_edge_directed(int u, int v, int cap, int flow, bool is_real,
			 pair<int,int> part) {
    Edge e = {v, cap, flow, is_real, part};    nbr[u].push_back(e);
  }
};

// Use this instead of G.add_edge_directed in your actual program
void add_edge(Graph& G,int u,int v,int cap){
  int U = G.nbr[u].size(), V = G.nbr[v].size();
  G.add_edge_directed(u,v,cap,0,true ,make_pair(v,V));
  G.add_edge_directed(v,u,0  ,0,false,make_pair(u,U));
}

void push_path(Graph& G, int s, int t, const vector<EdgeIter>& path, int flow) {
  for (int i = 0; s != t; s = path[i++]->to)
    if (path[i]->is_real) {
      path[i]->flow += flow;    path[i]->partner->cap += flow;
    } else {
      path[i]->cap -= flow;     path[i]->partner->flow -= flow;
    }
}

int augmenting_path(Graph& G, int s, int t, vector<EdgeIter>& path,
                    vector<bool>& visited, int step = 0) {
  if (s == t) return -1;  visited[s] = true;
  for (EdgeIter it = G.nbr[s].begin(); it != G.nbr[s].end(); ++it) {
    int v = it->to;
    if (it->residual() > 0 && !visited[v]) {
      path[step] = it;
      int flow = augmenting_path(G, v, t, path, visited, step+1);
      if (flow == -1)    return it->residual();
      else if (flow > 0) return min(flow, it->residual());
    }
  }
  return 0;
}

int network_flow(Graph& G, int s, int t) { // note that the graph is modified
  for(int i=0;i<G.num_nodes;i++)
    for(EdgeIter it=G.nbr[i].begin(); it != G.nbr[i].end(); ++it)
      G.nbr[it->part.first][it->part.second].partner = it;
  
  vector<EdgeIter> path(G.num_nodes);
  int flow = 0, f;
  do {
    vector<bool> visited(G.num_nodes, false);
    if ((f = augmenting_path(G, s, t, path, visited)) > 0) {
      push_path(G, s, t, path, f);    flow += f;
    }
  } while (f > 0);
  return flow;
}

int W, H, B;
const int IN = 0, OUT = 1;

int ind(int x, int y, int dir)
{
  return 2*(y * W + x) + dir;
}

void solve()
{
  cin >> W >> H >> B;

  bool R[100][500] = {false};
  for (int i = 0; i < B; i++) {
    int x0, y0, x1, y1;
    cin >> x0 >> y0 >> x1 >> y1;

    for (int x = x0; x <= x1; x++) {
      for (int y = y0; y <= y1; y++) {
	R[x][y] = true;
      }
    }
  }

  Graph G(2*H*W+2);

  int src = 2*H*W, sink = 2*H*W+1;
  int dx[] = {-1, 0, 1, 0};
  int dy[] = {0, -1, 0, 1};

  // connect src to bottom row, and top row to sink
  for (int x = 0; x < W; x++) {
    if (!R[x][0]) {
      add_edge(G, src, ind(x, 0, IN), 1);
    }
    if (!R[x][H-1]) {
      add_edge(G, ind(x, H-1, OUT), sink, 1);
    }
  }

  for (int x = 0; x < W; x++) {
    for (int y = 0; y < H; y++) {
      if (R[x][y]) continue;
      add_edge(G, ind(x, y, IN), ind(x, y, OUT), 1);
      for (int d = 0; d < 4; d++) {
	int x2 = x + dx[d], y2 = y + dy[d];
	if (!(0 <= x2 && x2 < W && 0 <= y2 && y2 < H)) continue;
	if (R[x2][y2]) continue;
	add_edge(G, ind(x,y,OUT), ind(x2,y2,IN), 1);
      }
    }
  }

  cout << network_flow(G, src, sink) << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }

  return 0;
}
