#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

int main(void) {
  int cases=0;
  int t;
  int a,b,c,i,j,k;

  scanf("%d", &cases);
  t=cases;

  while (t--) {
    c=0;
    scanf("%d %d %d", &a,&b,&k);
    // printf("%d %d %d\n", a, b, k);
    for (i=0;i<a;i++)
      for (j=0;j<b;j++)
        if ((i&j)<k) {
          c++;
          // printf("%d %d\n", i, j);
        }

    printf("Case #%d: ", cases-t);
    printf("%d\n", c);
  }
  return 0;
}
