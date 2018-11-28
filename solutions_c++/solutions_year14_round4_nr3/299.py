#include <iostream>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>
#include <cassert>
#include <ctime>


using namespace std;

#define ll long long
#define y1 _dfdfdfd


const int maxn = 510;
const int maxm = 110;
const int inf = 1000000007;
const int mod = 1000000007;
const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

struct Graph {
    struct Edge {
        int from, to, cap, flow, cost;
         
        Edge() {}
        Edge(int from, int to, int cap, int cost = 0) : from(from), to(to), cap(cap), flow(0), cost(cost) {}
    };
     
    int n;
    int S, T;
    vector<vector<int> > e;
    vector<Edge> edges;
    vector<int> d, c;
     
    Graph() {}
    Graph(int N) {
        n = 2 * N;
        e.resize(n);
        for (int i = 1; i + 1 < N; i++) addEdge(2 * i, 2 * i + 1, 1, 1);
        addEdge(0, 1, 1e9, 1);
        addEdge(n - 2, n - 1, 1e9, 1);
    }
 
private:
    bool bfs() {
        queue<int> q;
        c.assign(n, 0);
        d.assign(n, inf);
        q.push(S);
        d[S] = 0;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int i = 0; i < (int)e[v].size(); i++) {
                Edge cur = edges[e[v][i]];
                if (d[cur.to] > d[v] + 1 && cur.flow < cur.cap) {
                    d[cur.to] = d[v] + 1;
                    q.push(cur.to);
                }
            }
        }
        return d[T] != inf;
    }
     
    int dfs(int v, int flow) {
        if (v == T) return flow;
        if (!flow) return 0;
        for (int &i = c[v]; i < (int)e[v].size(); i++) {
            Edge cur = edges[e[v][i]];
            if (d[cur.to] != d[v] + 1) continue;
            int pushed = dfs(cur.to, min(flow, cur.cap - cur.flow));
            if (pushed) {
                edges[e[v][i]].flow += pushed;
                edges[e[v][i] ^ 1].flow -= pushed;
                return pushed;
            }
        }
        return 0;
    }
 
public:
    void addEdge(int from, int to, int cap, int cost = 0) {
        if (cost == 0) {
            from = 2 * from + 1;
            to = 2 * to;
        }
        e[from].push_back(edges.size());
        edges.push_back(Edge(from, to, cap, cost));
        e[to].push_back(edges.size());
        edges.push_back(Edge(to, from, 0, -cost));
    }
     
    int getFlow(int s = -1, int t = -1) {
        if (s == -1 && t == -1) {
            s = 0;
            t = n - 1;
        }
        S = s;
        T = t;
         
        int flow = 0;
        while (bfs()) {
            while (int pushed = dfs(S, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};
 
char c[maxn][maxm];
int w, h, n;

bool ok(int x, int y) {
    return 0 <= x && x < h && 0 <= y && y < w && c[x][y] == 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        memset(c, 0, sizeof(c));
        cin >> w >> h >> n;
        for (int i = 0; i < n; i++) {
            int x1, y1, x2, y2;
            cin >> y1 >> x1 >> y2 >> x2;
            for (int x = x1; x <= x2; x++) {
                for (int y = y1; y <= y2; y++) {
                    c[x][y] = 1;
                }
            }
        }
        
        Graph gr(w * h + 2);
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) if (ok(i, j)) {
                int num = i * w + j + 1;
                if (i == 0) gr.addEdge(0, num, 1);
                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k], ny = j + dy[k];
                    if (!ok(nx, ny)) continue;
                    int num2 = nx * w + ny + 1;
                    gr.addEdge(num, num2, 1);
                }
                if (i == h - 1) gr.addEdge(num, w * h + 1, 1);
            }
        }
        cout << gr.getFlow() << endl;
        cerr << test << endl;
    }

	return 0;
}
