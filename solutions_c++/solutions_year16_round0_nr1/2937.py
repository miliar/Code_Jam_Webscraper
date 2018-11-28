#include <bits/stdc++.h>

using namespace std;

int get(long long n) {
  int d = 0;
  while(n > 0) {
    d |= (1 << (n % 10));
    n /= 10;
  }
  return d;
}

int main() {
#ifdef DEBUG
  freopen("input.txt", "rt", stdin);
#else
  freopen("A.in", "rt", stdin);
  freopen("A.out", "wt", stdout);
#endif
  int t; scanf("%d", &t);
  for(int tst = 1; tst <= t; ++tst) {
    int n; scanf("%d", &n);
    printf("Case #%d: ", tst);
    if(n == 0) {
      puts("INSOMNIA");
      continue;
    }
    int was = get(n);
    int nn = n;
    while(was != 1023) {
      nn += n;
      was |= get(nn);
    }
    printf("%d\n", nn);
  }
  return 0;
}
