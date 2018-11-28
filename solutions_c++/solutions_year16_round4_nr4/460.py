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

const int inf = 1.01e9;

void precalc() {
}

const int maxn = 30;

int n;
int a[maxn][maxn];

bool read() {
  if (scanf("%d", &n) < 1) {
    return false;
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      char ch;
      scanf(" %c", &ch);
      a[i][j] = (ch == '1');
    }
  }
  return true;
}

int p[maxn];
bool used[maxn];

bool cool(int i) {
  if (i == n) {
    return true;
  }
  int v = p[i];
  bool fnd = false;
  for (int j = 0; j < n; ++j) {
    if (used[j] || !a[v][j]) {
      continue;
    }
    fnd = true;
    used[j] = true;
    if (!cool(i + 1)) {
      return false;
    }
    used[j] = false;
  }
  return fnd;
}

bool good() {
  memset(used, 0, sizeof(used));
  for (int i = 0; i < n; ++i) {
    p[i] = i;
  }
  do {
    if (!cool(0)) {
      return false;
    }
  } while (next_permutation(p, p + n));
  return true;
}

int gen(int i, int j, int k) {
  if (j == n) {
    return gen(i + 1, 0, k);
  }
  if (i == n) {
    return (good() ? k : inf);
  }

  if (a[i][j] == 1) {
    return gen(i, j + 1, k);
  }

  a[i][j] = 1;
  int res = gen(i, j + 1, k + 1);
  a[i][j] = 0;
  res = min(res, gen(i, j + 1, k));

  return res;
}

void solve() {
  printf("%d\n", gen(0, 0, 0));
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


