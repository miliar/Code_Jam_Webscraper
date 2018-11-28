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

const int maxn = 200;

int r, c;
int p[maxn];

bool read() {
  if (scanf("%d%d", &r, &c) < 2) {
    return false;
  }
  for (int i = 0; i < 2 * (r + c); ++i) {
    scanf("%d", &p[i]);
    --p[i];
  }
  return true;
}

int cx[maxn];
int cy[maxn];

char a[maxn][maxn];

const int dx[] = { 0, 1, 0,-1};
const int dy[] = { 1, 0,-1, 0};

bool inside(int x, int y) {
  return 1 <= x && x <= r && 1 <= y && y <= c;
}

pair<int, int> dfs(int x, int y, int d) {
  if (!inside(x, y)) {
    return mp(x, y);
  }
  if (a[x][y] == '/') {
    if (d == 0) {
      return dfs(x - 1, y, 3);
    } else if (d == 1) {
      return dfs(x, y - 1, 2);
    } else if (d == 2) {
      return dfs(x + 1, y, 1);
    } else {
      assert(d == 3);
      return dfs(x, y + 1, 0);
    }
  } else {
    assert(a[x][y] == '\\');
    if (d == 0) {
      return dfs(x + 1, y, 1);
    } else if (d == 1) {
      return dfs(x, y + 1, 0);
    } else if (d == 2) {
      return dfs(x - 1, y, 3);
    } else {
      assert(d == 3);
      return dfs(x, y - 1, 2);
    }
  }
}

bool check() {
  for (int i = 0; i < 2 * (r + c); i += 2) {
    int sx = cx[p[i]], sy = cy[p[i]];
    pair<int, int> f = mp(cx[p[i + 1]], cy[p[i + 1]]);

    pair<int, int> rf;
    if (sx == 0) {
      rf = dfs(sx + 1, sy, 1);
    } else if (sx == r + 1) {
      rf = dfs(sx - 1, sy, 3);
    } else if (sy == 0) {
      rf = dfs(sx, sy + 1, 0);
    } else {
      assert(sy == c + 1);
      rf = dfs(sx, sy - 1, 2);
    }

    if (rf != f) {
      return false;
    }
  }

  for (int i = 1; i <= r; ++i) {
    printf("%s\n", a[i] + 1);
  }

  return true;
}

bool gen(int x, int y) {
  if (y == c + 1) {
    return gen(x + 1, 1);
  }
  if (x == r + 1) {
    return check();
  }
  a[x][y] = '/';
  if (gen(x, y + 1)) {
    return true;
  }
  a[x][y] = '\\';
  if (gen(x, y + 1)) {
    return true;
  }
  return false;
}

void solve() {
  {
    int cnt = 0;
    for (int j = 1; j <= c; ++j) {
      cx[cnt] = 0, cy[cnt] = j;
      ++cnt;
    }
    for (int i = 1; i <= r; ++i) {
      cx[cnt] = i, cy[cnt] = c + 1;
      ++cnt;
    }
    for (int j = c; j >= 1; --j) {
      cx[cnt] = r + 1, cy[cnt] = j;
      ++cnt;
    }
    for (int i = r; i >= 1; --i) {
      cx[cnt] = i, cy[cnt] = 0;
      ++cnt;
    }
  }

  memset(a, 0, sizeof(a));
  if (!gen(1, 1)) {
    printf("IMPOSSIBLE\n");
  }
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
    printf("Case #%d:\n", tn);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}


