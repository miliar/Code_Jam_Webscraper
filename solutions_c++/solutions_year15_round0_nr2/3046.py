#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

int d;
int a[N];

int main() {
  freopen("inp.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    scanf("%d", &d);
    for (int i = 1; i <= d; i++) {
      scanf("%d", a + i);
    }
    sort(a + 1, a + d + 1);
    int res = 1000000000;
    for (int base = 1; base <= a[d]; base++) {
      int add = 0;
      for (int i = 1; i <= d; i++) {
        if (a[i] > base) {
          int foo = a[i] - base - 1;
          add += (foo / base) + 1;
        }
      }
      res = min(res, base + add);
    }
    printf("Case #%d: %d\n", test, res);
  }
  return 0;
}
