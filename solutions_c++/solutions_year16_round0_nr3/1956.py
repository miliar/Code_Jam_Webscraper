#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef unsigned long long UInt;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
Int lin() { Int x; scanf("%lld", &x); return x; }

bool divisible(uint x, int base, int mo) {
  int rem = 0;
  for (int i = 31; i >= 0; --i) {
    (rem *= base) %= mo;
    if (x & (1U << i)) {
      (rem += 1) %= mo;
    }
  }
  return rem == 0;
}

void solve() {
  int N = in();
  int J = in();

  for (int a = 1; a <= N - 2; ++a) {
    for (int b = a + 1; b <= N - 2; ++b) {
      for (int c = b + 1; c <= N - 2; ++c) {
        for (int d = c + 1; d <= N - 2; ++d) {
          uint x = (1U << (N - 1)) | (1U << d) | (1U << c) | (1U << b) | (1U << a) | (1U << 0);
          bool ok = true;
          for (int e = 2; e <= 10; ++e) {
            ok &= divisible(x, e, (e == 6 ? 7 : 3 - e % 2));
          }
          if (ok) {
            for (int i = N - 1; i >= 0; --i) {
              putchar('0' + ((x >> i) & 1));
            }
            puts(" 3 2 3 2 7 2 3 2 3");
            if (--J == 0) {
              return;
            }
          }
        }
      }
    }
  }
}

int main() {
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d:\n", CN);
    solve();
  }

  return 0;
}
