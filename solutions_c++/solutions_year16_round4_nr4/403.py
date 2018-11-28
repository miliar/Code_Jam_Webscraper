#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <random>
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
#include <queue>

using namespace std;

mt19937 mrand(random_device{} ()); 

int rnd(int x) {
  return mrand() % x;
}

#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

typedef long double ld;
typedef long long ll;

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) ;
#endif

#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define TASKNAME "text"

const int inf = (int) 1.01e9;
const ld eps = 1e-9;
const ld pi = acos((ld) -1.0);

void precalc() {
}

const int maxn = 25 + 5;
char s[maxn];
int go[maxn][maxn];

int n;

int read() {
  if (scanf("%d", &n) < 1) {
    return 0;
  }
  for (int i = 0; i < n; ++i) {
    scanf("%s", s);
    for (int j = 0; j < n; ++j) {
      go[i][j] = (s[j] == '1');
    }
  }
  return 1;
}

int used1[maxn], used2[maxn];

bool check(int iter) {
  if (iter == n) {
    return 1;
  }
  for (int v = 0; v < n; ++v) {
    if (used1[v]) {
      continue;
    }
    bool was = 0;
    for (int u = 0; u < n; ++u) {
      if (used2[u] || !go[v][u]) {
        continue;
      }
      used1[v] = 1, used2[u] = 1;
      was = 1;
      if (!check(iter + 1)) {
        return 0;
      }
      used1[v] = 0, used2[u] = 0;
    }
    if (!was) {
      return 0;
    }
  }
  return 1;
}

bool check() {
  /*for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      eprintf("%d%c", go[i][j], " \n"[j == n - 1]);
    }
  }*/
  for (int i = 0; i < n; ++i) {
    used1[i] = 0;
    used2[i] = 0;
  }
  if (!check(0)) {
    return 0;
  }
  return 1;
}

int res;

void gen(int v1, int v2, int cnt) {
  if (res <= cnt) {
    return;
  }

  if (v2 == n) {
    ++v1;
    if (v1 == n) {
      if (check()) {
        res = cnt;
      }
      return;
    }
    v2 = 0;
  }

  if (!go[v1][v2]) {
    go[v1][v2] = 1;
    gen(v1, v2 + 1, cnt + 1);
    go[v1][v2] = 0;
  }
  gen(v1, v2 + 1, cnt);
}

void solve() {
  res = inf;
  gen(0, 0, 0);
  printf("%d\n", res);
}

int main() {
  precalc();
#ifdef LOCAL
  freopen(TASKNAME".out", "w", stdout);
  assert(freopen(TASKNAME".in", "r", stdin));
#endif

  int T;
  scanf("%d", &T);
  int t = 0;
  while (1) {
    if (!read()) {
      break;
    }
    printf("Case #%d: ", ++t);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}
