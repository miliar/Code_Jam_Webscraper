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

typedef pair<int, int> qt;

qt mul(qt a, qt b) {
  const int tbl[4][4] = {
    {0, 1, 2, 3},
    {1, 0, 3, 2},
    {2, 3, 0, 1},
    {3, 2, 1, 0},
  };
  const int sgn[4][4] = {
    {0, 0, 0, 0},
    {0, 1, 0, 1},
    {0, 1, 1, 0},
    {0, 0, 1, 1},
  };
  return qt(a.first ^ b.first ^ sgn[a.second][b.second], tbl[a.second][b.second]);
}

char S[10050];
qt Q[10050];

void solve() {
  Int L = in();
  Int X = lin();
  scanf("%s", S);

  qt seg(0, 0);
  for (int i = 0; i < L; ++i) {
    Q[i] = qt(0, S[i] - 'i' + 1);
    seg = mul(seg, Q[i]);
  }

  qt whole(0, 0);
  for (int i = 0; i < X % 4; ++i) {
    whole = mul(whole, seg);
  }

  bool ok = false;
  for (int is = 0; is < 2; ++is) {
    for (int ks = 0; ks < 2; ++ks) {
      int js = is ^ ks;
      if (mul(mul(qt(is, 1), whole), qt(ks, 3)) != qt(js, 2)) {
        continue;
      }

      Int min_i = INFLL, max_k = -INFLL;
      qt ii(0, 0), kk(0, 0);
      for (Int i = 0; i < min(4 * L, X * L); ++i) {
        ii = mul(ii, Q[i % L]);
        if (ii == qt(is, 1)) {
          min_i = i;
          break;
        }
      }
      for (Int i = 0; i < min(4 * L, X * L); ++i) {
        kk = mul(Q[L - 1 - (i % L)], kk);
        if (kk == qt(ks, 3)) {
          max_k = X * L - 1 - i;
          break;
        }
      }

      ok |= max_k > min_i + 1;
    }
  }

  puts(ok ? "YES" : "NO");
}

int main() {
  int TC = in();

  for (int CN = 1; CN <= TC; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
