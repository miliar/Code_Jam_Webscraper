#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to, c, f;

    Edge(int _to, int _c): to(_to), c(_c), f(0) {}
};

const int MAXN = 10 * 1000 + 5, INF = 1000 * 1000 * 1000 + 5;
int pos[MAXN], d[MAXN], n;
vector<Edge> e;
vector<int> g[MAXN];
map<string, pair<int, int> > mp;

void addEdge(int v, int u, int c) {
    g[v].push_back(e.size());
    e.push_back(Edge(u, c));
    g[u].push_back(e.size());
    e.push_back(Edge(v, 0));
}

void addFlow(int id, int flow) {
    e[id].f += flow;
    e[id ^ 1].f -= flow;
}

bool bfs(int s, int t) {
    for(int i = 0; i < n; i++)
        d[i] = INF;
    d[s] = 0;
    queue<int> q;
    q.push(s);
    while(!q.empty() && d[t] >= INF) {
        int v = q.front();
        q.pop();
        for(size_t i = 0; i < g[v].size(); i++) {
            int u = e[g[v][i]].to, cf = e[g[v][i]].c - e[g[v][i]].f;
            if(cf && d[u] >= INF) {
                d[u] = d[v] + 1;
                q.push(u);
            }
        }
    }
    return d[t] < INF;
}

int dfs(int v, int t, int mincf) {
    if(!mincf || v == t)
        return mincf;
    for(; pos[v] < (int)g[v].size(); pos[v]++) {
        int id = g[v][pos[v]], u = e[id].to, cf = e[id].c - e[id].f;
        if(d[u] == d[v] + 1) {
            int f = dfs(u, t, min(mincf, cf));
            if(f) {
                addFlow(id, f);
                return f;
            }
        }
    }
    return 0;
}

int dinic(int s, int t) {
    int res = 0;
    while(bfs(s, t)) {
        for(int i = 0; i < n; i++)
            pos[i] = 0;
        while(int f = dfs(s, t, INF))
            res += f;
    }
    return res;
}

pair<int, int> add(string &w) {
    if(mp.find(w) != mp.end())
        return mp[w];
    int a = n++, b = n++;
    addEdge(a, b, 1);
    return mp[w] = make_pair(a, b);
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        int m;
        in >> m >> ws;
        n = 0;
        mp.clear();
        e.clear();
        for(int i = 0; i < MAXN; i++)
            g[i].clear();
        int a = -1, b = -1;
        for(int i = 0; i < m; i++) {
            int v = n++;
            if(i == 0)
                a = v;
            else if(i == 1)
                b = v;
            string s;
            getline(in, s);
            for(size_t j = 0; j < s.length(); j++) {
                if(s[j] == ' ')
                    continue;
                size_t k = j;
                while(k < s.length() && s[k] != ' ')
                    k++;
                string w = s.substr(j, k - j);
                pair<int, int> wid = add(w);
                addEdge(v, wid.first, 1);
                addEdge(wid.second, v, 1);
                j = k;
            }
        }
        out << "Case #" << tt + 1 << ": " << dinic(a, b) << '\n';
    }
    return 0;
}
