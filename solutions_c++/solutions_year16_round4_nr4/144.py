#include <bits/stdc++.h>
using namespace std;
int a[30], b[30];
char s[30][30];
bool ss[30][30];
bool sel[30];
int n;
bool recur(int x) {
  if (x == n) {
    return true;
  }
  bool t = true;
  bool chose = false;
  for (int i = 0; i < n; i++) {
    if (sel[i]) continue;
    if (s[a[x]][i] == '0' && !ss[a[x]][i])
      continue;
    chose = true;
    sel[i] = true;
    t &= recur(x + 1);
    sel[i] = false;
  }
  return t && chose;
}
int solve() {
  int ans = 99999;

  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%s", s[i]);
  }
  int m = (1 << (n * n));
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      a[j] = j;
    }
    bool ok = true;
    for (int p = 0; p < n; p++) {
      for (int q = 0; q < n; q++) {
        ss[p][q] = (i & (1 << (p * n + q))) > 0;
        ok &= s[p][q] == '0' || !ss[p][q];
      }
    }
    do {
      ok &= recur(0);
    } while (ok && next_permutation(a, a + n));
    if (ok) {
      int cnt = 0;
      for (int j = 0; j < n * n; j++) {
        cnt += (i & (1 << j)) > 0;
      }
      ans = min(ans, cnt);
    }
  }
  return ans;
}
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: %d\n", t, solve());
  }
  return 0;
}

