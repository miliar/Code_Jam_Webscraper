#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

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
  
  void add_edge_directed(int u, int v, int cap, int flow,bool is_real,pair<int,int> part) {
    Edge e = {v,cap,flow,is_real,part};    nbr[u].push_back(e);
  }
};

// Use this instead of G.add_edge_directed in your actual program
void add_edge_with_capacity_directed(Graph& G,int u,int v,int cap){
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


const int MAX_N = 530;
bool A[MAX_N][MAX_N];

int W,H;

int in(int i,int j){ int x = i*(W+1)+j;  return 2*x; }
int out(int i,int j){ int x = i*(W+1)+j; return 2*x+1; }

const int di[] = {-1,1,0,0};
const int dj[] = {0,0,1,-1};

int do_case(){
  int B;
  cin >> W >> H >> B;

  for(int i=0;i<=H;i++)
    for(int j=0;j<=W;j++)
      A[i][j] = true;

  Graph G(2*(W+2)*(H+2)+100);
  
  int x0,x1,y0,y1;
  for(int i=0;i<B;i++){
    cin >> x0 >> y0 >> x1 >> y1;
    for(int j=y0;j<=y1;j++)
      for(int k=x0;k<=x1;k++)
	A[j][k] = false;
  }
  
  for(int i=0;i<H;i++)
    for(int j=0;j<W;j++)
      for(int k=0;k<4;k++){
	int nI = i+di[k],nJ = j+dj[k];
	if(!(0 <= nI && nI < H && 0 <= nJ && nJ < W)) continue;
	add_edge_with_capacity_directed(G,out(i,j),in(nI,nJ),1);
      }

  for(int i=0;i<H;i++)
    for(int j=0;j<W;j++)
      if(A[i][j])
	add_edge_with_capacity_directed(G,in(i,j),out(i,j),1);

  int s = in(H,W), t = out(H,W);
  
  for(int i=0;i<W;i++)
    add_edge_with_capacity_directed(G,s,in(0,i),1);
  
  for(int i=0;i<W;i++)
    add_edge_with_capacity_directed(G,out(H-1,i),t,1);

  return network_flow(G,s,t);
}

int main(){
  int T,C=1;
  cin >> T;
  while(T--)
    cout << "Case #" << C++ << ": " << do_case() << endl;
  return 0;
}
