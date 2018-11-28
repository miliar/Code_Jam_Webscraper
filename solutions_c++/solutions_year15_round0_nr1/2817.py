#include <cstdio>
#include <algorithm>

char S[1002];

void tcase(int t) {
  int n; scanf("%d", &n);
  scanf("%s", S);

  int stand = 0, extra = 0;
  for (int i = 0; i <= n; i++) {
    if (stand < i) {
      extra += i - stand;
      stand = i;
    }
    stand += S[i] - '0';
  }

  printf("Case #%d: %d\n", t, extra);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    tcase(i);
  }
}
