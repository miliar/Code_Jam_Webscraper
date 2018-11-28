#include <cstdio>
#include <set>
using namespace std;

int T, N;
set<int> S;

int get_digits(int x) {
  while (x != 0) {
    S.insert(x % 10);
    x /= 10;
  }
}

int main(void) {
  scanf("%d", &T);
  int cs = 1;
  while (T--) {
    S.clear();
    scanf("%d", &N);
    if (N == 0) {
      printf("Case #%d: INSOMNIA\n", cs);
    } else {
      get_digits(N);
      int cnt = 1;
      while (S.size() < 10) {
        cnt++;
        get_digits(N * cnt);
      }
      printf("Case #%d: %d\n", cs, N * cnt);
    }
    cs++;
  }
  return 0;
}
