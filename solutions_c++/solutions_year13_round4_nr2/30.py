#include <stdio.h>
#include <string.h>
long long p;
int n;
int check1(long long x) {
  if (x == 0) return 1;
  long long left = x;
  long long pos = 0;
  for (int i = 0; i < n; i++) {
    long long d = (1ll << (n - 1 - i));
    if (left >= (1ll << i)) {
      left -= (1ll << i);
      pos += d;
    }
  }
  return pos < p;
}
int check2(long long x) {
  if (x == 0) return 1;
  long long left = (1ll << n) - 1 - x;
  long long pos = (1ll << n) - 1;
  for (int i = 0; i < n; i++) {
    long long d = (1ll << (n - 1 - i));
    if (left >= (1ll << i)) {
      left -= (1ll << i);
      pos -= d;
    } 
  }
  return pos < p;
}
int main() {
  int T, cp;
  for (scanf("%d", &T), cp = 1; cp <= T; cp++) {
    scanf("%d%lld", &n, &p);
    long long left = 0, right = p - 1, mid;
    long long ans1 = 0, ans2 = 0;
    while (left <= right) {
      mid = left + ((right - left) >> 1);
      if (check1(mid)) {
        left = mid + 1;
        ans1 = mid;
      } else right = mid - 1;
    }
    left = 0, right = (1ll << n) - 1;
    while (left <= right) {
      mid = left + ((right - left) >> 1);
      if (check2(mid)) {
        left = mid + 1;
        ans2 = mid;
      } else right = mid - 1;
    }
    printf("Case #%d: %lld %lld\n", cp, ans1, ans2);
  }
  return 0;
}
