#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define num(i,N) for(int i=0; i < (N); ++i)
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#if __cplusplus > 199711L
#define tr(c,i) for(auto i=(c).begin(); i != (c).end(); ++i)
#else
#define tr(c,i) for(typeof((c).begin()) i=(c).begin(); i != (c).end(); ++i)
#endif
#define has(c,x) ((c).find(x) != (c).end())

// Cut begin
#define DEBUG(x) cout<<"#"<<__LINE__<<": "<<#x<<" = "<<x<<endl;
template <class T> ostream& operator<<(ostream &out, const vector<T> &v) {
    out<<"["; num(i,sz(v)) out<<(i?", ":"")<<v[i]; return out << "]"; }
template <class T, class K> ostream& operator<<(ostream &out, const map<K,T> &m) {
    out<<"{"; tr(m,it) out<<(it==m.begin()?"":", ")<<it->first<<":"<<it->second;
    return out << "}"; }
template <class T> ostream& operator<<(ostream &out, const set<T> &s) {
    out<<"{"; tr(s,it) out<<(it==s.begin()?"":", ")<<*it; return out<<"}"; }
template <class T, class K> ostream& operator<<(ostream &out, const pair<K,T> &p) {
    return out<<"("<<p.first<<", "<<p.second<<")"; }
template <class T> void vprint(vector<T> v, int W=1) { cout<<"[\n";
    num(i,sz(v)) { if (i%W==0) cout<<"\n  "; cout<<v[i]<<", "; } cout<<"\n]\n"; }
// Cut end

typedef vector<map<int, double> > wgraph;
typedef pair<double, pair<int, int> > state;

double flow_augment(const wgraph &g, wgraph &flow, int source, int sink) {
    vector<int> from(g.size(), -1);
    priority_queue<state> pq;
    pq.push(mp(1e37, mp(source, source)));
    while (pq.size()) {
        int i = pq.top().second.second, s = pq.top().second.first;
        double f = pq.top().first; pq.pop();
        if (from[i] != -1) continue;
        if (f == 0.0) break;
        from[i] = s;
        if (i == sink) {
            int k = i;
            for (int k = i; from[k] != k; k = from[k]) {
                if (!has(flow[k], from[k])) {
                    flow[k][from[k]] = 0.0;
                }
                flow[k][from[k]] += f;
                flow[from[k]][k] -= f;
            }
            return f;
        }
        tr (flow[i], it) {
            if (from[it->first] != -1) continue;
            pq.push(mp(min(f, it->second), mp(i, it->first)));
        }
    }
    return 0.0;
}

// note: the flow WILL contain negative residual flows for
//       existing edges in the graph!
//pair<double, wgraph> maxflow(const wgraph &g, int source, int sink) {
double  maxflow(const wgraph &g, int source, int sink) {
    wgraph flow = g;
    double total_flow = 0.0, delta = 1.0;
    while (delta > 0.0) {
        delta = flow_augment(g, flow, source, sink);
        total_flow += delta;
    }
    for (int i = 0; i < sz(g); i++) tr (flow[i], it) {
        if (!has(g[i], it->first)) flow[i].erase(it->first);
        else it->second = g[i].at(it->first) - it->second;
    }
    return total_flow;
}

bool solve() {
    int W, H, B;
    scanf(" %d %d %d", &W, &H, &B);

    int N = W*H;
    wgraph g(2*N+2);
    num(i,W) num(j,H) {
        g[j*W+i][N+j*W+i] = 1;
        if (i>0) g[N+j*W+i][j*W+i-1] = 1;
        if (i<W-1) g[N+j*W+i][j*W+i+1] = 1;
        if (j>0) g[N+j*W+i][(j-1)*W+i] = 1;
        if (j<H-1) g[N+j*W+i][(j+1)*W+i] = 1;
    }

    num(b,B) {
        int x0,y0,x1,y1;
        scanf(" %d %d %d %d", &x0, &y0, &x1, &y1);
        for (int i=x0; i<=x1; i++) {
            for (int j=y0; j<=y1; j++) {
                g[j*W+i].clear();
                g[N+j*W+i].clear();
            }
        }
    }

    for (int i=0; i<W; i++) {
        g[2*N][i] = 1;
        g[N+(H-1)*W+i][2*N+1] = 1;
    }

    printf("%.0lf\n", maxflow(g,2*N,2*N+1));
    return true;
}

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        if (!solve()) break;
    }
}

// vim: set ff=unix ai tw=80 ts=4 sts=4 sw=4 et:
