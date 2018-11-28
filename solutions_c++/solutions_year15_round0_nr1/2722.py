#include <cstdio>
#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>

using namespace std;
typedef long long llint;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

const int MAXSMAX = 1005;

int smax;
char s[MAXSMAX];
int cnt[MAXSMAX];

void solve() {
  scanf("%d %s", &smax, s);
  REP(i, smax + 1) cnt[i] = s[i] - '0';

  int lo = 0, hi = smax;
  while (lo < hi) {
    int mid = (lo + hi) / 2;
    
    cnt[0] += mid;

    int all = 0;
    int standing = 0;
    REP(i, smax + 1) {
      all += cnt[i];
      if (standing >= i) standing += cnt[i];
    }

    if (standing < all)
      lo = mid + 1;
    else
      hi = mid;

    cnt[0] -= mid;
  }

  printf("%d\n", lo);
}

int main(void) 
{
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
