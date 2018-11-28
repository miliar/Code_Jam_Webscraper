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

using namespace std;

typedef unsigned uint;
typedef long long Int;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }

Int A[1<<20];

void solve() {
  int N = in();
  int P = in();
  int Q = in();
  int R = in();
  int S = in();

  Int all = 0;
  for (int i = 0; i < N; ++i) {
    A[i] = ((Int)i * P + Q) % R + S;
    all += A[i];
  }

  Int lo = 0, hi = all;
  while (hi - lo > 1) {
    Int mid = (hi + lo) / 2;
    Int left = 0, right = all;
    int j = 0;
    Int ma = 0;
    bool ok = false;
    for (int rev = 0; rev < 2; ++rev) {
      ma = 0;
      for (int i = 0; i < N; ++i) {
        if (ma + A[i] > mid) {
          int j = i;
          Int m1 = 0;
          while (j < N && m1 + A[j] <= ma) {
            m1 += A[j];
            ++j;
          }
          int k = j;
          Int m2 = 0;
          while (k < N && m2 + A[k] <= ma) {
            m2 += A[k];
            ++k;
          }
          ok |= k == N;
          break;
        }
        ma += A[i];
      }
      reverse(A, A + N);
    }

    ma = 0;
    for (int i = 0; i < N; ++i) {
      while (j < N && ma + A[j] <= mid) {
        ma += A[j];
        right -= A[j];
        ++j;
      }
      if (ma >= right && ma >= left) {
        ok = true;
        break;
      }
      ma -= A[i];
      left += A[i];
    }
    if (ok) {
      hi = mid;
    } else {
      lo = mid;
    }
  }

  Int k = all - hi;
  printf("%.12f\n", (double)k / all);
}

int main()
{
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
