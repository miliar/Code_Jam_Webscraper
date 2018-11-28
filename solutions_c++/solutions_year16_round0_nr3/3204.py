#include <cstdio>
#include <algorithm>

using namespace std;

typedef unsigned long ul;

ul pos = 0, divs[15];

ul trans(ul v, ul b) {
   ul res = 0;
   for (ul i = 1; v; i*=b, v/=2) res += i*(v%2);
   return res;
}

bool prime(ul n) {
   for (ul i = 2; i*i <= n; i++)
      if (!(n%i)) {
         divs[pos++] = i;
         return false;
      }
   return true;
}

/*
char *bin(ul v) {
   static char s[50];
   ul i;
   for (i = 0; v; i++, v/=2) s[i] = v%2+'0';
   for (ul j = 0; j <= i/2; j++) swap(s[j], s[i-j-1]);
   s[i] = '\0';
   return s;
}
*/

int main() {
   ul T, N, J, cnt = 0;
   scanf("%lu%lu%lu", &T, &N, &J);
   printf("Case #1:\n");
   for (ul v = (1<<(N-1))+1; cnt < J && v < (1<<N); v+=2) {
      ul i;
      pos = 0;

      /*
      printf("checking %lu: %s |", v, bin(v));
      for (i = 2; i <= 10; i++)
         printf(" %lu", trans(v, i));
      printf("\n");
      */

      for (i = 2; i <= 10; i++)
         if (prime(trans(v, i))) break;
      if (i == 11) {
         printf("%lu", trans(v, 10));
         for (i = 0; i < 9; i++) printf(" %lu", divs[i]);
         printf("\n");
         cnt++;
      }
   }
	return 0;
}
