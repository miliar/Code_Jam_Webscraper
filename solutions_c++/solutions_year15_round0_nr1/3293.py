#include <stdio.h>
#include <stdlib.h>

const int maxn = 1050;
char s[maxn];
int n;

int get_c(int x) {
  int cnt = x;
  for (int i = 0; i <= n; ++ i) {
    int digit = s[i] - '0';
    if (cnt >= i) {
      cnt += digit;
    } else {
      return 0;
    }
  }

  return 1;
}
int main() {
     freopen("A-large.in", "r", stdin);
     freopen("solve_out.txt", "w", stdout);

  int t;
  scanf("%d", &t);

  for (int i = 1; i <= t; ++ i) {
    scanf("%d %s", &n, s);
    printf("Case #%d: ", i);
     int low = 0, high = maxn;
  while (low < high) {
    int mid = (low + high) >> 1;
    if (get_c(mid)) {
      high = mid;
    } else {
      low = mid+1;
    }
  }

  printf("%d", low);
    if (i < t) {
      printf("\n");
    }
  }

  return 0;
}
