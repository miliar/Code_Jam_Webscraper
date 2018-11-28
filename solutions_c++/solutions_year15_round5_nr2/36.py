/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long ll;

void solve() {
  int n, k;
  cin >> n >> k;
  int m = n - k + 1;
  vector<ll> s(m);
  forn(i, m)
    cin >> s[i];
  vector<ll> add(n, 0);
  for (int i = k; i < n; i++)
    add[i] = add[i - k] - s[i - k] + s[i - k + 1];
  vector<ll> l(k, 0), r(k, 0);
  ll ans = 0, sum = 0, sum_len = 0;
  forn(i, k) {
    for (int j = i; j < n; j += k) {
      l[i] = min(l[i], add[j]);
      r[i] = max(r[i], add[j]);
    }      
    ans = max(ans, r[i] - l[i]);
    //printf("%d: %I64d %I64d\n", i, l[i], r[i]);
    sum += -l[i];
  }
  forn(i, k) 
    sum_len += ans - (r[i] - l[i]);
  int rest = (s[0] - sum) % k;
  if (rest < 0)
    rest += k;
  //printf("s[0] = %I64d, sum = %I64d, rest = %d, ans = %I64d, sum_len  = %I64d\n", s[0], sum, rest, ans, sum_len);
  printf("%I64d\n", ans + (rest > sum_len));
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
