#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <stack>
#include <queue>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <cstring>

#define rep(i,n) for(int i=0;i<(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

bool field[100][500];

typedef pair<int, int> P;
struct edge {int to, cap, rev;};
int V;
const int INF = 1 << 29;
const int MAX_V = 120000;
vector<vector<edge> > G;
int level[MAX_V], iter[MAX_V];
 
void add_edge(int from, int to, int cap) {
    G[from].push_back((edge){to,cap,G[to].size()});
    G[to].push_back((edge){from, 0, G[from].size()-1});
}
 
void bfs(int s) {
    memset(level, -1, sizeof(level));
    queue<int> que;
    level[s] = 0;
    que.push(s);
    while(!que.empty()) {
        int v = que.front();que.pop();
        rep(i, G[v].size()) {
            edge &e = G[v][i];
            if (e.cap > 0 && level[e.to] < 0) {
                level[e.to] = level[v] + 1;
                que.push(e.to);
            }
        }
    }
}

int dfs(int v, int t, int f) {
    if (v == t) return f;
    for (int &i = iter[v]; i < G[v].size(); i++) {
        edge &e = G[v][i];
        if (e.cap > 0 && level[v] < level[e.to]) {
            int d = dfs(e.to, t, min(f, e.cap));
            if (d > 0) {
                e.cap -= d;
                G[e.to][e.rev].cap += d;
                return d;
            }
        }
    }
    return 0;
}

int max_flow(int s, int t) {
    int flow = 0;
    for (;;) {
        bfs(s);
        if (level[t] < 0) return flow;
        memset(iter, 0, sizeof(iter));
        int f;
        while ((f = dfs(s, t, INF) > 0)) {
            flow += f;
        }
    }
}

void solve() {
    int W, H, B;
    cin >> W >> H >> B;
    V = W * H * 2 + 2;
    G = vector<vector<edge> >(V);
    rep(i, W)rep(j, H)field[i][j] = true;

    rep(i, B) {
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        for (int j = x0; j <= x1; j++) {
            for (int k = y0; k <= y1; k++) {
                field[j][k] = false;
            }
        }
    }

    int s = V - 1, t = V - 2;
    rep(i, W) {
        rep(j, H) {
            add_edge(i * H + j, W * H + i * H + j, 1);
        }
    }
    rep(i, W) {
        if (field[i][0] == true) add_edge(s, i * H, 1);
        if (field[i][H - 1] == true) add_edge(W * H + i * H + H - 1, t, 1);
    }
    
    rep(i, W) {
        rep(j, H) {
            if (i != 0 && field[i - 1][j]) add_edge(W * H + i * H + j, (i - 1) * H + j, 1);
            if (i != W - 1 && field[i + 1][j]) add_edge(W * H + i * H + j, (i + 1) * H + j, 1);
            if (j != H - 1 && field[i][j + 1]) add_edge(W * H + i * H + j, i * H + (j + 1), 1);
            if (j != 0 && field[i][j - 1]) add_edge(W * H + i * H + j, i * H + (j - 1), 1);
        }
    }
    
    cout << max_flow(s, t) << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
