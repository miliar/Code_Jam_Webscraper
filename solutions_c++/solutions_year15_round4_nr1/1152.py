#include <iostream>
#include <fstream>
#include <sstream>

#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <algorithm>
#include <bitset>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i< int(n); i++)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; i--)
#define foreach(it, a) for(__typeof((a).begin()) it = a.begin(); it != a.end(); it++)

template<typename X> X abs(X a) { if (a < 0) return -a; return a; }
template<typename X> X sqr(X a) { return a * a; }
template<typename X> bool hasbit(X mask, int pos) { return (mask >> pos) & 1; }

#define sz(a) int((a).size())
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
#define ft first
#define sc second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1000000000;
const ld EPS = 1e-9;
const ld PI = ld(3.1415926535897932384626433832795);

using namespace std;

int r, c;
char fs[105][105];
inline bool read(){
  if (scanf("%d %d\n", &r, &c) != 2)
    return false;
  forn(i, r) {
    scanf("%s\n", fs[i]);
  }
  return true;
}

struct edge
{
  int to;
  int flow, cap;
  int cost;

  edge() {}
  edge(int _to, int _cap, int _cost) {
    to = _to;
    cap = _cap;
    cost = _cost;
    flow = 0;
  }
};

inline bool correct(int x, int y) {
  return x >= 0 && y >= 0 && x < r && y < c;
}

const int N = 100 * 100 * 3;
const int M = 100 * 100 * 32;
int sze = 0;
edge e[M];

vector<int> g[N];

inline void add_edge(int v, int to, int cap, int cost)
{
  g[v].pb(sze);
  e[sze++] = edge(to, cap, cost);

  g[to].pb(sze);
  e[sze++] = edge(v, 0, -cost);
}

int q[M];
char inQ[N];
int d[N];
int p[N], pe[N];

int flow, cost;

inline bool enlarge(int s, int t)
{
  int head, tail;
  head = tail = 0;
  forn (i, N)
  {
    d[i] = INF;
    inQ[i] = 0;
  }

  d[s] = 0;
  inQ[s] = 1;
  q[tail++] = s;

  while (head != tail)
  {
    int v = q[head++];
    inQ[v] = 0;

    if (head == M)
      head = 0;

    forn (i, sz(g[v]))
    {
      int id = g[v][i];

      if (e[id].flow >= e[id].cap)
        continue;

      int to = e[id].to;

      if (d[to] > d[v] + e[id].cost)
      {
        d[to] = d[v] + e[id].cost;
        p[to] = v;
        pe[to] = id;

        if (!inQ[to])
        {
          inQ[to] = 1;
          q[tail++] = to;

          if (tail == M)
            tail = 0;
        }
      }
    }
  }

  if (d[t] == INF)
    return false;

  int addFlow = INF;

  for (int v = t; v != s; v = p[v])
  {
    int id = pe[v];

    addFlow = min(addFlow, e[id].cap - e[id].flow);
  }

  flow += addFlow;

  for (int v = t; v != s; v = p[v])
  {
    int id = pe[v];

    e[id].flow += addFlow;
    e[id ^ 1].flow -= addFlow;
  }

  cost += d[t] * addFlow;

  return true;
}

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int ch[] = {'>', '<', 'v', '^'};

inline void solve() {
  forn(i, N) g[i].clear();
  int s = 0;
  int t = 2 * r * c + 1;
  flow = 0;
  cost = 0;
  sze = 0;
  int cnt = 0;
  forn(i, r) 
  {
    forn(j, c) 
    {
      if (fs[i][j] == '.') continue;
      add_edge(s, i * c + j + 1, 1, 0);
      cnt++;
      forn(dir, 4) 
      {
        int nx = i;
        int ny = j;

        while (correct(nx + dx[dir], ny + dy[dir])) {
          nx += dx[dir];
          ny += dy[dir];
          if (fs[nx][ny] == '.') continue;
          add_edge(i * c + j + 1, r * c + nx * c + ny + 1, 1, ch[dir] != fs[i][j]);
          break;
        }
      }
      add_edge(r * c + i * c + j + 1, t, 4, 0);
    }
  }
  while (enlarge(s, t));
  if (flow != cnt) {
    puts("impossible");
  } else {
    printf("%d\n", cost);
  }
}

int main() {
#ifdef gridnevvvit
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif
  int testcount;
  scanf("%d\n", &testcount);
  forn(test, testcount) {
    assert(read());
    cerr << "solved " << test << endl;
    printf("Case #%d: ", test + 1);
    solve();
  }
}
