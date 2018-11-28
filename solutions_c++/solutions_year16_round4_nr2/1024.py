#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cassert>
#include <climits>
#include <ctime>
using namespace std;

typedef long long     ll;
typedef double        dbl;

#define X             first
#define Y             second
#define mp            make_pair
#define pb            push_back
#define sz(x)         static_cast<int>((x).size())
#define all(x)        x.begin(),x.end()

#ifdef ROMCHELA
#    define D(x)          cout<<#x<<" = "<<(x)<<endl
#    define Ds()          cout<<"------------"<<endl
#    define eprintf(...)  printf(__VA_ARGS__);
#else
#    define D(c)             static_cast<void>(0)
#    define Ds(x)            static_cast<void>(0)
#    define eprintf(...)     static_cast<void>(0)
#endif

const int maxn = 1e6 + 10;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

#ifdef ROMCHELA
  freopen("3.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int T;
  scanf("%d", &T);
  for (int n_test = 1; n_test <= T; n_test++) {
    int n, k;
    scanf("%d%d", &n, &k);
    vector<dbl> p(n, 0);
    for (int i = 0; i < n; i++)
      scanf("%lf", &p[i]);
    dbl ans = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
      int cntbits = __builtin_popcount(mask);
      if (cntbits != k) continue;

      dbl curp = 0;

      for (int submask = mask; submask; submask = (submask - 1) & mask) {
        cntbits = __builtin_popcount(submask);
        if (cntbits != k / 2) continue;
        
        dbl c = 1.0;

        for (int i = 0; i < n; i++) {
          bool m1 = (mask >> i) & 1;
          bool m2 = (submask >> i) & 1;
          if (m1 && m2)
            c *= p[i];
          if (m1 && !m2)
            c *= (1.0 - p[i]); 
        }

        curp += c;
      }

      ans = max(ans, curp);
    }
    printf("Case #%d: %.10lf\n", n_test, ans);
  }

#ifdef ROMCHELA
  cerr << "\nTIME ELAPSED: " << 1. * clock() / CLOCKS_PER_SEC << " sec\n";
#endif
  return 0;
}
