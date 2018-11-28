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

vi c(10);

void add(ll x) {
  while (x) {
    c[x%10] = 1;
    x /= 10;
  }
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    ll n;
    cin >> n;
    if (n == 0) {
      printf("INSOMNIA\n");
      continue;
    }
    c.assign(10, 0);
    for (int i = 1; ; ++i) {
      add(n*i);
      //if (i < 10) {for (int j = 0; j < 10; ++j) cerr << c[j]; cerr << endl;}
      if (c == vi(10, 1)) {
        printf("%lld\n", i*n);
        break;
      }
    }
  }
  return 0;
}
