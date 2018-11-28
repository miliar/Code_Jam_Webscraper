#include <stdio.h>
#include <stdlib.h>

char str[10000];
int main() {
  int T, x;
  scanf("%d", &T);
  for (int TC=1; TC<=T; TC++) {
    scanf("%d%s", &x, str);
    int ans = 0;
    int tot = 0;
    for (int i=0; i<=x; i++) {
      if(str[i]>'0') {
        if (tot < i) {
          ans += i - tot;
          tot = i;
        }
        tot += (str[i]-'0');
      }
    }
    printf("Case #%d: %d\n", TC, ans);
  }
}