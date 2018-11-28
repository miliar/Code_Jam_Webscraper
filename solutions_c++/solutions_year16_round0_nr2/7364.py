#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char input[120];

int main(){
   int T;
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   scanf("%d",&T);
   for(int a=1;a<=T;a++){
      scanf("%s",input);
      printf("Case #%d: ",a);
      int panjang = strlen(input);
      int i;
      int flips=0;
      //char last;
         for(i=0;i<panjang;i++){
            if(input[i]=='-'){
               while(input[i]=='-'){
                  i++;
                  if(i>=panjang){
                     break;
                  }
               }
               i--;
               flips+=1;
            }
            else if(input[i]=='+'){
               while(input[i]=='+'){
                  i++;
                  if(i>=panjang){
                     break;
                  }
               }
               if(i<panjang){
                  flips+=1;
                  while(input[i]=='-'){
                  i++;
                     if(i>=panjang){
                        break;
                     }
                  }
                  i--;
                  flips+=1;
               }
            }
         }
      
      printf("%d\n",flips);
   }
   return 0;
}
