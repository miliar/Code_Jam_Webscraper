#include<stdio.h>

int max(int a, int b) {
   return a > b ? a : b;
}

int main() {
   int t, n, x, p[26], s, m, v[2], idx[2], i;
   scanf("%d", &t);
   for (x = 1; x <= t; x++) {
      scanf("%d", &n);
      s = 0;
      for (i = 0; i < n; i++) {
         scanf("%d", &p[i]);
         s += p[i];
      }
      printf("Case #%d:", x);
      while (s > 0) {
         /* search two big */
         v[0] = v[1] = -1;
         for (i = 0; i < n; i++) {
            if (p[i] >= v[0]) {
               v[1] = v[0];
               v[0] = p[i];
               idx[1] = idx[0];
               idx[0] = i;
            }
            else if (p[i] >= v[1]) {
               v[1] = p[i];
               idx[1] = i;
            }
         }
         m = max(v[0]-1, v[1]);
         if (2*m <= s-1) {
            printf(" %c", 'A' + idx[0]);
            p[idx[0]]--;
            s--;
         }
         else {
            printf(" %c%c", 'A' + idx[0], 'A' + idx[1]);
            p[idx[0]]--;
            p[idx[1]]--;
            s -= 2;
         }
      }
      printf("\n");
   }
   return 0;
}
