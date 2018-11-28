#include <iostream>
using namespace std;

int main() {

  int T, tc, a, p, n, count, res, i;
  char str[1001], c;

  scanf("%d", &T);
  for(tc = 1; tc <= T; tc++) {
    scanf("%d", &n);
    scanf("%c", &c);
    scanf("%s", str);
    count = 0;
    res = 0;
    for(i = 0; i <= n; i++) {
      if(count < i) {
        res++;
        count++;
      }
      p = str[i] - '0';
      count = count + p;
    }
    printf("Case #%d: %d\n", tc, res);
  }
}