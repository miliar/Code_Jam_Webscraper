#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef int flow_type;
const flow_type inf_flow = 1234567890;
const int inf = inf_flow;

struct Edge {
    int to;
    flow_type cap, flow;
    Edge *rev;
    Edge(int to_, flow_type cap_, flow_type flow_): to(to_), cap(cap_), flow(flow_), rev(NULL) {}
};
    
struct FlowNetwork {
    vector< vector<Edge*> > adj;
    ~FlowNetwork() { for (int i=0; i<(int)adj.size(); ++i) for (int j=0; j<(int)adj[i].size(); ++j) delete adj[i][j]; }
    
    int add_source() {
        source = add_node();
        return source;
    }
    int add_sink() {
        sink = add_node();
        return sink;
    }
    
    int add_node() {
        adj.push_back(vector<Edge*>());
        return int(adj.size()) - 1;
    }
    void add_edge(int from, int to, flow_type cap) {
        Edge *u = new Edge(to, cap, 0);
        Edge *v = new Edge(from, 0, 0);
        u->rev = v;
        v->rev = u;
        adj[from].push_back(u);
        adj[to].push_back(v);
    }
    
    flow_type max_flow();
    
    private:
    int source, sink;
    bool can_augment(vector<Edge *> &);
};

bool FlowNetwork::can_augment(vector<Edge *> &P) {
    queue<int> Q;
    for (int i=0; i<(int)P.size(); ++i) {
        P[i] = NULL;
    }
    Q.push(source);
    
    while (!Q.empty()) {
        int x = Q.front();
        Q.pop();
        
        for (int i=0; i<(int)adj[x].size(); ++i) {
            Edge *e = adj[x][i];
            if (e->cap-e->flow>0 && P[e->to]==NULL) {
                P[e->to] = e;
                if (e->to == sink) {
                    return true;
                }
                Q.push(e->to);
            }
        }
    }
    
    return false;
}
flow_type FlowNetwork::max_flow() {
    flow_type ret = 0;
    vector<Edge*> P(adj.size());
    while (can_augment(P)) {
        flow_type flow = inf_flow;
        for (int upd=0; upd<2; ++upd) {
            int t = sink;
            while (t != source) {
                Edge *e = P[t];
                assert(e->to == t);
                if (!upd) {
                    flow = min(flow, e->cap - e->flow);
                } else {
                    e->flow += flow;
                    e->rev->flow -= flow;
                }
                t = e->rev->to;
            }
        }
        ret += flow;
    }

    return ret;
}


const int MAXN = 105;
const int MAXM = 505;
bool dead[MAXM][MAXN];
int I[MAXM][MAXN];
int O[MAXM][MAXN];
int solve() {
    int n, m, B;
    cin >> n >> m >> B;
    memset(dead, 0, sizeof dead);
    for (int k=0; k<B; ++k) {
        int j0, i0, j1, i1;
        cin >> j0 >> i0 >> j1 >> i1;
        for (int i=i0; i<=i1; ++i) {
            for (int j=j0; j<=j1; ++j) {
                dead[i][j] = 1;
            }
        }
    }
    /*
    for (int i=0; i<m; ++i) {
        for (int j=0; j<n; ++j) {
            cerr << dead[i][j];
        }
        cerr << '\n';
    }
    cerr << '\n' << '\n';
    */
    FlowNetwork F;
    int source = F.add_source();
    int sink = F.add_sink();
    for (int i=0; i<m; ++i) {
        for (int j=0; j<n; ++j) {
            if (dead[i][j]) continue;
            I[i][j] = F.add_node();
            O[i][j] = F.add_node();
            F.add_edge(I[i][j], O[i][j], 1);
            if (i == 0) {
                F.add_edge(source, I[i][j], 1);
            }
            if (i+1 == m) {
                F.add_edge(O[i][j], sink, 1);
            }
        }
    }
    for (int i=0; i<m; ++i) {
        for (int j=0; j<n; ++j) {
            if (dead[i][j]) continue;
            for (int di=-1; di<=1; ++di) {
                for (int dj=-1; dj<=1; ++dj) {
                    if (di!=0 && dj!=0) continue;
                    if (di==0 && dj==0) continue;
                    int r = i + di;
                    int c = j + dj;
                    if (r<0 || c<0 || r>=m || c>=n || dead[r][c]) continue;
                    F.add_edge(O[i][j], I[r][c], 1);
                }
            }
        }
    }

    return F.max_flow();
}

int main() {
    int T;
    cin >> T;
    cerr << T << " cases total\n";
    for (int t=1; t<=T; ++t) {
        int sol = solve();
        cout << "Case #" << t << ": " << sol << '\n';
        cerr << "Case #" << t << ": " << sol << '\n';
    }
	return 0;
}
