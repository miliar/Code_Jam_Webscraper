#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <ctime>
#include <string>

using namespace std;

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

typedef long double ld;

long long rdtsc() {
  long long tmp;
  asm("rdtsc" : "=A"(tmp));
  return tmp;
}

inline int myrand() {
  return abs((rand() << 15) ^ rand());
}

inline int rnd(int x) {
  return myrand() % x;
}

#define pb push_back
#define mp make_pair
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())
#define TASKNAME "text"

const int INF = (int)1e9 + 1;
const ld EPS = 1e-9;

void precalc() {
}

const int maxn = 100 + 10;
char s[maxn][maxn];

int n, m;

bool read() {
  if (scanf("%d%d", &n, &m) < 2) {
    return 0;
  }

  for (int i = 0; i < n; ++i) {
    scanf("%s", s[i]);
  }
  return 1;
}

const int maxg = 4;
const int go[maxg][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
const char goch[maxg] = {'v', '>', '^', '<'};

bool ok(int x, int y) {
  return 0 <= x && x < n && 0 <= y && y < m;
}

void solve() {
  int res = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (s[i][j] == '.') {
        continue;
      }
      bool can = 0, alr = 0;
      for (int g = 0; g < 4; ++g) {
        bool val = 0;
        int x = i, y = j;
        for (int it = 0;; ++it) {
          x += go[g][0], y += go[g][1];
          if (!ok(x, y)) {
            break;
          }
          if (s[x][y] != '.') {
            val = 1;
            break;
          }
        }
        if (!val) {
          continue;
        }
        can = 1;
        if (goch[g] == s[i][j]) {
          alr = 1;
        }
      }
      if (!can) {
        printf("IMPOSSIBLE\n");
        return;
      }
      res += !alr;
    }
  }
  printf("%d\n", res);
}

int main() {
  srand(rdtsc());
#ifdef DEBUG
  freopen(TASKNAME".out", "w", stdout);
  assert(freopen(TASKNAME".in", "r", stdin));
#endif

  precalc();
  int maxt;
  while (scanf("%d", &maxt) == 1) {
    for (int t = 0; t < maxt; ++t) {
      assert(read());
      printf("Case #%d: ", t + 1);
      solve();
#ifdef DEBUG
      eprintf("%.18lf\n", (double)clock() / CLOCKS_PER_SEC);
#endif
    }
  }
  return 0;
}
