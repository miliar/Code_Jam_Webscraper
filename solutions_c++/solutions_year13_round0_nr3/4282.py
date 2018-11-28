#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

int a[10000010];

bool palindrome(long long x) {
  char c[20];
  int cnt = 0;
  while (x) {
    c[cnt++] = x % 10;
    x /= 10;
  }
  for (int i = 0; i < cnt; i++) {
    if (c[i] != c[cnt - i - 1])
      return 0;
  }
  return 1;
}

void precalc() {
  for (int i = 1; i < 10000001; i++) {
    if (palindrome(i) && palindrome((long long)i*i)) {
      a[i] = a[i - 1] + 1;
    } else {
      a[i] = a[i - 1];
    }
  }
}
int T;
long long A, B;
int main() {
  precalc();
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    scanf("%lld%lld", &A, &B);
    int _a = sqrt(A);
    int _b = sqrt(B);
    if ((long long)_a*_a != A)
      _a++;
    printf("Case #%d: %d\n", test, a[_b] - a[_a - 1]);
  }
  return 0;
}
