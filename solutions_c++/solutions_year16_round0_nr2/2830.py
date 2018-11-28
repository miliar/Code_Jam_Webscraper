#include <algorithm>
#include <iostream>

using namespace std;

#define MAXS 110

int T, L = 0;
char S[MAXS];

char swap(char c) {
  if (c == '+')
    return '-';
  return '+';
}

int main() {
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    scanf("%s", S);
    L = strlen(S);
    int c = 0;
    int t = L;
    while (t != 0) {
      if (S[t - 1] == '+')
        t--;
      else {
        int j = 0;
        while (j < t && S[j] == '+')
          S[j++] = '-';
        if (j > 0)
          c++;
        if (j != t) {
          for (j = 0; j < (t + 1) / 2; j++) {
            S[j] = swap(S[j]);
            if (j != t - j - 1)
              S[t - j - 1] = swap(S[t - j - 1]);
            swap(S[j], S[t - j - 1]);
          }
          c++;
        }
      }
    }
    printf("Case #%d: %d\n", i, c);
  }
  return 0;
}
