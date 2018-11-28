/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long ll;

const int N = 60;

void solve() {
  int k, n = 0, z = 0;
  cin >> k;
  ll x[k], cnt[k], sum = 0;
  forn(i, k)
    cin >> x[i];
  forn(i, k)
    cin >> cnt[i], sum += cnt[i];
  while ((1LL << n) < sum)
    n++;
  while ((1LL << z) < cnt[0])
    z++;
  forn(i, k)
    cnt[i] >>= z;
  ll neg = -x[0];
  forn(i, k)
    x[i] += neg;
  vector<ll> res(n, 0);
  forn(i, n - z) {
    int r = k - 1;
    while (!cnt[r])
      r--;
    int l = r - 1;
    while (!cnt[l])
      l--;
    res[i] = x[r] - x[l];
    for (; r >= 0; r--)
      if (cnt[r]) {
        while (l >= 0 && x[r] - x[l] != res[i])
          l--;
        assert(l >= 0);
        assert(cnt[l] >= cnt[r]);
        cnt[l] -= cnt[r];
      }
  }
  int m = n - z;
  sort(res.begin(), res.begin() + m, greater<int>());
  forn(i, 1 << m) {
    ll sum = 0;
    forn(j, m)
      if ((i >> j) & 1)
        sum += res[j];
    //printf("%d: %I64d, %I64d\n", i, sum, neg);
    if (sum == neg) {
      forn(j, m)
        if ((i >> j) & 1)
          res[j] = -res[j];
      break;
    }
  }
  sort(res.begin(), res.end());
  forn(i, n)
    printf("%I64d ", res[i]);
  puts("");
}

int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    fprintf(stderr, "Case #%d:\n", t + 1);
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
