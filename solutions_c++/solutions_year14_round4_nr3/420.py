#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <functional>
#include <bitset>
#include <deque>
#include <tuple>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef pair<int, int> pii;

#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define FORD(i, x, y) for (ll i = x; i >= y; --i)
#define REP(i, n) for(ll i=0; i<n; i++)
#define REPD(i, n) for(ll i = n - 1; i >= 0; --i) 

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define UNIQ(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define SZ(c) (int)(c).size()
#define CONTAINS(s,obj) (s.find(obj)!=s.end())

#define CLEAR(x) memset(x,0,sizeof x)
#define COPY(from,to) memcpy(to, from, sizeof to)

#define sq(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second

const double eps = 1.0e-11;
const double pi = acos(-1.0);

class MinCoasMaxFlow {
  static const int INF = 1000000000;
  int n;
  struct edge {
    int to, u, c, f;
    size_t rev;
  };
  vector<vector<edge> > g;
public:
  MinCoasMaxFlow(int size) {
    g.resize(size);
    n = size;
  }
  // from, to, cost capacity
  void AddEdge(int a, int b, int u, int c) {
    cerr << a << " " << b << endl;
    edge e1 = {b, u, c, 0, SZ(g[b])};
    edge e2 = {a, 0, -c, 0, SZ(g[a])};
    g[a].push_back(e1);
    g[b].push_back(e2);
  }
  pii Calculate(int s, int t, const int max_flow = INF) {
    int flow = 0, cost = 0;
    // max flow we know, or specify as INF
    while(flow < max_flow) {
      vector<int> col(n, 0);
      vector<int> d(n, INF);
      deque<int> q;
      vector<pii> p(n);
      q.push_back(s);
      d[s] = 0;
      while(!q.empty()) {
        int v = q.front();
        q.pop_front();
        col[v] = 2;
        REP(i, SZ(g[v])) {
          const edge& e = g[v][i];
          if (e.f < e.u && d[v] + e.c < d[e.to]) {
            d[e.to] = d[v] + e.c;
            if (col[e.to] == 0) q.push_back(e.to);
            else if (col[e.to] == 2) q.push_front(e.to);
            col[e.to] = 1;
            p[e.to] = mp(v, i);
          }
        }
      }
      if (d[t] == INF) break;
      int add = max_flow - flow;
      for (int v = t; v != s; v = p[v].first) {
        int pv = p[v].first, pr = p[v].second;
        add = min(add, g[pv][pr].u - g[pv][pr].f);
      }
      for (int v = t; v != s; v = p[v].first) {
        int pv = p[v].first, pr = p[v].second, rev = g[pv][pr].rev;
        g[pv][pr].f += add;
        g[v][rev].f -= add;
        cost += g[pv][pr].c * add;
      }
      flow += add;
    }
    return mp(flow, cost);
  }
};

const int N = 505;
int t[N][N];
int dx1[] = {0, 1, 0};
int dy1[] = {-1, 0, 1};

int dx2[] = {0, -1, 0};
int dy2[] = {1, 0, -1};


int dx3[] = {-1, 0, 1};
int dy3[] = {0, 1, 0};


int dx4[] = {1, 0, -1};
int dy4[] = {0, -1, 0};



int w, h, b;


int Get(int i, int j, int f) {
  return w * h * f + w * i + j;
}

bool ok = false;

void Go(int x, int y, int px, int py) {
  if (x < 0 || x >= h || y < 0 || y >= w || t[x][y]) return;
  t[x][y] = 1;
  if (x == h - 1) {
    ok = true;
    return;
  }

  if (x > px) {
    REP(i, 3) Go(x + dx1[i], y + dy1[i], x, y);
  }
  if (x < px) {
    REP(i, 3) Go(x + dx2[i], y + dy2[i], x, y);
  }

  if (y > py) {
    REP(i, 3) Go(x + dx3[i], y + dy3[i], x, y);
  }

  if (y < py) {
    REP(i, 3) Go(x + dx3[i], y + dy3[i], x, y);
  }

  if (!ok) t[x][y] = 0;
}

// Need an endl after output.
void solve() {
  CLEAR(t);
  cin >> w >> h >> b;
  // MinCoasMaxFlow mf(2 * w * h + 2);
  REP(i, b) {
    int x0, y0, x1, y1;
    cin >> x0 >> y0 >> x1 >> y1;
    FOR(x, x0, x1) FOR(y, y0, y1) {
      t[x][y] = 1;
    }
  }

  int res = 0;
  REP(i, w) {
    ok = false;
    Go(0, i, -1, i);
    res += ok;
  }
  cout << res << endl;
  /*REP(i, h) REP(j, w) {
    if (t[i][j]) continue;
    mf.AddEdge(Get(i, j, 0), Get(i, j, 1), 0, 1);
    REP(dir, 4) {
      int x = i + dx[dir];
      int y = j + dy[dir];
      if (x < 0 || x >= h || y < 0 || y >= w || t[x][y]) continue;
      mf.AddEdge(Get(i, j, 1), Get(x, y, 0), 0, 1);
    }
  }

  int ss = 2 * w * h;
  int tt = ss + 1;
  REP(i, w) {
    if (!t[0][i]) mf.AddEdge(ss, Get(0, i, 0), 0, 1);
    if (!t[h - 1][i]) mf.AddEdge(Get(h - 1, i, 1), tt, 0, 1);
  }
  cout << mf.Calculate(ss, tt).first << endl;*/
}

int main() {
  // freopen("c.in", "r", stdin);
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int tests;
  scanf("%d", &tests);
  REP(i, tests) {
    printf("Case #%d: ", int(i + 1));
    solve();
  }
  return 0;
}