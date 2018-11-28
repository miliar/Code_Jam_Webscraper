#include <cstdio>
#include <cassert>

const int MAXN = 1005;

int D;
int a[MAXN];
void solve() {
  scanf("%d", &D);
  int maximum = 0;
  for (int i = 0; i < D; i++) {
    scanf("%d", &a[i]);
    if (a[i] > maximum)
      maximum = a[i];
  }
  int best = -1;
  for (int i = 1; i <= maximum; i++) {
    int ans = i;
    for (int j = 0; j < D; j++) {
      int b = a[j] / i - 1;
      if (b < 0)
        b = 0;
      while (a[j] - b*i > i)
        b++;
      ans += b;
    }
    if (best == -1 || ans < best)
      best = ans;
  }
  printf("%d\n", best);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve();
  }
}
