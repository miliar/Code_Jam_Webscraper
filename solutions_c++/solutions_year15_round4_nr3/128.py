#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <cassert>
#include <queue>
#include <sstream>
#include <set>
#include <functional>
#include <cfloat>
#include <unordered_map>
#include <ctime>
#include <complex>
#include <cmath>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef complex<double> cd;
#define mp make_pair                                                  

const ll MN = 2000000;
const ll mod = 1e9 + 7;

struct edge
{
    int v, u, flow, cap;
};

vector<edge> es;

int q[MN];
vi G[MN];
int d[MN];
int p[MN];
bool used[MN];

void add_edge(int v, int u, int cap)
{
    es.push_back(edge{ v, u, 0, cap });
    es.push_back(edge{ u, v, 0, 0 });
    G[v].push_back(es.size() - 2);
    G[u].push_back(es.size() - 1);
}

bool bfs(int s, int t)
{
    int qh = 0;
    int qt = 0;
    fill(d, d + MN, -1);
    d[s] = 0;
    q[qt++] = s;
    while (qh < qt)
    {
        int v = q[qh++];
        for (int i = 0; i < G[v].size(); ++i)
        {
            int idx = G[v][i];
            int u = es[idx].u;
            if (d[u] == -1 && es[idx].flow < es[idx].cap)
            {
                q[qt++] = u;
                d[u] = d[v] + 1;
            }
        }
    }
    return d[t] != -1;
}

int dfs(int v, int flow, int t)
{
    if (!flow)
        return 0;
    if (v == t)
        return flow;
    for (; p[v] < G[v].size(); ++p[v])
    {
        int idx = G[v][p[v]];
        int u = es[idx].u;
        if (d[u] != d[v] + 1)
            continue;
        int pushed = dfs(u, min(flow, es[idx].cap - es[idx].flow), t);
        if (pushed)
        {
            es[idx].flow += pushed;
            es[idx ^ 1].flow -= pushed;
            return pushed;
        }
    }
    return 0;
}

int dinic(int s, int t)
{
    int flow = 0;
    while (bfs(s, t))
    {
        fill(p, p + MN, 0);
        while (int pushed = dfs(s, 1e9, t))
            flow += pushed;
    }
    return flow;
}

void dfs2(int v)
{
    used[v] = true;
    for (int i = 0; i < G[v].size(); ++i)
    {
        int idx = G[v][i];
        if (es[idx ^ 1].cap > es[idx ^ 1].flow)
        {
            int u = es[idx].u;
            if (!used[u])
                dfs2(u);
        }
    }
}

void solve(int s, int t)
{
    int flow = dinic(s, t);
    cout << flow;
}

void solve()
{
    for (int i = 0; i < MN; ++i)
    {
        es.clear();
        q[i] = 0;
        G[i].clear();
        d[i] = p[i] = 0;
        used[i] = 0;
    }

    char* buf = new char[100000];
    int n;
    cin >> n;
    map<int, int> s_to_v;
    map<string, int> w_to_v;
    int vmax = 1;
    cin.getline(buf, 100000);
    for (int i = 0; i < n; ++i)
    {
        cin.getline(buf, 100000);
        string s(buf);
        istringstream iss(s);
        s_to_v[i] = vmax;
        vmax++;
        string w;
        set<string> u_w;
        while (iss >> w)
        {
            if (u_w.find(w) != u_w.end())
                continue;
            u_w.insert(w);
            int v;
            if (w_to_v[w] != 0)
                v = w_to_v[w];
            else
            {
                v = vmax;
                vmax += 2;
                add_edge(v, v + 1, 1);
                w_to_v[w] = v;
            }
            add_edge(s_to_v[i], v, 1);
            add_edge(v + 1, s_to_v[i], 1);
        }
    }
    solve(1, s_to_v[1]);
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}