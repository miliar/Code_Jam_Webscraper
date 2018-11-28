#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int p[10000];
int main() {
  int T, n;
  scanf("%d", &T);
  for (int TC=1; TC<=T; TC++) {
    scanf("%d", &n);
    int ax = 0;
    for (int i=0; i<n; i++) {
      scanf("%d", &p[i]);
      ax = max(ax, p[i]);
    }

    int ans = ax;
    for (int t=1; t<ax; t++) {
      int tot = t;
      for (int i=0; i<n; i++) {
        tot += ((p[i] + t - 1)/t - 1);
      }
      ans = min(ans, tot);
    }
    printf("Case #%d: %d\n", TC, ans);
  }
}