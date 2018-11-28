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

const int maxn = 200 + 10;
int n, k;

ld a[maxn];

int read() {
  if (scanf("%d%d", &n, &k) < 2) {
    return 0;
  }
  assert(n < maxn);
  for (int i = 0; i < n; ++i) {
    double x;
    scanf("%lf", &x);
    a[i] = x;
  }
  return 1;
}

ld b[maxn];

ld dp[maxn];
ld solve(int n) {
  for (int i = 0; i <= n; ++i) {
    dp[i] = 0;
  }
  dp[0] = 1;
  for (int i = 0; i < n; ++i) {
    for (int j = n; j >= 0; --j) {
      dp[j + 1] += dp[j] * b[i];
      dp[j] *= (1 - b[i]);
    }
  }
  return dp[n / 2];
}

void solve() {
  sort(a, a + n);
  ld res = 0;
  for (int pref = 0; pref <= k; ++pref) {
    for (int i = 0; i < pref; ++i) {
      b[i] = a[i];
    }
    for (int i = 0; i < k - pref; ++i) {
      b[pref + i] = a[n - 1 - i];
    }
    res = max(res, solve(k));
  }
  printf("%.18f\n", (double) res);
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
