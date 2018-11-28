#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

#define pb push_back
#define mp make_pair
//#define TASKNAME ""

#ifdef DEBUG
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...)
#endif

#define TIMESTAMP(x) eprintf("[" #x "] Time = %.3lfs\n",clock()*1.0/CLOCKS_PER_SEC)

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

#define sz(x) ((int)(x).size())
#define forn(i, n) for (int i = 0; i < (n); i++)

using namespace std;

typedef long double ld;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;
typedef pair <ll, ll> pll;
typedef vector<pii> vpii;

const int inf = 1e9;
const double eps = 1e-7;
const int INF = inf;
const double EPS = eps;

#ifdef DEBUG
struct __timestamper {
	~__timestamper(){
		TIMESTAMP(end);
	}
} __Timestamper;
#else
struct __timestamper {};
#endif

/*Template end*/

class Solver {
  struct Edge {
    int to, ne, w;
  };
  vector<Edge> es;
  vi firs;

  vb was;
  int en;
  bool dfs(int v) {
    if (v == en) return true;
    if (was[v]) return false;
    was[v] = true;
    for (int i = firs[v]; i >= 0; i = es[i].ne) if (es[i].w > 0) {
      if (dfs(es[i].to)) {
        es[i].w--;
        es[i ^ 1].w++;
        return true;
      }
    }
    return false;
  }

public:
  Solver(int n) : es(), firs(n, -1) {}
  void adde(int a, int b, int w) {
    assert(0 <= a && a < sz(firs));
    assert(0 <= b && b < sz(firs));
    es.pb({ b, firs[a], w }); firs[a] = sz(es) - 1;
    es.pb({ a, firs[b], 0 }); firs[b] = sz(es) - 1;
//    eprintf("%d-->%d (%d)\n", a, b, w);
  }
  int solve(int st, int _en) {
    en = _en;
//    eprintf("%d %d\n", st, en);
    int res = 0;
    was = vb(sz(firs), false);
    for (;;) {
      fill(was.begin(), was.end(), false);
      if (dfs(st)) res++;
      else break;
    }
    return res;
  }
};

const int FINF = 2000;

void solve() {
  int n;
  scanf("%d", &n);
  static char buf[int(1e5)];
  fgets(buf, sizeof buf, stdin);

  map<string, int> ids;
  int m = 0;

  vvi ss(n);
  forn (i, n) {
    fgets(buf, sizeof buf, stdin);
    stringstream s;
    s << buf;
    string w;
    while (s >> w) {
      if (!ids.count(w)) {
        ids[w] = m++;
      }
      ss[i].pb(ids[w]);
    }
  }

  Solver s(2 * m + n);
  forn (i, m) {
    s.adde(i, m + i, +1);
  }
  forn (i, n)
  for (int w : ss[i]) {
    s.adde(2 * m + i, w, FINF);
    s.adde(m + w, 2 * m + i, FINF);
  }
  int ans = s.solve(2 * m + 0, 2 * m + 1);
  printf("%d\n", ans);
}

bool endsWith(string a, string b) {
  return a.length() >= b.length() && string(a, a.length() - b.length()) == b;
}

int main(int argc, char *argv[]) {
  {
    string fn = "";
    if (argc >= 2) fn = argv[1];
    if (endsWith(fn, ".in")) fn = string(fn, 0, fn.length() - 3);
    freopen((fn + ".in").c_str(), "r", stdin);
    freopen((fn + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    eprintf("Case #%d:\n", TN);
    printf("Case #%d: ", TN);
    try {
      solve();
    } catch (...) {
      eprintf("Caught exception at test case #%d\n", TN);
      return 1;
    }
  }
  return 0;
}
