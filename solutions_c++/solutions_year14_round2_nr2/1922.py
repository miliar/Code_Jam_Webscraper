#include <cstdio>

void work(int indexa) {
  printf("Case #%d: ", indexa);
  int A, B, K;
  scanf("%d %d %d", &A, &B, &K);
  int i, j;
  int ans = 0;
  for(i = 0; i < A; i++) {
    for(j = 0; j < B; j++) {
      if((i & j) < K) ans++;
    }
  }
  printf("%d\n", ans);
}

int main() {
  int T;
  scanf("%d", &T);
  int cnt;
  for(cnt = 1; cnt <= T; cnt++) {
    work(cnt);
  }
  return 0;
}
