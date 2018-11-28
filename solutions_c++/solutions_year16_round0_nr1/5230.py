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
#ifdef ROMCHELA
  freopen("2.in", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    ll n;
    cin >> n;
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", i);
      continue;
    }
    ll cur = n;
    ll t = 1;
    int cnt = 0;
    vector<bool> used(10, 0);
    while (cnt != 10) {
      ll c = cur * t;
      while (c) {
        used[c % 10] = 1;
        c /= 10;
      }
      cnt = 0;
      for (int i = 0; i < 10; i++)
        cnt += used[i];
      t++;
    }

    printf("Case #%d: %lld\n", i, cur * (t - 1));
  }

#ifdef ROMCHELA
  cerr << "\nTIME ELAPSED: " << 1. * clock() / CLOCKS_PER_SEC << " sec\n";
#endif
  return 0;
}
