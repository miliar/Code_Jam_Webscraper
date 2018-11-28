#include<stdio.h>
#include<stdlib.h>

int main(){
    freopen("A-small-attempt3.in","r",stdin);
    freopen("out.txt","w",stdout);
    int round;
    int rowchosed;
    int number[4][4];
    int penampung[2][4];
    int flag;
    int result;
    scanf("%d",&round);
    if(round<1 || round>100)scanf("%d",&round);
    for(int i=0;i<round;i++){
        flag=0;
        for(int m=0;m<2;m++){
            scanf("%d",&rowchosed);
            if(rowchosed<1 || rowchosed>4)scanf("%d",&rowchosed);
            for(int j=0;j<4;j++){
                for(int k=0;k<4;k++){
                    scanf("%d",&number[j][k]);
                }
            }
            for(int l=0;l<4;l++)penampung[m][l] = number[rowchosed-1][l];
        }
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                if(penampung[0][j] == penampung[1][k]){
                    flag+=1;
                    result=penampung[0][j];
                }
            }
        }
        if(flag>1)printf("Case #%d: Bad Magician!\n",i+1);
        else if(flag==1)printf("Case #%d: %d\n",i+1,result);
        else if(flag<1)printf("Case #%d: Volunteer Cheated!\n",i+1);
    } 
    return 0;
}
