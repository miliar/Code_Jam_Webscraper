#include <cassert>
#include <cstdio>

int main() {
  int tn;
  assert(scanf("%d", &tn) == 1);
  for (int t = 1; t <= tn; t++) {
    printf("Case #%d: ", t);
    int r1, r2, d1[16], d2[16];
    assert(scanf("%d", &r1) == 1);
    for (int i = 0; i < 16; i++)
      assert(scanf("%d", &d1[i]) == 1);
    assert(scanf("%d", &r2) == 1);
    for (int i = 0; i < 16; i++)
      assert(scanf("%d", &d2[i]) == 1);
    int cnt[17];
    for (int i = 1; i <= 16; i++)
      cnt[i] = 0;
    for (int i = 0; i < 4; i++) {
      cnt[d1[i + (r1 - 1) * 4]]++;
      cnt[d2[i + (r2 - 1) * 4]]++;
    }
    int ans = -1, res = 0;
    for (int i = 1; i <= 16; i++)
      if (cnt[i] == 2) {
        ans = i;
        res++;
      }
    if (res < 1)
      puts("Volunteer cheated!");
    else if (res > 1)
      puts("Bad magician!");
    else
      printf("%d\n", ans);
  }
  return 0;
}

