#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int maxn = 1111;
int n;
int a[maxn];

int max;

void solve2();

void solve() {
  solve2();
  return;
  int ans = 0;
  for (int i = 1000; i; -- i) if (a[i]) {
    int t = i/2;
    if (i&1) t += 1;
    int j;
    for (j = i-1; j != t; -- j) {
      if (a[j]) break;
    }
    if ( i-j > a[i]) {
      ans += a[i];
      a[t] += 1;
      a[i-t] += 1;
    } else {
      ans += i;
      break;
    }
  }

  printf("%d", ans);
}

void solve2() {
  int ans = 100000;
  for (int i = 1; i <= max; ++ i) {
    int cnt = i;
    for (int j = 0; j < n; ++ j) {
      if (a[j] > i) {
        cnt += (a[j]-i)/i;
        if ( (a[j]-i)%i ) cnt +=1;
      }
    }

    if (cnt < ans) ans = cnt;
  }

  printf("%d", ans);

}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++ i) {
    scanf("%d", &n);
    memset(a, 0, sizeof(a));
    max = 0;
    for (int i = 0; i < n; ++ i) {
      int t;
      //scanf("%d", &t);
      //a[t] += 1;
      scanf("%d", a+i);
      if (a[i] > max) max = a[i];
    }
    printf("Case #%d: ", i);
    solve();
    if (i < t) {
      printf("\n");
    }
  }

  return 0;
}

