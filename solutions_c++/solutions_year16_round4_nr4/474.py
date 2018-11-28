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

const int N = 5;

int n;
string can[N];

bool test(int m, int x) {
  return (m >> x) & 1;
}

bool searchBad(int x, int pv, int msk, int taken) {
  if (x == pv) {
    return searchBad(x + 1, pv, msk, taken);
  }
  if (x == n) {
    bool any = false;
    for (int i = 0; i < n; i++) {
      if (!test(taken, i) && test(msk, pv * n + i)) {
        any = true;
      }
    }
    return !any;
  }
  bool hadTurn = false;
  for (int i = 0; i < n; i++) {
    if (!test(taken, i) && test(msk, x * n + i)) {
      hadTurn = true;
      if (searchBad(x + 1, pv, msk, taken | (1 << i)))
        return true;
    }
  }
  if (!hadTurn) {
    return true;
  }
  return false;
}

void solve() {
  n = read();
  for (int i = 0; i < n; i++) {
    cin >> can[i];
  }
  int nn = n * n;
  int ans = inf;
  for (int msk = 0; msk < (1 << nn); msk++) {
    bool bad = false;
    int cost = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int id = i * n + j;
        if (can[i][j] == '1' && test(msk, id) == 0) {
          bad = true;
        }
        if (can[i][j] == '0' && test(msk, id) == 1) {
          cost += 1;
        }
      }
    }
    for (int pv = 0; pv < n; pv++) {
      if (searchBad(0, pv, msk, 0)) {
        bad = true;
      }
    }
    if (!bad) {
      umin(ans, cost);
    }
  }
  printf("%d\n", ans);
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
    printf("Case #%d: ", i);
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