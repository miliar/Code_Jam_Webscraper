#include <stdio.h>
#include <string.h>

long long table[100000], tablen;

bool ispalin(long long int in){
   char str[50];
   sprintf(str, "%lld", in);
   
   int len = strlen(str);
   for(int i = 0, j = len-1; i < j; i++, j--){
      if(str[i] != str[j]) return false;
   } 
   return true;
}

int main(){
   for(long long int trying = 1; trying <= 10000000; trying++){
      if( ispalin(trying) ){
         long long sq = trying * trying;
         if( ispalin(sq) ) table[tablen++] = sq;
      }
   }
    
   int test, ti = 1;
   long long a, b;
   scanf("%d", &test);
   
   while( test-- && scanf("%lld%lld", &a, &b) ){
      int ans = 0;
      for(long long int i = 0; i < tablen; i++){
         if(table[i] >= a && table[i] <= b) ans++;
      }
      printf("Case #%d: %d\n", ti++, ans);
   }

   return 0;
}
