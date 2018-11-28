#include <cstdio>

using namespace std;

int N, X;
int mem[10];

inline int func(int x) {
   while (x > 0) {
      mem[x % 10] = 1;
      x /= 10;
   }
   for(int j = 0 ; j < 10 ; j++) {
      if (mem[j] == 0) {
         return false;
      }
   }
   return true;
}

int main() {
   scanf("%d", &N);
   for(int i = 1 ; i <= N ; i++) {
      scanf("%d", &X);
      for(int j = 0 ; j < 10 ; j++) {
         mem[j] = 0;
      }
      if (X == 0) {
         printf("Case #%d: INSOMNIA\n", i);
      }
      else {
         int ans = 0;
         int lv = 0;
         while (lv < 10000000) {
            ans += X;
            if (func(ans)) {
               printf("Case #%d: %d\n", i, ans);
               break;
            }
            lv++;
         }
         if (lv == 10000000) {
            printf("Case #%d: INSOMNIA\n", i);
         }
      }
   }
   return 0;
}
