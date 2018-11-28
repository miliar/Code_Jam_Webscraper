#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)(x).size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))

const LL INF = (LL) 1e18;

int n, m, p;

int mn_e[2005];
int mx_e[2005];

bool forbidden_e[2005];

int endp[2005][2];

vector<PII> e[1005];

vector<LL> dijkstra(int x, int *costs, const vector<LL>& max_allowed, LL starting = 0) {
    vector<LL> dist(n + 1, INF);
    priority_queue<pair<LL, int>, vector<pair<LL, int> >, greater<pair<LL, int> > > q;
    dist[x] = starting;
    q.push(MP(starting, x));
    while (!q.empty()) {
        int c = q.top().second;
        LL cd = q.top().first;
        q.pop();
        if (cd > dist[c]) {
            continue;
        }
        FORE (it, e[c]) {
            if (forbidden_e[it->ND]) {
                continue;
            }
            LL nd = cd + costs[it->ND];
            if (nd < dist[it->ST] && nd <= max_allowed[it->ST]) {
                dist[it->ST] = nd;
                q.push(MP(nd, it->ST));
            }
        }
    }
    return dist;
}

bool check(const vector<int>& picked, int c) {
    for (int i = 1; i <= m; ++i) {
        forbidden_e[i] = false;
    }
    for (int i = 0; i < c; ++i) {
        forbidden_e[picked[i]] = true;
    }
    vector<LL> total_cost(c + 1);
    vector<int> vertex(c + 1);
    vector<char> got(n + 1, false);
    total_cost[0] = 0;
    vertex[0] = 1;
    got[1] = true;
    for (int i = 0; i < c; ++i) {
        int z = 0;
        if (endp[picked[i]][z] == vertex[i]) {
            ++z;
        }
        vertex[i + 1] = endp[picked[i]][z];
        if (got[vertex[i + 1]]) {
            return false;
        }
        got[vertex[i + 1]] = true;
        total_cost[i + 1] = total_cost[i] + mn_e[picked[i]];
    }
    vector<LL> max_allowed(n + 1, INF);
    for (int i = 0; i < (int) vertex.size(); ++i) {
        vector<LL> dist = dijkstra(vertex[i], mx_e, vector<LL>(n + 1, INF));
        for (int j = 1; j <= n; ++j) {
            max_allowed[j] = min(max_allowed[j], dist[j] + total_cost[i]);
        }
    }
    for (int i = 0; i < (int) vertex.size(); ++i) {
        if (max_allowed[vertex[i]] < total_cost[i]) {
            return false;
        }
    }
    vector<LL> dist = dijkstra(vertex.back(), mn_e, max_allowed, total_cost.back());
    return dist[2] < INF;
}

void alg() {
    cin >> n >> m >> p;
    for (int i = 1; i <= m; ++i) {
        int u, v;
        cin >> u >> v >> mn_e[i] >> mx_e[i];
        e[u].PB(MP(v, i));
        e[v].PB(MP(u, i));
        endp[i][0] = u;
        endp[i][1] = v;
    }
    vector<int> picked(p);
    for (int i = 0; i < p; ++i) {
        cin >> picked[i];
    }
    int l = 0;
    int r = p;
    while (l < r) {
        int c = (l + r + 1) / 2;
        if (check(picked, c)) {
            l = c;
        } else {
            r = c - 1;
        }
    }
    if (l == p) {
        cout << "Looks Good To Me" << endl;
    } else {
        cout << picked[l] << endl;
    }
    for (int i = 1; i <= n; ++i) {
        e[i].clear();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int d;
    cin >> d;
    for (int i = 1; i <= d; ++i) {
        cout << "Case #" << i << ": ";
        alg();
    }
}
