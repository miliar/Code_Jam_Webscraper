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

struct tap {
  double r, c;
} T[128];

double pour(int n, double t, double maxv) {
  double x = 0.0, v = 0.0;
  for (int i = 0; i < n; ++i) {
    double r = t * T[i].r;
    chmin(r, maxv - v);
    x = (v * x + r * T[i].c) / (v + r);
    v += r;
  }
  return x;
}

void solve() {
  int N = in();
  double V = fin();
  double X = fin();
  double mi = 100.0, ma = 0.0, rsum = 0.0;
  for (int i = 0; i < N; ++i) {
    T[i].r = fin();
    T[i].c = fin();
    rsum += T[i].r;
    chmin(mi, T[i].c);
    chmax(ma, T[i].c);
  }

  if (mi == X || ma == X) {
    double rs = 0.0, m = (mi == X ? mi : ma);
    for (int i = 0; i < N; ++i) {
      if (T[i].c == m) {
        rs += T[i].r;
      }
    }
    printf("%.9f\n", V / rs);
    return;
  }

  if (mi <= X && X <= ma) {
    double lo = V / rsum, hi = 1e12;
    for (int loop = 0; loop < 200; ++loop) {
      double mid = (hi + lo) / 2;
      sort(T, T + N, [] (const tap& a, const tap& b) { return a.c < b.c; });
      double xlo = pour(N, mid, V);
      reverse(T, T + N);
      double xhi = pour(N, mid, V);
      if (xlo <= X && X <= xhi) {
        hi = mid;
      } else {
        lo = mid;
      }
    }
    printf("%.9f\n", hi);
  } else {
    puts("IMPOSSIBLE");
  }
}

int main() {
  int TN = in();

  for (int CN = 1; CN <= TN; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
