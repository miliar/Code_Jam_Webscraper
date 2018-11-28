#include <cstdio>

const int MAXN = 111;
const int MAXL = 111;
int T;
int N, L;

char A[MAXN][MAXL];
char B[MAXL];
int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    bool done = false;
    printf("Case #%d: ", t);
    scanf("%d %d", &N, &L);
    for(int i = 0; i < N; ++i) {
      scanf("%s", A[i]);
      bool good = true;
      for(int j = 0; j < L; ++j) {
        if (A[i][j] == '0') {
          good = false;
        }
      }
      if (good) {
        printf("IMPOSSIBLE\n");
        done = true;
      }
    }

    scanf("%s", B);
    if (!done) {
      if (L == 1) {
        printf("0");
      }
      for(int i = 0; i < L - 1; ++i) {
        printf("1");
      }
      printf(" ");
      for(int i = 0; i < L; ++i) {
        printf("0?");
      }
      printf("\n");
    }
  }
}
