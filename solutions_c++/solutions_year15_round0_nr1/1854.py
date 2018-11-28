#include <cstdio>
#include <algorithm>

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int no = 1; no <= tcase; ++no) {
    int s;
    scanf("%d", &s);
    int ans = 0, sum = 0;
    for (int i = 0; i <= s; ++i) {
      char ch;
      scanf(" %c", &ch);
      ans += std::max(i - (ans + sum), 0);
      sum += ch - '0';
    }
    printf("Case #%d: %d\n", no, ans);
  }
  return 0;
}
