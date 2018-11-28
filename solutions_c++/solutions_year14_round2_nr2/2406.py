#include <cstdio>

using namespace std;

int main() {
  int T;

  scanf("%d", &T);

  for (int cas = 1; cas <= T; cas++) {
    printf("Case #%d: ", cas);

    int A, B, K;

    scanf("%d %d %d", &A, &B, &K);

    int cnt = 0;

    for (int i = 0; i < A; i++) {
      for (int j = 0; j < B; j++) {
        if ((i & j) >= K) continue;
        cnt++;
      }
    }

    printf("%d\n", cnt);
  }

  return 0;
}
