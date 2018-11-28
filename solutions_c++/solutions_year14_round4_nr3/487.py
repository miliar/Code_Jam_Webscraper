using namespace std;

#include "iostream"
#include <cmath>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

const int INF = 2000000000;

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct Dinic {
  int N;
  vector<vector<Edge> > G;
  vector<Edge *> dad;
  vector<int> Q;
  
  Dinic(int N) : N(N), G(N), dad(N), Q(N) {}
  
  void AddEdge(int from, int to, int cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  long long BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), (Edge *) NULL);
    dad[s] = &G[0][0] - 1;
    
    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < G[x].size(); i++) {
  Edge &e = G[x][i];
  if (!dad[e.to] && e.cap - e.flow > 0) {
    dad[e.to] = &G[x][i];
    Q[tail++] = e.to;
  }
      }
    }
    if (!dad[t]) return 0;

    long long totflow = 0;
    for (int i = 0; i < G[t].size(); i++) {
      Edge *start = &G[G[t][i].to][G[t][i].index];
      int amt = INF;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
  if (!e) { amt = 0; break; }
  amt = min(amt, e->cap - e->flow);
      }
      if (amt == 0) continue;
      for (Edge *e = start; amt && e != dad[s]; e = dad[e->from]) {
  e->flow += amt;
  G[e->to][e->index].flow -= amt;
      }
      totflow += amt;
    }
    return totflow;
  }

  long long GetMaxFlow(int s, int t) {
    long long totflow = 0;
    while (long long flow = BlockingFlow(s, t))
      totflow += flow;
    return totflow;
  }
} *G;

bool a[ 102 ][ 505 ];

inline int in(int vertex) { return 2 * vertex; }
inline int out(int vertex) { return 2 * vertex + 1; }

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int main(int argc, char const *argv[])
{
  int T;

  cin >> T;
  for (int tc = 1; tc <= T; tc++)
  {
    int W, H, B;
    cin >> W >> H >> B;

    for (int i = 0; i < W; i++) for (int j = 0; j < H; j++) a[i][j] = true;
    for (int i = 0; i < B; i++)
    {
      int x0, y0, x1, y1;
      cin >> x0 >> y0 >> x1 >> y1;

      for (int x = x0; x <= x1; x++)
        for (int y = y0; y <= y1; y++)
          a[x][y] = false;
    }

    int N = W * H;
    G = new Dinic( 2 * (N + 2) );

    for (int x = 0; x < W; x++)
      for (int y = 0; y < H; y++)
      {
        int v = x * H + y + 1;
        G->AddEdge( in(v), out(v), 1 );

        if ( a[x][y] == false ) continue;

        for (int k = 0; k < 4; k++)
        {
          int xx = x + dx[ k ];
          int yy = y + dy[ k ];

          if ( xx >= 0 && xx < W && yy >= 0 && yy < H )
          {
            if ( a[xx][yy] == false ) continue;

            int w = xx * H + yy + 1;
            G->AddEdge( out(v), in(w), 1 );
          }
        }
      }

    for (int x = 0; x < W; x++)
    {
      int v = x * H + 1;
      if ( a[x][0] == true ) G->AddEdge( out(0), in(v), 1 );

      v = x * H + H;
      if ( a[x][H - 1] == true ) G->AddEdge( out(v), in(N + 1), 1 );
    }

    cout << "Case #" << tc << ": " << (G->GetMaxFlow( out(0), in(N + 1) )) << endl;

    delete G;
  }

  return 0;
}