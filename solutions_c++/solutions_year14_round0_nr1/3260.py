#include <stdio.h>
#include <iostream>
#include <cstdlib>

int main(){
    int T,count=0,sol;
    int r[2];
    int a[2][4][4];

    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        count=0;
        for(int j=0;j<2;j++){
            scanf("%d",&r[j]);
            for(int k=0;k<4;k++){
                for(int m=0;m<4;m++){
                    scanf("%d",&a[j][k][m]);
                }
            }
        }
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                if(a[0][r[0]-1][j]==a[1][r[1]-1][k]){
                    count++;
                    sol=a[0][r[0]-1][j];
                }
            }
        }
        if(count==1){
            printf("Case #%d: %d\n",i,sol);
        }else if(count>1){
            printf("Case #%d: Bad magician!\n",i);
        }else if(count==0){
            printf("Case #%d: Volunteer cheated!\n",i);
        }
    }
}
