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

void solve() {
  int N = in();
  int A[1024];
  for (int i = 0; i < N; ++i) {
    A[i] = in();
  }

  int B[1024];
  memcpy(B, A, sizeof(B));
  sort(B, B + N);

  int res = 0;
  for (int i = 0; i < N; ++i) {
    int u = -1;
    for (int j = 0; j < N; ++j) {
      if (A[j] == B[i]) {
        u = j;
        break;
      }
    }

    int left = 0, right = 0;
    for (int j = 0; j < N; ++j) {
      if (A[j] > B[i]) {
        if (j < u) ++left;
        else ++right;
      }
    }

    res += min(left, right);
  }

  printf("%d\n", res);
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
