#include <stdio.h>

int t, first_t;
int k, c, s;

int main() {
  scanf("%d", &t);
  first_t = t;

  int c = 0;
  while (t--) {
    scanf("%d %d %d", &k, &c, &s);

    printf("Case #%d: ", first_t - t);
    
    for (int i = 0; i < s; i++) {
      printf("%d ", i + 1);
    }

    printf("\n");
  }

}
