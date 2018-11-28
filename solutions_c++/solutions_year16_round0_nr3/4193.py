#include<stdio.h>
#define ll long long

int main() {
   int T, N, J, p, i, j, ok, fail, np, isPrime, count;
   ll primes[1000], div[10], ndiv;
   char coinjam[35];
   ll a, b, s, e;
   
   primes[0] = 2;
   np = 1;
   for (p = 3; p < 1000; p++) {
      isPrime = 1;
      for (i = 0; i < np; i++) {
         if (p%primes[i] == 0) {
            isPrime = 0;
            break;
         }
      }
      if (isPrime == 1)
         primes[np++] = p;
   }
   
   scanf("%d %d %d", &T, &N, &J);
   printf("Case #1:\n");
   count = 0;
   for (i = 0; i < (1 << (N-2)); i++) {
      ok = 1;
      ndiv = 0;
      for (b = 2; b <= 10; b++) {
         s = i;
         a = 1;
         coinjam[0] = '1';
         e = b;
         for (j = 1; j < N-1; j++) {
            a = a + (s%2)*e;
            coinjam[j] = '0' + s%2;
            s /= 2;
            e *= b;
         }
         a += e;
         coinjam[j] = '1';
         
         /*
         for (j = N-1; j >= 0; j--) {
            printf("%c", coinjam[j]);
         }
         printf(" in base %d is %lld\n", b, a);
         */
         
         fail = 1;
         // test "a" for some primes
         for (j = 0; j < np; j++) {
            if (a%primes[j] == 0) {
               div[ndiv++] = primes[j];
               fail = 0;
               break;
            }
         }
         if (fail) {
            ok = 0;
            break;
         }
      }
      if (ok) {
         for (j = N-1; j >= 0; j--) {
            printf("%c", coinjam[j]);
         }
         for (j = 0; j < ndiv; j++) {
            printf(" %lld", div[j]);
         }
         printf("\n");
         count++;
         if (count >= J) break;
      }
   }
   
   return 0;
}
