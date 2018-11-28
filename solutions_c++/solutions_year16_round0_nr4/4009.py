#include <cstdio>

int main() {
  int ttt;
  scanf("%d", &ttt);
  for (int tt = 0; tt < ttt; ++tt) {
    int len, iters, numTest;
    scanf("%d%d%d", &len, &iters, &numTest);
    printf("Case #%d:", tt + 1);
    if (len != numTest) {
      printf(" IMPOSSIBLE\n");
      continue;
    }
    for (int i = 0; i < len; ++i) {
      long long ret = 0;
      for (int j = 0; j < iters; ++j) {
        ret = ret * len + i;
      }
      printf(" %lld", ret + 1);
    }
    printf("\n");
  }
  return 0;
}
