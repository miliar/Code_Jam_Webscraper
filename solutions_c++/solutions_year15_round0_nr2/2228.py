#include <stdio.h>

int a[10001];

int main(){
   int T, n;
   int maxnum, tmp, ans;
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      scanf("%d", &n);
      for(int i=0; i<n; ++i){
         scanf("%d", &a[i]);
         if(a[i] > maxnum) maxnum = a[i];
      }
      ans = maxnum;
      for(int k=1; k<=maxnum; ++k){
         tmp = 0;
         for(int i=0; i<n; ++i) tmp += (a[i]-1)/k;
         if(k+tmp < ans) ans = k+tmp;
      }
      printf("Case #%d: %d\n", t, ans);
   }

   return 0;
}
