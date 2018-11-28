#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    long long n;
    cin >> n;
    if (n == 0) {
      puts("INSOMNIA");
      continue;
    }
    vector <int> cnt(10, 0);
    for (int j = 0; ; j++) {
      long long x = n * j;
      while (x > 0) {
        cnt[x % 10]++;
        x /= 10;
      }
      bool all = true;
      for (int k = 0; k < 10; k++) {
        all &= (cnt[k] > 0);
      }
      if (all) {
        printf("%lld\n", n * j);
        break;
      }
    }
  }
  return 0;
}
