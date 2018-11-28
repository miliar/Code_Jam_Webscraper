#include <cstdio>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <utility>
#include <numeric>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <cassert>

typedef long long ll;
typedef std::pair<int, int> pii;

const int MAX = 1111;
int N, S;
int X[MAX], Y[MAX], Z[MAX];
int VX[MAX], VY[MAX], VZ[MAX];

struct edge {
    int u, v;
    double w;

    edge(int _u, int _v, double _w) 
        : u(_u), v(_v), w(_w) {}

    bool operator < (const edge & r) const {
        if(w != r.w) return w < r.w;
        if(u != r.u) return u < r.u;
        return v < r.v;
    }
};

struct nd {
    int rank;
    int parent;
    nd() : parent(0), rank(0) {}
    nd(int _p, int _r=0) : parent(_p), rank(_r) {}
} sub[MAX];

int find(int i) {
    if(sub[i].parent != i)
        sub[i].parent = find(sub[i].parent);
    return sub[i].parent;
}

void join(int x, int y) {
    int xroot = find(x);
    int yroot = find(y);

    if(sub[xroot].rank < sub[yroot].rank) 
        sub[xroot].parent = yroot;
    else if(sub[xroot].rank > sub[yroot].rank)
        sub[yroot].parent = xroot;
    else {
        sub[yroot].parent = xroot;
        sub[xroot].rank++;
    }
}

double sq(double arg) { return arg * arg; }
double dist(int a, int b) {
    return sqrt(sq(X[a] - X[b]) + sq(Y[a] - Y[b]) + sq(Z[a] - Z[b]));
}

double solve() {
    for(int i = 0; i < N; ++i) sub[i] = nd(i);

    std::vector<edge> edges;
    for(int i = 0; i < N; ++i)
        for(int j = 0; j < N; ++j) {
            edges.push_back(edge(i, j, dist(i, j)));
            edges.push_back(edge(j, i, dist(i, j)));
        }
    std::sort(edges.begin(), edges.end());
    
    std::vector<std::vector<int> > adj;
    adj.resize(N);
    for(const edge & e : edges) {
        if(find(e.u) != find(e.v)) {
            join(e.u, e.v);
            adj[e.u].push_back(e.v);
            adj[e.v].push_back(e.u);
            /* printf("%d %d %g\n", e.u, e.v, e.w); */
        }
    }

    double res = 0.0;
    int par[MAX];
    bool seen[MAX];
    memset(par, -1, sizeof(par));
    memset(seen, false, sizeof(seen));
    std::queue<int> q;
    q.push(0);
    while(!q.empty()) {
        int cur = q.front(); q.pop();
        if(cur == 1) break;
        assert(!seen[cur]);
        seen[cur] = true;

        for(int nxt : adj[cur]) {
            if(seen[nxt]) continue;
            assert(par[nxt] == -1);
            par[nxt] = cur;
            q.push(nxt);
        }
    }

    int cur = 1;
    while(cur != 0) {
        res = std::max(res, dist(cur, par[cur]));
        cur = par[cur];
    }

    return res;
}

int main() {
    int CS;
    std::cin >> CS;
    std::cout << std::fixed << std::setprecision(9);
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N >> S;
        for(int n = 0; n < N; ++n) {
            std::cin >> X[n] >> Y[n] >> Z[n];
            std::cin >> VX[n] >> VY[n] >> VZ[n];
        }

        double ans = solve();
        std::cout << "Case #" << cs << ": " << ans << std::endl;
    }
    return 0;
}

