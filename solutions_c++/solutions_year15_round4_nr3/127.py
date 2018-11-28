#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

const int INF = 1e9;

#define MAX_V 16384

struct Edge{
  int src, dest;
  int cap, rev;
};
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;
int d[MAX_V];
int iter[MAX_V];

void add_edge(Graph &g, int src, int dest, int cap) {
  g[src].push_back((Edge){src, dest, cap, (int)g[dest].size()});
  g[dest].push_back((Edge){dest, src, 0, (int)g[src].size() - 1});
}

void bfs(Graph &g, int s) {
  memset(d, -1, sizeof(d));
  queue<int> que;
  d[s] = 0;
  que.push(s);
  while(!que.empty()) {
    int v = que.front(); que.pop();
    REP(i, g[v].size()) {
      Edge &e = g[v][i];
      if (e.cap > 0 && d[e.dest] < 0) {
        d[e.dest] = d[v] + 1;
        que.push(e.dest);
      }
    }
  }
}

int dfs(Graph &g, int v, int t, int f) {
  if (v == t) return f;
  for (int &i = iter[v]; i < (int)g[v].size(); i++) {
    Edge &e = g[v][i];
    if (e.cap > 0 && d[v] < d[e.dest]) {
      int d = dfs(g, e.dest, t, min(f, e.cap));
      if (d > 0) {
        e.cap -= d;
        g[e.dest][e.rev].cap += d;
        return d;
      }
    }
  }
  return 0;
}

int max_flow(Graph g, int s, int t) {
  int flow = 0;
  for (;;) {
    bfs(g, s);
    if (d[t] < 0) return flow;
    memset(iter, 0, sizeof(iter));
    int f;
    while ((f = dfs(g, s, t, INF)) > 0) flow += f;
  }
}

map<string,int> ma;

int has(string str) {
  if (ma.count(str)) return ma[str];
  int num = ma.size();
  ma[str] = num;
  return num;
}

vector<int> uniq(vector<int> v) {
  sort(ALL(v));
  auto it = unique(ALL(v));
  vector<int> w;
  for (auto i = v.begin(); i != it; ++i)
    w.push_back(*i);
  return w;
}

vector<int> ary[256];

int solve() {
  int N; cin >> N;
  string str;
  getline(cin, str);
  REP(i,N) {
    getline(cin, str);
    istringstream is(str);
    string s;
    vector<int> v;
    while (is >> s) v.push_back(has(s));
    ary[i] = uniq(v);
  }
  int V = ma.size();
  Graph g(2 * V + 2);
  int source = 2 * V, sink = 2 * V + 1;
  REP(i,V) {
    add_edge(g, source, i, 3000);
    add_edge(g, i, i + V, 3001);
    add_edge(g, i + V, sink, 3000);
  }
  for (int i : ary[0]) add_edge(g, V + i, sink, 10000000);
  for (int i : ary[1]) add_edge(g, source, i, 10000000);
  REP(i,N) {
    REP(j,ary[i].size()) REP(k,ary[i].size()) {
      if (j == k) continue;
      add_edge(g, ary[i][j] + V, ary[i][k], 10000000);
    }
  }
  return max_flow(g, source, sink) - 3000 * V;
}

int main() {
  int T; cin >> T;
  REP(i,T) {
    ma.clear();
    cout << "Case #" << i + 1 << ": " << solve() << endl;
  }
  return 0;
}
