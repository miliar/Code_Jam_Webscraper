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
const ld EPS = 1e-15;

void precalc() {
}

const int maxn = 100 + 10;
pair<ld, ld> ps[maxn];

int n;
ld V, X;

bool read() {
  double tmp1, tmp2;
  if (scanf("%d%lf%lf", &n, &tmp1, &tmp2) < 3) {
    return 0;
  }
  V = tmp1, X = tmp2;
  for (int i = 0; i < n; ++i) {
    double r, c;
    scanf("%lf%lf", &r, &c);
    ps[i] = mp(c, r);
  }
  return 1;
}

void solve() {
  sort(ps, ps + n);
  ld sumr = 0;
  for (int i = 0; i < n; ++i) {
    sumr += ps[i].second;
  }

  const static ld MAXRIGHT = 1e9;
  ld left = 0, right = MAXRIGHT;
  for (int iter = 0; iter < 90; ++iter) {
    ld tme = (left + right) / 2;

    if (tme * sumr < V) {
      left = tme;
      continue;
    }
    ld minSum = 0;
    {
      ld leftV = V;
      for (int i = 0; i < n; ++i) {
        ld curV = min(leftV, ps[i].second * tme);
        leftV -= curV;
        minSum += curV * ps[i].first;
      }
      //eprintf("1 %.3f\n", (double) leftV);
    }
    ld maxSum = 0;
    {
      ld leftV = V;
      for (int i = n - 1; i >= 0; --i) {
        ld curV = min(leftV, ps[i].second * tme);
        leftV -= curV;
        maxSum += curV * ps[i].first;
      }
      //eprintf("2 %.3f\n", (double) leftV);
    }
    if (minSum <= EPS + V * X && X * V <= EPS + maxSum) {
      right = tme;
    } else {
      left = tme;
    }
  }
  if (right >= MAXRIGHT - 1) {
    printf("IMPOSSIBLE\n");
  } else {
    printf("%.18f\n", (double) left);
  }
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
