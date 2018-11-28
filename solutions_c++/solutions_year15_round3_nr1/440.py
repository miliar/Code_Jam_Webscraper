#include <cstdio>

int t, r, c, w;

int main() {
  scanf("%d", &t);

  for (int i = 1; i <= t; ++i) {
    scanf("%d%d%d", &r, &c, &w);
    int extra = (w * (c / w) != c ? 1 : 0);
    printf("Case #%d: %d\n", i, r * (c / w) + w - 1 + extra); 
  }
  return 0;
}
