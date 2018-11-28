#include <stdio.h>
#include <string.h>
#include <math.h>

long long int poww(long long int n, long long int l)
{
    if(l==0)return 1;
    long long int ans=1;
    for(long long int i=0;i<l;i++)ans*=n;
    //cout<<ans<<"pww";
    return ans;
}
long long int radixChange(char* data, int num){
   int len = strlen(data);
   int i;
   long long int ans = 0;
   for(i = 0; i < len; i++){
      if(data[i] == '1')
         ans += poww(num, len-i-1);
   }
   return ans;
}

int main(){
   int tc, count;
   int n, j, i, k, isAns;
   FILE* fp = fopen("output.txt", "w");
   char data[33];
   long long int ans[9];
   long long int rad, rrad;

   scanf("%d", &tc);

   for(count = 0; count < tc; count++){
      scanf("%d%d", &n, &j);
      data[0] = '1';
      for(i = 1; i < n; i++)
         data[i] = '0';
      data[i] = 0;
      data[i-1] = '1';

      printf("Case #%d:\n", count+1);
      fprintf(fp, "Case #%d:\n", count+1);
      while(j > 0){
         for(i = 0; i < 9; i++)
            ans[i] = 0;
         isAns = 1;
         data[n-2]++;
         for(i = n; i > 0; i--){
            if(data[i] == '2'){
               data[i] = '0';
               data[i-1]++;
            }
         }

         for(i = 2; i < 11; i++){
            rad = radixChange(data, i);
            rrad = sqrt(rad) + 2;
            if(rad%2 == 0){
               ans[i-2] = 2;
               continue;
            }
            for(k = 3; k < rrad; k+=2){
               if(rad%k == 0){
                  ans[i-2] = k;
                  break;
               }
            }
         }

         for(i = 0; i < 9; i++){
            if(ans[i] == 0){
               isAns = 0;
               break;
            }
         }

         if(isAns != 0){
            j--;
            printf("%s", data);
            fprintf(fp, "%s", data);
            for(i = 0; i < 9; i++){
               printf(" %d", ans[i]);
               fprintf(fp, " %d", ans[i]);
            }
            printf("\n");
            fprintf(fp, " \n");
         }

      }
   }
}
