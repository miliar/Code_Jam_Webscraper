// MAKSYMALNY PRZEPLYW O(V^3) (algorytm Push-Relabel)
// Adam Polak
#include <queue>
#include <cassert>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 4*2000*1000+2;

#define REP(i,n) for (int i=0;i<n;++i)

struct Edge {
    int v,cap,flow;
    int back_ind;
    Edge *back;
    Edge(int vi, int ci):v(vi),cap(ci){}
};

/* Usage:
   1) n=...; s=...; t=...;
   2) REP(i,n) g[i].clear();
   3) add_edge(...);
   4) compute_flow();
*/

int n,s,t;
int e[N],h[N];
vector<Edge> g[N];
vector<Edge>::iterator cur[N];

#define FOREACH(i, C) for (auto i=(C).begin(); i!=(C).end(); ++i)

void bfs(int start, int start_h) {
    queue<int> q;
    h[start] = start_h;
    for(q.push(start);!q.empty();q.pop()) {
        int u = q.front();
        for (Edge& i : g[u]) {
            if (i.back->flow < i.back->cap && h[i.v]>h[u]+1) {
                    h[i.v] = h[u] + 1;
                    q.push(i.v);
            }
        }
    }
}

int compute_flow() {
    queue<int> q;
    for (int i=0;i<n;++i) {
        FOREACH(j,g[i]) {
            j->flow = 0;
            j->back = &g[j->v][j->back_ind];
        }
        cur[i] = g[i].begin();
        h[i] = e[i] = 0;
    }
    FOREACH(i,g[s]) {
        i->flow = i->cap;
        i->back->flow = -i->flow;
        if (e[i->v]==0 && i->v!=t) q.push(i->v);
        e[i->v] += i->flow;
    }
    h[s] = n;
    int relabel_counter = 0;
    for(;!q.empty();q.pop()) {
        int u = q.front();
        while (e[u]>0) {
            if (cur[u]==g[u].end()) { // relabel
                relabel_counter++;
                h[u] = 2*n+1;
                FOREACH(i,g[u]) if(i->flow < i->cap) h[u]=min(h[u],1+h[i->v]);
                cur[u] = g[u].begin(); 
                continue; 
            }
            if (cur[u]->flow < cur[u]->cap && h[u]==h[cur[u]->v]+1) { // push
                int d = min(e[u], cur[u]->cap - cur[u]->flow);
                cur[u]->flow += d;
                cur[u]->back->flow -= d;
                e[u] -= d;
                e[cur[u]->v] += d;
                if (e[cur[u]->v]==d && cur[u]->v!=t && cur[u]->v!=s) q.push(cur[u]->v);
            } else cur[u]++; 
        }
        if (relabel_counter >= n) { 
            REP(i,n) h[i]=2*n+1;
            bfs(t,0);
            bfs(s,n);
            relabel_counter = 0;
        }
    }
    return e[t];
}

void add_edge(int a, int b, int c, int c_back=0) {
    assert(a != b);  // NIE wrzucac petelek!
    g[a].push_back(Edge(b,c));
    g[b].push_back(Edge(a,c_back));
    g[a].back().back_ind = g[b].size()-1;
    g[b].back().back_ind = g[a].size()-1;
    //cerr << a << " " << b << " " << c << endl;
}

int main() {
  int T;
  cin >> T;
  for (int ttt=1; ttt<=T; ++ttt) {
    int w, h, b;
    cin >> w >> h >> b;
    vector<int> X1(b),X2(b),Y1(b),Y2(b),Ys(b*2);
    for (int i=0;i<b;++i) {
      cin >> X1[i] >> Y1[i] >> X2[i] >> Y2[i];
      
      Ys[2*i] = Y1[i];
      Ys[2*i+1]=Y2[i];
    }

/*
    sort(Ys.begin(), Ys.end());
    Ys.erase(unique(Ys.begin(), Ys.end()), Ys.end());
    for (int i=0;i<b;++i)  {
    //  Y1[i] = lower_bound(Ys.begin(),Ys.end(),Y1[i])-Ys.begin();
      //Y2[i] = lower_bound(Ys.begin(),Ys.end(),Y2[i])-Ys.begin();
    }

    //h = Ys.size();
*/

    vector<vector<bool>> grid(w, vector<bool>(h, true));

    for (int i=0; i<b; ++i) 
      for (int x=X1[i];x<=X2[i];++x)
        for (int y=Y1[i];y<=Y2[i];++y)
          grid[x][y] = false;
    n = 2 * w * h + 2;
    s = n - 2;
    t = n - 1;
    REP(i,n) g[i].clear();
    for (int i=0;i<w;++i)
      for (int j=0; j<h; ++j) 
        if (grid[i][j]) {
          add_edge((i*h+j)*2,(i*h+j)*2+1,1);
          if (i>0 && grid[i-1][j]) 
            add_edge((i*h+j)*2+1,(i*h+j-h)*2,1);
          if (i<w-1 && grid[i+1][j]) 
            add_edge((i*h+j)*2+1,(i*h+j+h)*2,1);
          if (j>0 && grid[i][j-1]) 
            add_edge((i*h+j)*2+1,(i*h+j-1)*2,1);
          if (j<h-1 && grid[i][j+1]) 
            add_edge((i*h+j)*2+1,(i*h+j+1)*2,1);
        }
    for (int i=0; i<w; ++i) {
      if (grid[i][0])
        add_edge(s, i*h*2,1);
      if (grid[i][h-1])
        add_edge((i*h+h-1)*2+1,t,1);
    }
    int FLOW = compute_flow();
    cout << "Case #" << ttt << ": " << FLOW << endl;
  }

}
