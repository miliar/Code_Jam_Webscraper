#include <bits/stdc++.h>

using namespace std;

const int MAXN = 25 + 10;
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

int n;
int a[MAXN][MAXN], b[MAXN][MAXN];

void init() {
    cin >> n;
    for(int i = 1; i <= n; i++) {
        string s;
        cin >> s;
        for(int j = 1; j <= n; j++) a[i][j] = s[j - 1] - '0';
    }
}

int get_bit(int x, int n) {
    return ((x >> n) & 1);
}

bool check(int x) {

    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= n; j++)
            if (b[i][j] == 0) {
                Dinic d(n * n + 2);
                int cnt = 0;
                for(int v = 1; v <= n; v++)
                    if (b[i][v] == 1) {
                        cnt++;
                        for(int u = 1; u <= n; u++)
                            if ((u != i) && (b[u][v] == 1)) {
                                d.AddEdge(u, n + v, 1);
                            }
                    }
                int src = 0, snk = n * n + 1;
                for(int i = 1; i <= n; i++) d.AddEdge(src, i, 1);
                for(int i = n + 1; i <= n + n; i++) d.AddEdge(i, snk, 1);

                //cout << i << " " << j << " " << cnt << " " << d.GetMaxFlow(src, snk) << endl;
                if (d.GetMaxFlow(src, snk) == cnt) return false;
            }
    return true;
}

int get_cost(int x) {
    int res = 0;
    for(int i = 1; i <= n * n; i++) {
        int u = get_bit(x, i - 1);
        int v = a[i / n + (i % n > 0)][(i - 1) % n + 1];
        if ((u == 0) && (v == 1)) return INF;
        if ((u == 1) && (v == 0)) res++;
        b[i / n + (i % n > 0)][(i - 1) % n + 1] = u;
    }

    if (check(x)) return res;
    else return INF;
}

void solve() {
    init();
    int res = INF;
    for(int i = 1; i < (1 << (n * n)); i++) {
        int cost = get_cost(i);
        res = min(res, cost);
    }

    cout << res << endl;
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-0.out", "w", stdout);

    int ntests;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; tc++) {
        cout << "Case #" << tc << ": ";
        solve();
    }
}
