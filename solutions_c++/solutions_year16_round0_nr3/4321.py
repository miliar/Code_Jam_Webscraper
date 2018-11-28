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

vector<ll> getdiv(ll n) {
  vector<ll> v;
  for (ll i = 2; i < 11; i++) {
    ll res = 0;
    ll c = n;
    ll ipow = 1;
    while (c) {
      res += (c % 2) * ipow;
      c /= 2;
      ipow *= i;
    }
    //printf("%lld\n", res);
    for (ll j = 2; j * j <= res; j++) {
      if (res % j == 0) {
        v.pb(j);
        break;
      }
    }
  }
  return v;
}

int main() {
#ifdef ROMCHELA
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int T;
  scanf("%d", &T);
  int n, j;
  scanf("%d%d", &n, &j);
  n--; 
  printf("Case #1:\n");
  set<ll> S;
  while (j) {
    ll t = (1LL << n) + 1;
    int magic = rand() % 15;
    for (int i = 0; i < magic; i++) {
      int pos = rand() % (n - 2);
      t ^= (1LL << (pos + 1));
    }
    cerr << t << endl;
    if (S.count(t) != 0)
      continue;
    S.insert(t);
    vector<ll> r = getdiv(t);
    if (sz(r) == 9) {
      cerr << j << endl;
      j--;
      string s = "";
      while (t) {
        s += '0' + t%2;
        t /= 2;
      }
      reverse(all(s));
      printf("%s ", s.c_str());
      for (int i = 0; i < sz(r); i++)
        printf("%lld ", r[i]);
      puts("");
    }
  }

#ifdef ROMCHELA
  cerr << "\nTIME ELAPSED: " << 1. * clock() / CLOCKS_PER_SEC << " sec\n";
#endif
  return 0;
}
