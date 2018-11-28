#include <stdio.h>
#include <stdlib.h>

long long int aya, temp;
bool list[10], result;

void init(){
   result = false;
   aya = 0;
   temp =0;
   int i;
   for(i=0;i<10;i++){
      list[i] = false;
   }
}

bool check(){
   int i;
   for(i=0;i<10;i++){
      if(list[i] == false){
         return false;
      }
   }
   return true;
}

int main(){
   int T;
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   scanf("%d",&T);
   for(int a=1;a<=T;a++){
      int N;
      scanf("%d",&N);
      printf("Case #%d: ",a);
      if(N==0){
         printf("INSOMNIA\n");
      }
      else{
         init();
         int i=0;
         
         while(1){
            i+=1;
            aya = i *N;
            temp = aya;
            while(temp>0){
               int a = temp%10;
               temp/=10;
               list[a] = true;
               result = check();
               if(result){
                  break;
               }
               else{
                  continue;
               }
            }
            if(result){
               break;
            }
            else{
               continue;
            }
         }
         printf("%d\n",aya);
      }
   }
   return 0;
}
