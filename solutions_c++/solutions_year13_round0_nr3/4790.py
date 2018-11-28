#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;
const int MAXN = 1005;

bool check(int val) {
  static char s[MAXN];
  int n = 0;
  while (val) {
    s[n++] = val % 10;
    val /= 10;
  }
  for (int i = 0; i < n / 2; ++i) {
    if (s[i] != s[n - i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);
  int t, a, b, cas = 1;

  scanf("%d", &t);
  while (t--) {
    printf("Case #%d: ", cas++);
    scanf("%d%d", &a, &b);

    int cnt = 0;
    for (int i = a; i <= b; ++i) {
      int sq = sqrt(i * 1.0);
      if (sq * sq == i && check(sq) && check(i)) {
        ++cnt;
      }
    }
    printf("%d\n", cnt);
  }
  return 0;
}
