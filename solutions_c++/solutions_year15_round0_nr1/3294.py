#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int maxn = 1111;
char s[maxn];
int n;

int get(int x) {
  int cnt = x;
  for (int i = 0; i <= n; ++ i) {
    int dig = s[i] - '0';
    if (cnt >= i) {
      cnt += dig;
    } else {
      return 0;
    }
  }

  return 1;
}

void solve() {
  int low = 0, high = maxn;
  while (low < high) {
    int mid = (low + high) >> 1;
    if (get(mid)) {
      high = mid;
    } else {
      low = mid+1;
    }
  }

  printf("%d", low);
}

int main() {
  int t;
  scanf("%d", &t);

  for (int i = 1; i <= t; ++ i) {
    scanf("%d %s", &n, s);
    printf("Case #%d: ", i);
    solve();
    if (i < t) {
      printf("\n");
    }
  }

  return 0;
}

