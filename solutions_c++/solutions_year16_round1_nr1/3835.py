#include<stdio.h>
#include<string.h>
#define N 1010

char S[N], a[N], b[N];
char m[N][N];

int main() {
   int T, i, j, x, n;
   scanf("%d", &T);
   for (x = 1; x <= T; x++) {
      scanf(" %s", S);
      n = strlen(S);
      m[0][0] = S[0];
      m[0][1] = 0;
      for (i = 1; i < n; i++) {
         for (j = 0; j <= i-1; j++) {
            a[j] = m[i-1][j];
         }
         a[i] = S[i];
         a[i+1] = 0;
         for (j = 1; j <= i; j++) {
            b[j] = m[i-1][j-1];
         }
         b[0] = S[i];
         b[i+1] = 0;
         if (strcmp(a, b) > 0) {
            strcpy(m[i], a);
         }
         else {
            strcpy(m[i], b);
         }
      }
      printf("Case #%d: %s\n", x, m[n-1]);
   }
   return 0;
}
