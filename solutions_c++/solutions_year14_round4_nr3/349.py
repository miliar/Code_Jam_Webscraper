/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

const int max_n = 50000 * 2 + 10;

struct network {
    struct node {
        int v, c, b;
        node(int _v, int _c, int _b): v(_v), c(_c), b(_b) {
        }
    };
    int n, src, dst, h[max_n], cnt[max_n];
    vector<node> adj[max_n];
    void clear() {
        for (int i = 0; i < n; ++i)
            adj[i].clear();
        n = 0;
    }
    void insert(int u, int v, int c, bool d = false) {
        n = max(n, max(u, v) + 1);
        adj[u].push_back(node(v, c, adj[v].size()));
        adj[v].push_back(node(u, d ? c : 0, adj[u].size() - 1));
    }
    int get_max_flow(int from, int to) {
        src = from;
        dst = to;
        memset(h, 0, sizeof(h));
        memset(cnt, 0, sizeof(cnt));
        int flow = 0;
        while (h[src] < n)
            flow += dfs(src, INT_MAX);
        return flow;
    }
    int dfs(int v, int flow) {
        if (v == dst)
            return flow;
        int min_h = n - 1, res = 0;
        for (vector<node>::iterator i = adj[v].begin(); flow != 0 && i != adj[v].end(); ++i) {
            if (i->c == 0)
                continue;
            if (h[i->v] + 1 == h[v]) {
                int k = dfs(i->v, min(i->c, flow));
                if (k != 0) {
                    i->c -= k;
                    adj[i->v][i->b].c += k;
                    flow -= k;
                    res += k;
                }
                if (h[src] >= n)
                    return res;
            }
            min_h = min(min_h, h[i->v]);
        }
        if (res != 0)
            return res;
        if (--cnt[h[v]] == 0)
            h[src] = n;
        h[v] = min_h + 1;
        ++cnt[h[v]];
        return 0;
    }
};

int t, w, h, n, cell[120][512];
network g;

void solve() {
    scanf("%d%d%d", &w, &h, &n);
    memset(cell, 0, sizeof(cell));
    for (int i = 0; i < n; ++i) {
        int x1, y1, x2, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        for (int x = x1; x <= x2; ++x)
            for (int y = y1; y <= y2; ++y)
                cell[x][y] = 1;
    }
    g.clear();
    for (int i = 0; i < w; ++i) {
        for (int j = 0; j < h; ++j) {
            // printf("%d ", cell[i][j]);
            if (cell[i][j])
                continue;
            g.insert((i * h + j) * 2, (i * h + j) * 2 + 1, 1);
            if (i > 0 && !cell[i - 1][j])
                g.insert((i * h + j) * 2 + 1, ((i - 1) * h + j) * 2, 1);
            if (i < w - 1 && !cell[i + 1][j])
                g.insert((i * h + j) * 2 + 1, ((i + 1) * h + j) * 2, 1);
            if (j > 0 && !cell[i][j - 1])
                g.insert((i * h + j) * 2 + 1, (i * h + j - 1) * 2, 1);
            if (j < h - 1 && !cell[i][j + 1])
                g.insert((i * h + j) * 2 + 1, (i * h + j + 1) * 2, 1);
            if (j == 0)
                g.insert(w * h * 2, (i * h + j) * 2, 1);
            if (j == h - 1)
                g.insert((i * h + j) * 2 + 1, (w * h) * 2 + 1, 1);
        }
        // puts("");
    }
    g.n = (w * h) * 2 + 2;
    fprintf(stderr, "t");
    printf("Case #%d: %d\n", ++t, g.get_max_flow(w * h * 2, (w * h) * 2 + 1));
    fprintf(stderr, "%d\n", t);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
