#include<iostream>

using namespace std;

int main (void) {
  int t;
  scanf("%d", &t);
  for (int cn = 1; cn <= t; ++cn) {
    int n;
    scanf(" %d", &n);
    int sum = 0;
    int ret = 0;
    for (int i = 0; i <= n; ++i) {
      char c;
      int d;
      scanf(" %c", &c);
      d = int(c) - '0';
      if (sum < i) {
        ret += (i - sum);
        sum = i;
      }
      sum += d;
    }
    printf("Case #%d: %d\n", cn, ret);
  }
  return 0;
}
