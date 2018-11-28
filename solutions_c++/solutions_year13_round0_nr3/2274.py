#include <cstdio>

typedef long long ll;

bool is(ll n) {
  int gg[17], l = 0;
  for (; n; n /= 10)
    gg[l++] = n % 10;
  for (int a = 0; a < l;)
    if (gg[a++] != gg[--l])
      return false;
  return true;
}

int ans(ll a, ll b) {
  int cnt = 0;

  int tests[] = {1, 4, 9, 121, 484};
  for (int i = 0; i < 5; ++i)
    if (a <= tests[i] && tests[i] <= b)
      cnt += 1;

  ll pot[17] = {1};
  for (int i = 1; i < 17; ++i)
    pot[i] = pot[i-1] * 10;

  for (int dig = 3; ;dig += 1) {
    ll v = 0, vv;
    int hlf = (dig) / 2, uhlf = (dig + 1) / 2;

    for (int i = pot[uhlf-1]; i < pot[uhlf]; ++i) {
      if (dig % 2 == 0)
	v = (pot[hlf] + pot[hlf-1]) * (i % 10);
      else
	v = pot[hlf] * (i % 10);

      int l, r;
      if (dig % 2 == 0)
	l = hlf, r = hlf-1;
      else
	l = r = hlf;
      for (int t = i / 10, c = 1; t; t /= 10, c += 1)
	v += (pot[l+c] + pot[r-c]) * (t % 10);

      vv = v * v;
      if (vv > b) return cnt;
      else if (vv < a) continue;
      
      if (is(vv)) cnt += 1;
    }
  }

  return cnt;
}

int main() {
  int t;
  scanf("%d", &t);

  for (int i = 1; i <= t; ++i) {
    ll a, b;
    scanf("%I64d%I64d", &a, &b);
    printf("Case #%d: %d\n", i, ans(a, b));
  }

  return 0;
}
