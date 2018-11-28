#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){

int T;
scanf("%d",&T);
for(int c=1;c<=T;c++){
        int flag=0;
        int arr;
        int card[10][10]={-1},card2[10][10]={-1};
        int r1,r2;
        scanf("%d",&r1);
        for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        scanf("%d",&card[i][j]);
                }
        }
        scanf("%d",&r2);
        for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        scanf("%d",&card2[i][j]);
                }
        }
        
        for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        if(card[r1-1][i]==card2[r2-1][j]){
                        arr = card[r1-1][i];
                        flag++;
                        }
                }
        }
        if(flag==0){
        printf("Case #%d: Volunteer cheated!\n",c);
        
        }
        else if(flag==1){
        printf("Case #%d: %d\n",c,arr);
        }
        else{
             printf("Case #%d: Bad magician!\n",c);
        
        }
                
      
}



return 0;
}
