#include <bits/stdc++.h>
using namespace std;

void run(int cas) {
  printf("Case #%d: ", cas);
  int n; scanf("%d", &n);
  if (n == 0) {puts("INSOMNIA"); return;}
  int cnt[10]; memset(cnt, 0, sizeof(cnt));
  int has = 0;
  for (int i = 1; ; ++i) {
    long long x = (long long)n * i;
    while (x) {
      cnt[x % 10]++;
      if (cnt[x % 10] == 1) ++has;
      x /= 10;
    }
    if (has == 10) {
      printf("%lld\n", (long long)i * n);
      return;
    }
  }
  puts("INSOMNIA");
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) run(cas);
  return 0;
}
