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

const int MOD = int(1e9) + 7;
void madd(int &a, int b) { if ((a += b) >= MOD) a -= MOD; }
int mmul(int a, int b) { return ll(a) * b % MOD; }

int h, w;
vvi f;

set<vvi> ans;

bool precheck() {
  forn (y, h)
  forn (x, w) if (f[y][x] >= 0) {
    int same = 0, cadd = 0;
    if (y > 0) same += f[y][x] == f[y - 1][x], cadd += f[y - 1][x] < 0;
    if (y + 1 < h) same += f[y][x] == f[y + 1][x], cadd += f[y + 1][x] < 0;
    same += f[y][x] == f[y][(x + 1) % w], cadd += f[y][(x + 1) % w] < 0;
    same += f[y][x] == f[y][(x + w - 1) % w], cadd += f[y][(x + w - 1) % w] < 0;
    if (same > f[y][x]) return false;
    if (same + cadd < f[y][x]) return false;
  }
  return true;
}

void check() {
  forn (y, h)
  forn (x, w) {
    int same = 0;
    if (y > 0) same += f[y][x] == f[y - 1][x];
    if (y + 1 < h) same += f[y][x] == f[y + 1][x];
    same += f[y][x] == f[y][(x + 1) % w];
    same += f[y][x] == f[y][(x + w - 1) % w];
    if (same != f[y][x]) return;
  }

  vvi minv = f;
  forn (i, w) {
    forn (y, h)
      rotate(f[y].begin(), f[y].begin() + 1, f[y].end());
    minv = min(minv, f);
  }
  if (!ans.count(minv)) {
    forn (y, h) {
      forn (x, w)
        eprintf("%d", f[y][x]);
      eprintf("\n");
    }
    eprintf("\n");
  }
  ans.insert(minv);
}

void go(int y, int x) {
  if (x >= w) return go(y + 1, 0);
  if (y >= h) return check();
  if (!precheck()) return;
  for (int i = 1; i <= 3; i++) {
    f[y][x] = i;
    go(y, x + 1);
    f[y][x] = -1;
  }
}

void solve() {
  scanf("%d%d", &h, &w);
  ans.clear();
  f = vvi(h, vi(w, -1));
  go(0, 0);
  printf("%d\n", sz(ans));
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
