#include <cstdio>
#include <cstdlib>
#include <cstring>

int main() {
  int T;
  char pancake[101];
  int pos[101];
  int neg[101];
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%s", pancake);
    pos[0] = pancake[0] == '+' ? 0 : 1;
    neg[0] = pancake[0] == '-' ? 0 : 1;
    for (size_t i = 1; i < strlen(pancake); i++) {
      pos[i] = pancake[i] == '+' ? pos[i - 1] : (neg[i - 1] + 1);
      neg[i] = pancake[i] == '-' ? neg[i - 1] : (pos[i - 1] + 1);
    }
    printf("Case #%d: %d\n", t, pos[strlen(pancake) - 1]);
  }
  return 0;
}
