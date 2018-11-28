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

void solve() {
  int N = in();
  int P = 0;

  for (int i = 0; i < N; ++i) {
    char b[8];
    scanf("%s", b);
    for (int j = 0; j < N; ++j) {
      if (b[j] == '1') {
        P |= (1 << (i * N + j));
      }
    }
  }

  int res = 100;
  for (int Q = 0; Q < (1 << (N * N)); ++Q) {
    if ((P & Q) != P) {
      continue;
    }
    int pos[1<<4][1<<4];
    memset(pos, 0, sizeof(pos));
    pos[0][0] = 1;
    bool ok = true;
    for (int i = 0; i < (1 << N); ++i) {
      for (int j = 0; j < (1 << N); ++j) {
        if (pos[i][j]) {
          for (int k = 0; k < N; ++k) {
            if (i & (1 << k)) {
              continue;
            }
            bool ok1 = false;
            for (int u = 0; u < N; ++u) {
              if (Q & (1 << (k * N + u))) {
                if (j & (1 << u)) {
                  continue;
                }
                ok1 = true;
                pos[i | (1 << k)][j | (1 << u)] = 1;
              }
            }
            ok &= ok1;
          }
        }
      }
    }
    if (ok) {
      chmin(res, __builtin_popcount(Q) - __builtin_popcount(P));
    }
  }
  printf("%d\n", res);
}

int main() {
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
