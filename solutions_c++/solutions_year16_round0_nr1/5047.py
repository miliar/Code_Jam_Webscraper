#include<stdio.h>

int main() {
   int T, N, i, s[10], x, y, a, count;
   scanf("%d", &T);
   for (x = 1; x <= T; x++) {
      scanf("%d", &N);
      printf("Case #%d: ", x);
      if (N == 0) {
         printf("INSOMNIA\n");
         continue;
      }
      count = 0;
      for (i = 0; i <= 9; i++)
         s[i] = 0;
      for (i = 1; count < 10; i++) {
         y = a = N*i;
         while (a > 0) {
            if (s[a%10] == 0) {
               s[a%10] = 1;
               count++;
            } 
            a /= 10;
         }
      }
      printf("%d\n", y);
   }
   return 0;
}
