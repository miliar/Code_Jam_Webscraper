#include <iostream>
#include <cstdio>

using namespace std;

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    long long n;
    scanf("%lld", &n);
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", i);
    } else {
      int flag = 0;
      int m = 0;
      do {
        ++m;
        int nm = n*m;
        while (nm) {
          flag |= 1 << (nm%10);
          nm /= 10;
        }
      } while (flag != ((1<<10)-1));
      printf("Case #%d: %lld\n", i, n*m);
    }
  }

}
