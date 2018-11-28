#include <cstdio>
#include <cstring>

#define MAX 2000

using namespace std;

void flip(char *p, int k) {
  for (int i = 0; i < k; ++i) {
    if (*p == '-') {
      *p = '+';
    } else {
      *p = '-';
    }
    p++;
  }
}

int main() {
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; ++test) {
    int k; char pan[MAX];
    scanf("%s %d", pan, &k);
    std::size_t n = strlen(pan);

    int res = 0;
    bool ok = true;
    for (int i = 0; i < n; ++i) {
      if (pan[i] == '-' && i + k <= n) {
        flip(pan + i, k);
        res++;
      } else if (pan[i] == '-' && i + k > n) {
        ok = false;
        break;
      }
    }

    if (ok) {
      printf("Case #%d: %d\n", test, res);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", test);
    }
  }

  return 0;
}
