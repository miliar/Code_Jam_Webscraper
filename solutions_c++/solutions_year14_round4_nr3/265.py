#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <utility>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

template<class W>
struct Edge {
    int u, v;
    W capa, flow;
    int next, rev;
    Edge(int u, int v, const W& c, const W& f)
        : u(u), v(v), capa(c), flow(f) {}
    W res() const { return capa - flow; }
};

template<class E>
struct Graph {
    int n, m;
    vector<E> es;
    vector<int> head;
    Graph(int _n) : n(_n), m(0), head(_n, -1) {}
    void add(const E& e) {
        es.push_back(e);
        es[m].next = head[e.u];
        head[e.u] = m;
        m++;
    }
    void add_rev(const E& e, const E& r) {
        assert(e.u == r.v && e.v == r.u);
        add(e);
        add(r);
        es[m-2].rev = m-1;
        es[m-1].rev = m-2;
    }
    void reindex() {
        fill(head.begin(), head.end(), -1);
        for(int i=m-1; i>=0; i--) {
            es[i].next = head[es[i].u];
            head[es[i].u] = i;
        }
    }
};

struct MaxFlow {
    typedef int capa_t;
    typedef Edge<capa_t> E;
    Graph<E> g;
    vector<int> prev;
    MaxFlow(int n) : g(n), prev(n) {}
    void add_edge(int u, int v, int ca) {
        g.add_rev(E(u, v, ca, 0), E(v, u, 0, 0));
    }
    int pour(int s, int t, capa_t F=1<<30) {
        capa_t total = 0;
        while(total < F) {
            fill(prev.begin(), prev.end(), -1);
            queue<int> q;
            prev[s] = g.m;
            q.push(s);
            while(!q.empty() && prev[t]<0) {
                const int u = q.front();
                q.pop();
                for(int x=g.head[u]; x!=-1; x=g.es[x].next) {
                    const E& e = g.es[x];
                    if(prev[e.v]<0 && e.res() > 0) {
                        prev[e.v] = x;
                        q.push(e.v);
                    }
                }
            }
            if(prev[t]<0) return total;
            capa_t inc = F-total;
            for(int at=t; prev[at]!=g.m; at=g.es[prev[at]].u) {
                const E& e = g.es[prev[at]];
                inc = min(inc, e.res());
            }
            for(int at=t; prev[at]!=g.m; at=g.es[prev[at]].u) {
                E& e = g.es[prev[at]];
                E& r = g.es[e.rev];
                e.flow += inc;
                r.flow -= inc;
            }
            total += inc;
        }
        return total;
    }
};

int w, h, f[128][512];

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

int solve() {
    MaxFlow flow(2+w*h*2);
    rep (i, w) rep (j, h) {
        const int ix = i * h + j;
        flow.add_edge(2+2*ix, 2+2*ix+1, 1);
    }
    rep (i, w) rep (j, h) if (f[i][j] == 0) {
        const int ix = i * h + j;
        if (j == 0) {
            flow.add_edge(0, 2+2*ix, 1);
        }
        if (j == h-1) {
            flow.add_edge(2+2*ix+1, 1, 1);
        }
        rep (d, 4) {
            const int nx = i + dx[d];
            const int ny = j + dy[d];
            const int jx = nx * h + ny;
            if (0 <= nx && nx < w && 0 <= ny && ny < h) {
                if (f[nx][ny] == 0) {
                    flow.add_edge(2+2*ix+1, 2+2*jx, 1);
                }
            }
        }
    }
    return flow.pour(0, 1);
}

int main() {
    int T;
    cin >> T;
    for (int _q = 0; _q < T; _q++) {
        int b;
        cin >> w >> h >> b;
        memset(f, 0, sizeof(f));
        rep (i, b) {
            int x0, y0, x1, y1;
            cin >> x0 >> y0 >> x1 >> y1;
            for (int x = x0; x <= x1; x++) {
                for (int y = y0; y <= y1; y++) {
                    f[x][y] = 1;
                }
            }
        }
        printf("Case #%d: %d\n", _q+1, solve());
    }
    return 0;
}

