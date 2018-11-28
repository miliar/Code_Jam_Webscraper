#include <stdio.h>
#include <string.h>

char long_list[1005];
int S[1005];
int tmp[1005];

bool isPossible(int s_max, int* A, int friends) {
  memcpy(tmp, A, sizeof(int) * (s_max + 1));
  tmp[0] += friends;
  int totalSoFar = tmp[0];
  for (int i = 1; i <= s_max; ++i) {
    if (tmp[i] > 0 && totalSoFar < i) {
      return false;
    }
    totalSoFar += tmp[i];
  }
  return true;
}

int main() {
  int tc;
  scanf("%d ", &tc);
  for (int TC = 1; TC <= tc; ++TC) {
    int s_max;
    scanf("%d ", &s_max);
    fgets(long_list, 1005, stdin);
    for (int i = 0; i <= s_max; ++i) {
      S[i] = long_list[i] - '0';
    }

    for (int i = 0;; ++i) {
      if (isPossible(s_max, S, i)) {
        printf("Case #%d: %d\n", TC, i);
        break;
      }
    }
  }
  return 0;
}
