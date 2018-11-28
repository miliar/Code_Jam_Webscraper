#include <cstdio>
#include <cassert>

#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x" = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 1010;

int N, H;
int a[MAX];

int calc(int x, int y, int s, int t) {
  if (s == 0 && t == 0) return x > y;
  if (s == 0 && t == 1) return 0;
  if (s == 1 && t == 0) return 1;
  if (s == 1 && t == 1) return x < y;
  assert(false);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    scanf("%d", &N);
    REP(i, N) scanf("%d", a+i);

    H = 0;
    REP(i, N) H = max(H, a[i]);

    int ans = N*N;

    REP(mask, 1<<N) {
      int cost = 0;
      REP(i, N) FOR(j, i+1, N) cost += calc(a[i], a[j], (mask>>i) & 1, (mask>>j) & 1);
      ans = min(ans, cost);
    }

    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
