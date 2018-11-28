#include <cstdio>
#include <cstring>

const int MAX_L = 1000000 + 5;

bool isCons(char c) {
  return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

char s[MAX_L];
int consecutive[MAX_L];
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int n;
    scanf("%s %d\n", s, &n);
    memset(consecutive, 0, sizeof(consecutive));
    consecutive[0] = isCons(s[0]);
    for (int i = 1; s[i]; ++i) {
      if (isCons(s[i])) {
        consecutive[i] = consecutive[i - 1] + 1;
      }
    }
    int start = -1;
    long long res = 0;
    for (int i = 0; s[i]; ++i) {
      if (consecutive[i] >= n) {
        start = i - n + 1;
      }
      if (start != -1) {
        res += start + 1;
      }
    }
    printf("Case #%d: %lld\n", t + 1, res);
  }
}
