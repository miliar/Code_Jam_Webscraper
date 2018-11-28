#include <cstdio>
#include <cassert>

#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x" = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 10100;

int N, X;
int size[MAX];

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    scanf("%d%d", &N, &X);

    REP(i, N) scanf("%d", size+i);
    sort(size, size + N);

    int cnt = 0;

    int lo = 0, hi = N-1;
    while (lo < hi) {
      if (size[lo] + size[hi] <= X) {
        ++lo;
        --hi;
      } else {
        --hi;
      }
      ++cnt;
    }

    if (lo == hi) ++cnt;
    printf("Case #%d: %d\n", tt, cnt);
  }
  return 0;
}
