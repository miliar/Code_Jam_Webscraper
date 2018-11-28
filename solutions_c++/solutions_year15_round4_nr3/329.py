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

const int maxs = (int) 1e3 * 12 + 100;
char s[maxs];

int n;

map<string, int> getId;
int maxid;

const int maxn = 200 + 10;
vector<int> a[maxn];

bool read() {
  if (scanf("%d ", &n) < 1) {
    return 0;
  }
  //eprintf("n = %d\n", n);
  getId.clear();
  maxid = 0;
  for (int i = 0; i < n; ++i) {
    gets(s);
    a[i].clear();
    for (int l = 0; s[l]; ++l) {
      if (isspace(s[l])) {
        continue;
      }
      int r;
      for (r = l; s[r] && !isspace(s[r]); ++r) ;
      char tmp = s[r];
      s[r] = 0;
      string cur(s + l);
      auto iter = getId.find(cur);
      int id;
      if (iter != getId.end()) {
        id = iter->second;
      } else {
        id = maxid++;
        getId[cur] = id;
      }
      a[i].pb(id);
      //eprintf(" %d(%s)", id, cur.c_str());
      s[r] = tmp;
      l = r - 1;
    }
    //eprintf("\n");
  }

  return 1;
}

const int rmaxId = maxn * 10 + (int) 1e3 * 2;
int can[rmaxId][2];

void solve() {
  int res = INF;
  for (int mask = 0; mask < (1 << (n - 2)); ++mask) {
    for (int i = 0; i < maxid; ++i) {
      can[i][0] = can[i][1] = 0;
    }
    for (int it = 0; it < n; ++it) {
      int type = (it < 2 ? it : ((mask >> (it - 2)) & 1));
      for (int j = 0; j < sz(a[it]); ++j) {
        can[a[it][j]][type] = 1;
      }
    }
    int val = 0;
    for (int i = 0; i < maxid; ++i) {
      val += (can[i][0] && can[i][1]);
    }
    res = min(res, val);
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
