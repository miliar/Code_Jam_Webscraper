#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <sstream>
#include <queue>
#include <map>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

namespace maxflow {
  typedef pair<int, int> edge;
#define b first
#define d second

  const int MAXN = 50050;
  const int inf = 2e9;
  
  vector<edge> E[MAXN];
  vector<int> cap[MAXN];
  int dist[MAXN];
  int bio[MAXN];
  int cur[MAXN];
  int cookie, s, t;
  int N;

  queue<int> Q;

  bool bfs() {
    while (!Q.empty()) Q.pop();
    
    REP(i, N) dist[i] = -1;
    dist[s] = 0;
    Q.push(s);
    while (!Q.empty()) {
      int x = Q.front(); Q.pop();
      if (x == t) return true;

      REP(i, (int)E[x].size()) {
        int y = E[x][i].b;
        if (dist[y] == -1 && cap[x][i] > 0) {
          dist[y] = dist[x]+1;
          Q.push(y);
        }
      }
    }
    return false;
  }
  
  int augment(int x, int c) {
    if (x == t) return c;
    
    for (int &i = cur[x]; i < (int)E[x].size(); ++i) {
      int y = E[x][i].b;
      if (cap[x][i] > 0 && dist[y] == dist[x]+1) {
        int v = augment(y, min(c, cap[x][i]));
        if (v > 0) { 
          cap[x][i] -= v;
          cap[y][E[x][i].d] += v;
          return v;
        }
      }
    }
    return 0;
  }
  
  
  void add_edge(int a, int b, int cab, int cba) {
    E[a].push_back(edge(b, E[b].size()));
    E[b].push_back(edge(a, E[a].size()-1));
    cap[a].push_back(cab);
    cap[b].push_back(cba);
  }
  
  llint solve(int S, int T) {
    s = S, t = T;
    llint ans = 0;
    while (bfs()) {
      int f;
      REP(i, N) cur[i] = 0;
      while ((f = augment(s, inf))) ans += f;
    }
    return ans;
  }

  void init(int n) {
    N = n;
    REP(i, n) E[i].clear(), cap[i].clear();
  }
};

const int MAX = 50000;
const int inf = 1e9;

vector<int> v[MAX];
bool bio[2][MAX];

map<string, int> M;

vector<int> read_sentence() {
  static char buff[1000000];
  scanf(" %[^\n]s", buff);
  stringstream ss(buff);

  vector<int> v;
  string s;
  while (ss >> s) {
    if (!M.count(s)) {
      int idx = M.size();
      M[s] = idx;
    }
    v.push_back(M[s]);
  }
  return v;
}

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {

    int n;
    scanf("%d", &n);
    M.clear();
    REP(i, n) v[i] = read_sentence();

    int m = M.size();
    int cnt = 2*m;
    int s = cnt++;
    int t = cnt++;


    maxflow::init(cnt);
    FOR(i, 2, n)
      for (int x: v[i])
        for (int y: v[i])
          maxflow::add_edge(x, m+y, maxflow::inf, 0);
    REP(j, m) maxflow::add_edge(j, m + j, maxflow::inf, 0);

    REP(i, 2) REP(j, m) bio[i][j] = false;
    REP(i, 2) for (int x: v[i]) bio[i][x] = true;

    int ans = 0;
    REP(j, m) {
      if (bio[0][j]) ans++;
      maxflow::add_edge(s, j, !bio[0][j], 0);
      if (bio[1][j]) ans++;
      maxflow::add_edge(m+j, t, !bio[1][j], 0);
    }

    ans += maxflow::solve(s, t);
    ans -= m;

    printf("Case #%d: ", tp);
    printf("%d\n", ans);
  }
  return 0;
}
