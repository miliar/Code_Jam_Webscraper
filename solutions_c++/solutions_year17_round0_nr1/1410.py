#include <cstdio>
#include <vector>

using namespace std;

const int MAXN = 2010;

int T, k, test_case = 1;
char pancakes[MAXN];

int main(void) {
  scanf("%d", &T);

  while (T--) {
    scanf("%s %d", pancakes, &k);
    
    int sol = 0;
    int len = strlen(pancakes);
    bool impossible = false;
    for (int i = 0; i < len; ++i) {
      if (i + k <= len && pancakes[i] == '-') {
        for (int j = i; j < i + k; ++j) {
          pancakes[j] = pancakes[j] == '+' ? '-' : '+';
        }
        sol += 1;
      }
      if (pancakes[i] == '-') {
        impossible = true;
      }
    }
    if (impossible) {
      printf("Case #%d: IMPOSSIBLE\n", test_case++);
    } else {
      printf("Case #%d: %d\n", test_case++, sol);
    }
  }
  return 0;
}
