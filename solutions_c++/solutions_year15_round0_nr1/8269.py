#include <cstdio>
#include <algorithm>

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    int s_max;
    scanf("%d ", &s_max);
    int result = 0;
    int people = 0;
    for (int level = 0; level <= s_max; ++level) {
      char cur;
      scanf("%c", &cur);
      cur -= '0';
      if (cur == 0) {
        continue;
      }
      int cur_add = std::max(0, level - people);
      result += cur_add;
      people += cur_add + cur;
    }
    printf("Case #%d: %d\n", t, result);
  }
}
