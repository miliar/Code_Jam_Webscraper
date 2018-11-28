#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int test;
    int arr1[4][4]={0}, arr2[4][4]={0};
    int ans1, ans2, i,j, k, flag=0;
    int temp1[17]={0}, temp2[17]={0};
    int count=0;
    int cases=0;
    scanf("%d", &test);
    while(cases<test){
        for(i=0; i<17;i++){
            temp1[i]=0; temp2[i]=0;
        }
        count=0;
        scanf("%d", &ans1);
        for(i=0; i<4; i++){
           for(j=0;j<4;j++){
             scanf("%d", &arr1[i][j]);
            } 
        }
        scanf("%d", &ans2);
        for(i=0; i<4; i++){
           for(j=0;j<4;j++){
             scanf("%d", &arr2[i][j]);
            }
        }

        for(i=ans1-1, j=ans2-1, k=0; k<4; k++){
            //printf("Elements checking are :: Array 1 :: %d, Array 2 :: %d\n", arr1[i][k], arr2[i][k]);
            temp1[arr1[i][k]]=1;
            temp2[arr2[j][k]]=1;
        }
        for(i=0; i<17; i++){
            //printf("Temp1 :: %d Temp2 :: %d and i = %d\n",temp1[i], temp2[i], i);
             if(temp1[i]==temp2[i] && temp1[i]==1){
                count++;
                flag=i;
               // printf("Common elements found :: %d\n", flag);
            }
        }
        
        //printf("The count obtained is :: %d\n", count);
        switch(count){
            case 0: printf("Case #%d: Volunteer cheated!\n", cases+1);;
            break;
            case 1: printf("Case #%d: %d\n",cases+1,flag);
            break;
            default: printf("Case #%d: Bad magician!\n", cases+1);
        }
     cases++;
    }
    return 0;
}