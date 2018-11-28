#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d:\n", test);
    int n,k;
    cin >> n >> k;
    int cnt = 0;
    for (int mask = 0; cnt < k && mask < (1 << (n-2)); ++mask) {
      vi v(n, 1);
      for (int i = 0; i < n-2; ++i) if (!(mask & (1 << i))) {
        v[1+i] = 0;
      }
      bool ok = 1;
      vl out;
      for (int b = 2; b <= 10; ++b) {
        ll x = 0;
        for (int i = 0; i < n; ++i) {
          x = x * b + v[i];
        }
        ll d = 1;
        for (ll i = 2; i * i <= x; ++i) if (x % i == 0) {
          d = i;
          break;
        }
        if (d == 1) {
          ok = 0;
          break;
        }
        out.push_back(d);
      }
      if (ok) {
        ++cnt;
        for (int i = 0; i < n; ++i) printf("%d", v[i]);
        for (ll x : out) printf(" %lld", x);
        printf("\n");
      }
    }
  }
  return 0;
}
