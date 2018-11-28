#include <stdio.h>
#include <stdlib.h>

int main(){
   int T;
   int set1[5][5];
   int set2[5][5];
   int ans1;
   int ans2;
   int ansRow1[5];
   int ansRow2[5];
   freopen("A-small-attempt3.in","r",stdin);
   freopen("aya.out","w",stdout);
   scanf("%d",&T);
   for(int a=1;a<=T;a++){
      int same=0;
      int sameval=-1;
      scanf("%d",&ans1);
      for(int i=0;i<4;i++){
         for(int j=0;j<4;j++){
            scanf("%d",&set1[i][j]);
         }
      }
      for(int i=0;i<4;i++){
         ansRow1[i]=set1[ans1-1][i];
      }
      scanf("%d",&ans2);
      for(int i=0;i<4;i++){
         for(int j=0;j<4;j++){
            scanf("%d",&set2[i][j]);
         }
      }
      for(int i=0;i<4;i++){
         ansRow2[i]=set2[ans2-1][i];
      }
      for(int i=0;i<4;i++){
         for(int j=0;j<4;j++){
            if(ansRow1[i]==ansRow2[j]){
               same+=1;
               sameval=ansRow1[i];
               if(same>1){
                  printf("Case #%d: Bad magician!\n",a);
                  break;
               }
            }
         }
         if(same>1){
            //printf("Case #%d: Bad magician!\n",a);
            break;
            }
      }
      if(same==0){
         printf("Case #%d: Volunteer cheated!\n",a);
      }
      if(same==1){
         printf("Case #%d: %d\n",a,sameval);
      }
   }
   return 0;
}
