#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

bool is_palindrom(int n) {
   char angka[110];
   sprintf(angka, "%d", n);
   for (int i=0; i*i<strlen(angka); i++)
      if (angka[i] != angka[strlen(angka)-i-1]) return false;
   return true;
}

bool is_square(int n) {
   int sq = (int)sqrt(n);
   return ((sq*sq == n) && is_palindrom(sq));
}

int main() {
   int t;
   scanf("%d", &t);
   for (int c = 1; c <= t; c++) {
      int a, b, counter = 0;;
      scanf("%d %d", &a, &b);
      for (int i=a; i<=b; i++) {
         if (is_palindrom(i) && is_square(i)) counter++;
      }
      printf("Case #%d: %d\n", c, counter);
   }
   return 0;
}
