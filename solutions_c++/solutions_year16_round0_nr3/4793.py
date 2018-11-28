#include <cstdio>

typedef long long ll;

int n, j;
int d[16];

ll prime(ll n) {
  if (n % 2 == 0) return 2;
  for (ll i = 3; n/i >= i; i += 2)
    if (n % i == 0)
      return i;
  return 0;
}

void tryit() {
  bool ok = true;
  ll div[11];
  for (ll b = 2; b <= 10; ++b) {
    ll x = 0;
    for (int i = 0; i < n; ++i)
      x = x * b + d[i];

    div[b] = prime(x);
    ok = ok && div[b] > 0;
  }

  if (ok) {
    for (int i = 0; i < n; ++i) printf("%d", d[i]);
    for (int i = 2; i <= 10; ++i)
      printf(" %lld", div[i]);
    puts("");
    --j;
  }
}

void jam(int i = 1) {
  if (j==0) return;
  if (i == n-1) {
    d[n-1] = 1;
    tryit();
  } else {
    d[i] = 0;
    jam(i+1);
    d[i] = 1;
    jam(i+1);
  }
}

int main() {
  int t;
  scanf("%d", &t);
  d[0] = 1;
  for (int c = 1; c <= t; ++c) {
    scanf("%d %d", &n, &j);
    printf("Case #%d:\n", c);
    jam();
  }
  return 0;
}
