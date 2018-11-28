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

const int maxn = 13;
string dp[maxn][3];

void precalc() {
  dp[0][0] = "R";
  dp[0][1] = "P";
  dp[0][2] = "S";
  for (int it = 1; it < maxn; ++it) {
    for (int i = 0; i < 3; ++i) {
      string &a = dp[it - 1][i], &b = dp[it - 1][(i + 1) % 3];
      if (a < b) {
        dp[it][i] = a + b;
      } else {
        dp[it][i] = b + a;
      }
    }
  }
}

int n;
int cnt[3];

int read() {
  if (scanf("%d", &n) < 1) {
    return 0;
  }
  assert(n < maxn);
  for (int i = 0; i < 3; ++i) {
    scanf("%d", &cnt[i]);
  }
  return 1;
}

void solve() {
  string res = "";
  for (int i = 0; i < 3; ++i) {
    bool ok = 1;
    for (int j = 0; j < 3; ++j) {
      if (count(dp[n][i].begin(), dp[n][i].end(), dp[0][j][0]) != cnt[j]) {
        ok = 0;
        break;
      }
    }
    if (ok) {
      string &cur = dp[n][i];
      if (!sz(res) || res > cur) {
        res = cur;
      }
    }
  }
  if (sz(res)) {
    printf("%s\n", res.c_str());
  } else {
    printf("IMPOSSIBLE\n");
  }
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
