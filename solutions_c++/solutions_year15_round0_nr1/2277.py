#include <stdio.h>

int main(){
   int T, n, sum, ans;
   char s[10001];
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      scanf("%d", &n);
      scanf("%s", s);
      sum = ans = 0;
      for(int i=0; i<=n; ++i){
         if(i > sum){
            ans += (i-sum);
            sum = i;
         }
         sum += (s[i]-'0');
      }
      printf("Case #%d: %d\n", t, ans);
   }
}
