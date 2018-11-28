#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

struct TEdge {
    int from, to;
    ll cap, flow;
    ll cost;
    TEdge* reverse;
};

TEdge edgePool[50000000];
int edgePoolPtr = 0;

typedef vector<TEdge*> ve;
vector< ve > edges;

int SOURCE, TARGET;

TEdge* AddEdge(int from, int to, ll capacity, ll cost = 0) {
    TEdge* e1 = &edgePool[edgePoolPtr++];
    TEdge* e2 = &edgePool[edgePoolPtr++];
    TEdge fw = {from, to, capacity, 0, cost, e2};
    TEdge bw = {to, from, 0, 0, cost, e1};
    *e1 = fw;
    *e2 = bw;
//    cerr << edges.size() << endl;
    edges[from].push_back(e1);
    edges[to].push_back(e2);
    return e1;
}

inline ll AvailableCapacity(const TEdge* p) {
    return (p->cap - p->flow);
}

vvi x;
int w,h,b,N;

vector<bool> been;
bool ff_dfs(int p) {
    if (p == TARGET) return true;
    if (been[p]) return false;
    been[p] = true;
    for (ve::iterator it = edges[p].begin(); it != edges[p].end(); it++) {
        if ((*it)->flow < (*it)->cap && ff_dfs((*it)->to)) {
            (*it)->flow++;
            (*it)->reverse->flow--;
            return true;
        }
    }
    return false;
}

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

bool ok(int i, int j) {
    if (i < 0 || j < 0 || i >= w || j >= h)
        return 0;
    for (int l = 0; l < b; ++l) {
        if (x[l][0] <= i && i <= x[l][2] && x[l][1] <= j && j <= x[l][3]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        cin >> w >> h >> b;
        x.assign(b, vi(4));
        for (int i = 0; i < b; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &x[i][j]);
            }
        }
        N = w*h;
        SOURCE = 2*w*h;
        TARGET = SOURCE + 1;
        edges.assign(TARGET + 1, ve());
//        cerr << TARGET << " " << edges.size() << endl;
        for (int i = 0; i < w; ++i) for (int j = 0; j < h; ++j) {
            if (!ok(i, j)) continue;
            AddEdge(i*h+j, N+i*h+j, 1);
            for (int d = 0; d < 4; ++d) {
                int ni = i+dx[d], nj = j+dy[d];
                if (!ok(ni, nj)) continue;
                AddEdge(N+i*h+j, ni*h+nj, 1);
            }
        }
        for (int i = 0; i < w; ++i) {
            AddEdge(SOURCE, i*h, 1);
            AddEdge(N+i*h+h-1, TARGET, 1);
        }
        int res = 0;
        been.assign(TARGET+1, 0);
        while (ff_dfs(SOURCE)) {
            ++res;
            been.assign(TARGET+1, 0);
        }
        cout << res << endl;
    }
    return 0;
}
