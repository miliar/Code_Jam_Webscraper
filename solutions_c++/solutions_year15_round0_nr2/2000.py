/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 * Date: 2015.04.12
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

void solve() {
  int n;
  scanf("%d", &n);
  int a[n];
  forn(i, n)
    scanf("%d", &a[i]);

  int l = 0, r = *max_element(a, a + n);
  while (l != r) {
    int m = (l + r) / 2, good = 0;
    forn(t, m) {
      int T = m - t, cnt = 0;
      forn(i, n)
        cnt += (a[i] + T - 1) / T - 1;
      //printf("m = %d, t = %d, T = %d, cnt = %d\n", m, t, T, cnt);
      good |= cnt <= t;
    }
    if (good)
      r = m;
    else
      l = m + 1;
  }
  printf("%d\n", l);
}

int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}

