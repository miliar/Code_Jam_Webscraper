#include <stdio.h>

int main(){
   int T;
   int x, r, c, flg;
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      scanf("%d%d%d", &x, &r, &c);
      if(x == 1) flg = 1;
      else if(x == 2){
         if(r*c % 2) flg = 0;
         else flg = 1;
      }
      else if(x == 3){
         if(r<3 && c<3) flg = 0;
         else if(r*c==3 || r*c%3) flg = 0;
         else flg = 1;
      }
      else{
         if(r<4 && c<4) flg = 0;
         else if(r*c <= 8) flg = 0;
         else flg = 1;
      }
      if(flg == 0) printf("Case #%d: RICHARD\n", t);
      else printf("Case #%d: GABRIEL\n", t);
   }

   return 0;
}
