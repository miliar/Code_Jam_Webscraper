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

//const int inf = 1e9;
const double eps = 1e-7;
//const int INF = inf;
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

const int MAXH = 10;
const int MAXW = 10;
int f[MAXH][MAXW];
int h, w;
bool was[MAXH][MAXW];

int dfs(int x, int y) {
  if (x < 0 || y < 0 || x >= w || y >= h) return 0;

  if (was[y][x]) return 0;
  was[y][x] = true;
  int res = 1;
  if (f[y][x]) return res;

  for (int dy = -1; dy <= 1; dy++)
  for (int dx = -1; dx <= 1; dx++)
    res += dfs(x + dx, y + dy);
  return res;
}

void solve() {
  int cnt;
  scanf("%d%d%d", &h, &w, &cnt);
  for (int msk = 0; msk < (1 << (h * w)); msk++) if (__builtin_popcount(msk) == cnt) {
    memset(f, 0, sizeof f);
    for (int y = 0; y < h; y++)
    for (int x = 0; x < w; x++) {
      for (int dx = -1; dx <= 1; dx++)
      for (int dy = -1; dy <= 1; dy++) {
        int nx = x + dx, ny = y + dy;
        if (nx < 0 || ny < 0 || nx >= w || ny >= h) continue;
        if (msk & (1 << (ny * w + nx)))
          f[y][x]++;
      }
    }
    for (int y = 0; y < h; y++)
    for (int x = 0; x < w; x++) if (!(msk & (1 << (y * w + x)))) {
      memset(was, 0, sizeof was);
      int dep = dfs(x, y);
      if (dep + cnt == h * w) {
        for (int cy = 0; cy < h; cy++) {
          for (int cx = 0; cx < w; cx++) {
            char c = '.';
            if (msk & (1 << (cy * w + cx))) c = '*';
            if (y == cy && x == cx) c = 'c';
            printf("%c", c);
          }
          printf("\n");
        }
        return;
      }
    }
  }
  printf("Impossible\n");
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
    printf("Case #%d:\n", TN);
    try {
      solve();
    } catch (...) {
      eprintf("Caught exception at test case #%d\n", TN);
      return 1;
    }
  }
  return 0;
}
