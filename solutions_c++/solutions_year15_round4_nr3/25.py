#include<bits/stdc++.h>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
// Let's Fight!

const int MAXN = 212;
const int MAXW = 5000;
const int INF = 1029384756;

int N;
string raws[MAXN];
vector<int> vec[MAXN];
map<string, int> mp;
string inv[MAXW];

class Isap
{
public:
    static const int MXN = 10000;
    class Edge
    {
    public:
        int v, f, re;
        Edge()
        {
            v = f = re = -1;
        }
        Edge(int _v, int _f, int _r)
        {
            v = _v;
            f = _f;
            re = _r;
        }
    };
    int n, s, t, h[MXN], gap[MXN];
    vector<Edge> E[MXN];
    void init(int _n, int _s, int _t)
    {
        n = _n;
        s = _s;
        t = _t;
        for (int i = 0; i < n; i++)
            E[i].clear();
    }
    void add_edge(int u, int v, int f)
    {
        E[u].PB(Edge(v, f, E[v].size()));
        E[v].PB(Edge(u, 0, E[u].size() - 1));
    }
    int DFS(int u, int nf, int res = 0)
    {
        if (u == t) return nf;
        for (auto& it : E[u]) {
            if (h[u] == h[it.v] + 1 && it.f > 0) {
                int tf = DFS(it.v, min(nf, it.f));
                res += tf;
                nf -= tf;
                it.f -= tf;
                E[it.v][it.re].f += tf;
                if (nf == 0) return res;
            }
        }
        if (nf) {
            if (--gap[h[u]] == 0) h[s] = n;
            gap[++h[u]]++;
        }
        return res;
    }
    int flow(int res = 0)
    {
        FZ(h);
        FZ(gap);
        gap[0] = n;
        while (h[s] < n)
            res += DFS(s, 2147483647);
        return res;
    }
} flow;

int calc()
{
    int M = mp.size();
    int V = N + M * 2;
    flow.init(V, 0, 1);
    
    for(int i=0; i<N; i++)
    {
        for(auto j: vec[i])
        {
            flow.add_edge(i, N+j, INF);
            flow.add_edge(N+M+j, i, INF);
        }
    }
    for(int i=0; i<M; i++)
    {
        flow.add_edge(N+i, N+M+i, 1);
    }

    return flow.flow();
}

void init()
{
    mp.clear();
    for (int i = 0; i < N; i++) {
        vec[i].clear();
    }
}

int main()
{
    IOS;
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        cin >> N;
        init();
        string s;
        getline(cin, s);
        for (int i = 0; i < N; i++) {
            getline(cin, raws[i]);
            stringstream ss;
            ss.str(raws[i]);
            while (ss >> s) {
                if (!mp.count(s)) {
                    int z = mp.size();
                    mp[s] = z;
                    inv[z] = s;
                }
                vec[i].PB(mp[s]);
            }
        }

        int ans = calc();
        cout << "Case #" << tt << ": " << ans << endl;
    }

    return 0;
}
