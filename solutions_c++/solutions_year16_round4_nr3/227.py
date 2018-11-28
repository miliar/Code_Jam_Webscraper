#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <cassert>
#include <iostream>
#include <cstring>
#include <cmath>

#define pb push_back
#define all(x) (x).begin(), (x).end()

#ifdef LOCAL
  #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
  #define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a < b) a = b;}
template<class T> inline void umin(T &a,T b){if(a > b) a = b;}
template<class T> inline T abs(T a){return a > 0 ? a : -a;}

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int inf = 1e9 + 143;
const ll longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int N = 512;

int r, c;
int a[N], b[N];
int cset[N];

bool test(int m, int x) {
  return (m >> x) & 1;
}

int getId(int x, int y, int t) {
  return (x * c + y) * 4 + t;
}

int p[N];

int get(int x) {
  if (x == p[x])
    return x;
  return p[x] = get(p[x]);
}

void init() {
  for (int i = 0; i < N; i++) {
    p[i] = i;
  }
}

void add(int u, int v) {
  u = get(u);
  v = get(v);
  if (u != v) {
    p[u] = v;
  }
}

void output(int msk) {
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      int id = i * c + j;
      if (test(msk, id) == 0) {
        printf("\\");
      } else {
        printf("/");
      }
    }
    printf("\n");
  }
}

void solve() {
  r = read();
  c = read();
  for (int i = 0; i < r + c; i++) {
    a[i] = read() - 1;
    b[i] = read() - 1;
  }
  int rc = r * c;
  for (int msk = 0; msk < (1 << rc); msk++) {
    init();
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (i > 0) {
          add(getId(i - 1, j, 2), getId(i, j, 0));
        }
        if (j > 0) {
          add(getId(i, j - 1, 1), getId(i, j, 3));
        }
        int cellId = i * c + j;
        if (test(msk, cellId) == 0) { // '\'
          add(getId(i, j, 0), getId(i, j, 1));
          add(getId(i, j, 2), getId(i, j, 3));
        } else {
          add(getId(i, j, 0), getId(i, j, 3));
          add(getId(i, j, 2), getId(i, j, 1));  
        }
      }
    }
    for (int i = 0; i < c; i++) {
      cset[i] = get(getId(0, i, 0));
      cset[i + r + c] = get(getId(r - 1, c - i - 1, 2));
    }
    for (int i = 0; i < r; i++) {
      cset[i + c] = get(getId(i, c - 1, 1));
      cset[i + r + 2 * c] = get(getId(r - i - 1, 0, 3));
    }
    bool bad = false;
    for (int i = 0; i < r + c; i++) {
      if (cset[a[i]] != cset[b[i]]) {
        bad = true;
      }
    }
    if (!bad) {
      output(msk);
      return;
    }
  }
  puts("IMPOSSIBLE");
}

void preCalc() {
}

int main() {
  preCalc();
  
  int numTestCases = read();
  int fromTest = 0;
  int toTest = int(1e9);
  
  #ifdef PART
    fromTest = FROM
    toTest = TO
  #endif
  
  for (int i = 1; i <= numTestCases; i++) {
    printf("Case #%d:\n", i);
    //readInput();
    if (i >= fromTest && i <= toTest) {
      solve();
      eprintf("Test %d is done..\n", i);
      fflush(stderr);
      fflush(stdout);  
    }
  }

  return 0;  
}