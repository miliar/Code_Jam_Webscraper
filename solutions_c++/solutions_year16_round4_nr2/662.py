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

const int N = 22;

bool test(int m, int x) {
  return (m >> x) & 1;
}

double p[N];
double f[N], nf[N];

void solve() {
  int n = read();
  int k = read();
  for (int i = 0; i < n; i++) {
    cin >> p[i];
  }
  double ans = 0;
  for (int msk = 0; msk < (1 << n); msk++) {
    if (__builtin_popcount(msk) != k)
      continue;
    memset(f, 0, sizeof f);
    f[0] = 1;
    for (int i = 0; i < n; i++) {
      if (test(msk, i)) {
        memset(nf, 0, sizeof nf);
        for (int s = 0; s <= n; s++) {
          nf[s + 1] += f[s] * p[i];
          nf[s] += f[s] * (1.0 - p[i]);
        }    
        for (int s = 0; s <= n; s++) {
          f[s] = nf[s];
        }
      }
    }
    umax(ans, f[k / 2]);
  } 
  printf("%.10f\n", ans);
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