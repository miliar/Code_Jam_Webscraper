#include "stdc++.h"
using namespace std;

int main() {
  int tc, cn, smax, i, ans, p;
  char s[1002];
  scanf("%d", &tc);
  for(cn = 1; cn <= tc; cn++) {
    scanf("%d%s", &smax, s);
    for(i = ans = p = 0; i <= smax; i++) {
      if(s[i] > '0' && i > p) {
	ans += i - p;
	p = i;
      }
      p += s[i] - '0';
    }
    printf("Case #%d: %d\n", cn, ans);
  }
  return 0;
}
