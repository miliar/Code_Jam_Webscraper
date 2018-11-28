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
  int D = in();
  int P[1024];
  for (int i = 0; i < D; ++i) {
    P[i] = in();
  }

  int res = INF;
  for (int r = 1; r <= 1000; ++r) {
    int cost = 0;
    for (int i = 0; i < D; ++i) {
      cost += P[i] / r;
      if (P[i] % r == 0) {
        --cost;
      }
    }
    chmin(res, cost + r);
  }
  printf("%d\n", res);
}

int main() {
  int TC = in();

  for (int CN = 1; CN <= TC; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
