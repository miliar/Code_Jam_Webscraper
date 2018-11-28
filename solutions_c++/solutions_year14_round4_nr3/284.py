#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<set>
#include<string.h>
using namespace std;


// Adjacency list implementation of Dinic's blocking flow algorithm.
// This is very fast in practice, and only loses to push-relabel flow.
//
// Running time:
//     O(|V|^2 |E|)
//
// INPUT:
//     - graph, constructed using AddEdge()
//     - source
//     - sink
//
// OUTPUT:
//     - maximum flow value
//     - To obtain the actual flow values, look at all edges with
//       capacity > 0 (zero capacity edges are residual edges).


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
};
int river[110][510];
int hasWater[110];
void solve(){
    memset(river,0,sizeof(river));
    int w,h,b;
    scanf("%d %d %d",&w,&h,&b);
    for(int i = 0 ; i < b ; ++ i ){
        int x1,y1,x2,y2;
        scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
        for(int x =x1;x<=x2;++x)
            for(int y=y1;y<=y2;++y)
                river[x][y]=1;
    }

    Dinic G(w*h*2+2);
    for(int i = 1 ; i <= w ; ++i){
        if(river[i-1][0]==0)
            G.AddEdge(0,i,1);
    }
    for(int x=0;x<w;++x){
        for(int y=0;y<h;++y){
            if(river[x][y]==0){
                G.AddEdge(w*y+x+1,w*y+x+1+w,1);
                if(x&&river[x-1][y]==0){
                    G.AddEdge(w*y+x+1+w,w*y+x,1);
                }
                if(x+1<w&&river[x+1][y]==0){
                    G.AddEdge(w*y+x+1+w,w*y+x+2,1);
                }
                if(y+1<h&&river[x][y+1]==0){
                    G.AddEdge(w*y+x+1+w,w*(y+1)+x+1,1);
                }
                else if(y+1==h){
                    G.AddEdge(w*y+x+1+w,w*h*2+1,1);
                }
            }
        }
    }
    printf("%d\n",G.GetMaxFlow(0,w*h*2+1));

}

int main(){
    freopen("C-small-attempt1"".in","r",stdin);
    freopen("C-small-attempt1"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
