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

void myexit(int res, int n) {
  printf("Case #%d: %d\n", n, res);
}

int main() {
#ifdef ROMCHELA
  freopen("4.in", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int T;
  scanf("%d\n", &T);
  for (int ntest = 1; ntest <= T; ntest++) {
    string s;
    getline(cin, s);
    int ans = 0;
    int pos = sz(s) - 1;
    while (true) {
      while (pos >= 0 && s[pos] == '+') pos--;
      for (int i = 0; i <= pos; i++) {
        if (s[i] == '+') s[i] = '-';
        else s[i] = '+';
      }
      if (pos < 0) break;
      ans++;
    }
    myexit(ans, ntest);
  }

#ifdef ROMCHELA
  cerr << "\nTIME ELAPSED: " << 1. * clock() / CLOCKS_PER_SEC << " sec\n";
#endif
  return 0;
}
