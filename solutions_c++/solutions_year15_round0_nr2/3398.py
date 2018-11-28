#include <cstdio>
#include <cmath>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#define SIZE(x) ((int) (x).size())
#define REP(i, n) for (int i = 0; i < (int) (n); ++i)
#define FOR(i, a, b) for (int i = (int) (a); i <= (int) (b); ++i)
#define FORD(i, a, b) for (int i = (int) (a); i >= (int) (b); --i)
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

const int INF = 1023456789;

int solve() {
  int n;
  scanf("%d", &n);
  VI A(n);
  REP(i, n)
    scanf("%d", &A[i]);
  int m = *max_element(A.begin(), A.end());
  int res = INF;
  FOR(t, 1, m) {
    int q = 0;
    REP(i, n)
      q += (A[i] - 1) / t;
    res = min(res, q + t);
  }
  return res;
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i, 1, t) {
    printf("Case #%d: %d\n", i, solve());
  }
}
