#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>

int Tcase, n, m;
bool bo[11];

int solve(int n) {
  m = 0;
  memset(bo, false, sizeof(bo));
  
  int t = 0, num;
  while (m != 10) {
    num = (++t) * n;
    while (num > 0) {
      if (!bo[num % 10]) bo[num % 10] = true, ++m;
      num /= 10;
    }
  }
  return t * n;
}

int main() {
  scanf("%d", &Tcase);
  for (int tt = 1; tt <= Tcase; ++tt) {
    scanf("%d", &n);
    
    if (n == 0) printf("Case #%d: INSOMNIA\n", tt);
    else printf("Case #%d: %d\n", tt, solve(n));
  }
  return 0;
}