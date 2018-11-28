#include <cstdio>
#include <set>
using namespace std;

int main() {
  int T, N;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; ++tc) {
    scanf("%d", &N);
    if (N == 0) {
      printf("Case #%d: INSOMNIA\n", tc);
    } else {
      set<int> digits;
      int a = 0;

      while (digits.size() < 10) {
        a += N;
        int tmp = a;
        while (tmp > 0) {
          digits.insert(tmp % 10);
          tmp /= 10;
        }
      }
      printf("Case #%d: %d\n", tc, a);
    }
  }

  return 0;
}
