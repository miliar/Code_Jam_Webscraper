/** Dinic's from http://stanford.edu/~liszt90/acm/notebook.html#file1
used in ICPC 2015 by Team UNSW. **/

#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <cstring>

#define D(x...) fprintf(stderr, x)
#define D(x...)

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
    D("addedge from %d->%d [cap=%d]\n",from,to,cap);
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

const int MAX_WORDS = 4005;

int N;
map<string,int> words;
bool defEng[MAX_WORDS];
bool defFrench[MAX_WORDS];
char buf[100005];
vector<int> here[MAX_WORDS];

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        N = 0;
        words.clear();
        for(int i=0;i<MAX_WORDS;i++) {
            defEng[i] = false;
            defFrench[i] = false;
            here[i].clear();
        }

        int L;
        scanf(" %d ",&L);

        for(int i=0;i<L;i++) {
            gets(buf);
            char *ptr = strtok(buf, " ");
            while(ptr != NULL) {
                string s = string(ptr);
               // D("s = %s\n",s.c_str());

                if(words.find(s) == words.end()) {
                    words[s] = N;
                    N++;
                }

                if(i == 0) {
                    defEng[words[s]] = true;
                }

                if(i == 1) {
                    defFrench[words[s]] = true;
                }
                here[i].push_back(words[s]);
                D("sz = %d\n",here[i].size());

                ptr = strtok(NULL, " ");
            }
        }
        D("N = %d\n",N);

        Dinic din = Dinic(2*(N+1));

        int source = (2*N);
        int sink = (2*N)+1;

        long long ans = 0;
        for(int i=0;i<N;i++) {
            if(!defEng[i] || !defFrench[i]) {
                din.AddEdge(i, i+N, 1);
            } else {
                ans++;
            }

            if(defEng[i]) {
                din.AddEdge(source, i, INF);
            }
            
            if(defFrench[i]) {
                din.AddEdge(i+N, sink, INF);
            }
        }

        for(int i=0;i<L;i++) {
            for(int j=0;j<here[i].size();j++) {
                int jj = here[i][j];
                for(int k=0;k<j;k++) {
                    int kk = here[i][k];
                    din.AddEdge(jj+N, kk, INF);
                    din.AddEdge(kk+N, jj, INF);
                }
            }
        }

        ans += din.GetMaxFlow(source, sink);
        D("mf = %lld\n",ans);
        printf("Case #%d: %lld\n",z,ans);
    }

    return 0;
}
