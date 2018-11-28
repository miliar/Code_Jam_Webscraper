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

void solve() {
  int h, w;
  scanf("%d%d", &h, &w);
  vector<string> f(h);
  forn (y, h) {
    static char buf[110];
    scanf("%s", buf);
    f[y] = buf;
  }

  const int dx[] = { 1, 0, -1, 0 };
  const int dy[] = { 0, 1, 0, -1 };
  const char *dc = ">v<^";

  int ans = 0;
  forn (y, h)
  forn (x, w)
    if (f[y][x] != '.') {
      int good = 0;
      forn (d, 4) {
        int cx = x, cy = y;
        bool fini = false;
        for (;;) {
          cx += dx[d];
          cy += dy[d];
          if (cx < 0 || cx >= w || cy < 0 || cy >= h) break;
          if (f[cy][cx] != '.') {
            fini = true;
            break;
          }
        }
        if (fini) good |= 1 << d;
      }
      if (!good) {
        printf("IMPOSSIBLE\n");
        return;
      }
      int cdir = strchr(dc, f[y][x]) - dc;
      if (!(good & (1 << cdir))) {
        ans++;
      }
    }
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
