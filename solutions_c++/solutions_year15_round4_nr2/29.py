/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long double dbl;

void solve() {
  int n;
  dbl V, T;
  cin >> n >> V >> T;
  struct Source {
    dbl v, t;
    bool operator < ( Source s ) const { return t < s.t; }
  } s[n];
  forn(i, n)
    cin >> s[i].v >> s[i].t;
  sort(s, s + n);
  if (s[0].t > T || s[n - 1].t < T) {
    puts("IMPOSSIBLE");
    return;
  }
  const dbl eps = 1e-14;
  dbl s1 = 0, s2 = 0, S1, S2;
  forn(i, n)
    s1 += s[i].v * s[i].t, s2 += s[i].v;
  //fprintf(stderr, "%.3f < %.3f\n", s1, T * s2);
  if (s1 < T * s2 * (1 - eps)) {
    int l = 0;
    while (l + 1 < n && (S1 = s1 - s[l].v * s[l].t) < T * (S2 = s2 - s[l].v) * (1 - eps))
      s1 = S1, s2 = S2, l++;
    // s1 - i * s[l].t = T * (s2 - i)
    if (s[l].t != T) {
      dbl i = (T * s2 - s1) / (T - s[l].t);
      s1 -= i * s[l].t, s2 -= i;
    }
  } else if (s1 > T * s2 * (1 + eps)) {
    int r = n - 1;
    while (r > 0 && (S1 = s1 - s[r].v * s[r].t) > T * (S2 = s2 - s[r].v) * (1 + eps))
      s1 = S1, s2 = S2, r--;
    // s1 - i * s[r].t = T * (s2 - i)
    if (s[r].t != T) {
      dbl i = (T * s2 - s1) / (T - s[r].t);
      s1 -= i * s[r].t, s2 -= i;
    }
  }
  //fprintf(stderr, "%.15f / %.15f == %.15f : %.15f\n", s1, s2, s1 / s2, T);
  printf("%.15f\n", (double)(V / s2));
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
