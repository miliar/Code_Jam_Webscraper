#include <bits/stdc++.h>

using namespace std;

typedef long double ld;
typedef long long ll;

long long rdtsc() {
  long long tmp;
  asm("rdtsc" : "=A"(tmp));
  return tmp;
}

inline int myrand() {
#ifdef _WIN32
  return abs((rand() << 15) ^ rand());
#else
  return rand();
#endif
}

inline int rnd(int x) {
  return myrand() % x;
}

#ifdef LOCAL
#define LLD "%lld"
#else
#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
#endif

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stdout)
#else
#define eprintf(...) ;
#endif

#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define TASK "text"

void precalc() {
}

const int maxn = 210;

int n, k;
ld p[maxn];

bool read() {
  if (scanf("%d%d", &n, &k) < 2) {
    return false;
  }
  for (int i = 0; i < n; ++i) {
    double tmp;
    scanf("%lf", &tmp);
    p[i] = tmp;
  }
  return true;
}

ld dp[maxn][maxn];
ld q[maxn];

ld calcdp(int n) {
  for (int i = 0; i <= n; ++i) {
    for (int j = 0; j <= n; ++j) {
      dp[i][j] = 0;
    }
  }
  dp[0][0] = 1;

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j <= n; ++j) {
      dp[i + 1][j] += dp[i][j] * ((ld) 1 - q[i]);
      dp[i + 1][j + 1] += dp[i][j] * q[i];
    }
  }

  return dp[n][n / 2];
}

void solve() {
  assert(k % 2 == 0);

  sort(p, p + n);

  ld res = 0;

  for (int a = 0; a <= k; ++a) {
    for (int b = 0; a + b <= k; ++b) {
      int c = k - a - b;
      for (int l = a; l + b <= n - c; ++l) {
        for (int i = 0; i < k; ++i) {
          if (i < a) {
            q[i] = p[i];
          } else if (i < a + b) {
            q[i] = p[l + (i - a)];
          } else {
            q[i] = p[n - c + (i - a - b)];
          }
        }
        res = max(res, calcdp(k));
      }
    }
  }

  printf("%.18f\n", (double) res);
}

int main() {
  srand(rdtsc());
  precalc();
#ifdef LOCAL 
  assert(freopen(TASK".out", "w", stdout));
  assert(freopen(TASK".in", "r", stdin));
#endif

  int T;
  scanf("%d", &T);
  for (int tn = 1; tn <= T; ++tn) {
    assert(read());
    printf("Case #%d: ", tn);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}


