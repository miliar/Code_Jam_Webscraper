#include <bits/stdc++.h>
using namespace std;

int main() {
  int z = 0;
  scanf("%d", &z);
  for (int zz = 1; zz <= z; ++zz) {
    long long t = 0;
    scanf("%lld", &t);
    array<bool, 10> seen = {false,};
    long long ans = -1;
    for (int i = 1; i <= 100; ++i) {
      long long tt = t * i;
      while (tt > 0) {
        seen[tt % 10] = true;
        tt /= 10;
      }
      if (count(begin(seen), end(seen), true) == 10) {
        ans = t * i;
        break;
      }
    }

    printf("Case #%d: ", zz);
    if (ans > 0) printf("%lld\n", ans);
    else printf("INSOMNIA\n");
  }

  return 0;
}
