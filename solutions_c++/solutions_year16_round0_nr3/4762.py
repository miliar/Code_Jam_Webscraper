#include <bits/stdc++.h>

using namespace std;

const int N = 555, M = 11;
long long a[N][M];

long long convert(long long x, int base) {
  long long ret = 0, power = 1;
  while (x) {
    ret += x % 10 * power;
    power *= base;
    x /= 10;
  }
  return ret;
}

long long getDivisor(long long x) {
  for (long long i = 2; i * i <= x; ++i) {
    if (x % i == 0)
      return i;
  }
  return 0;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    int n, m;
    scanf("%d %d", &n, &m);
    int sz = 0;
    for (int mask = 1; sz < m && mask < (1 << n); mask += 2) {
      if (32 - __builtin_clz(mask) != n)
        continue;
      long long x = 0, tmp = 0;
      for (int i = 0; i < n; ++i)
        tmp = tmp * 10 + ((mask >> i) & 1);
      while (tmp) {
        x = x * 10 + tmp % 10;
        tmp /= 10;
      }
      bool check = true;
      for (int base = 2; base < M; ++base) {
        a[sz][base - 1] = getDivisor(convert(x, base));
        check &= !!a[sz][base - 1];
      }
      if (check)
        a[sz++][0] = x;
    }
    printf("Case #%d:\n", tst++);
    for (int i = 0; i < sz; ++i) {
      for (int j = 0; j + 1 < M; ++j) {
        printf("%lld%c", a[i][j], " \n"[j + 2 == M]);
      }
    }
  }
}
