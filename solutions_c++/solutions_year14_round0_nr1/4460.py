#include<iostream>
#include<stdio.h>
using namespace std;

int main(){

  int t,test = 0;
  scanf("%d",&t);
  int arr1[4][4],arr2[4][4];
  while(t--){
    test++;
    int ans1,ans2;
    scanf("%d",&ans1);
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
      scanf("%d",&arr1[i][j]);
      }
    }
     scanf("%d",&ans2);
     for(int i=0;i<4;i++){
     
       for(int j=0;j<4;j++){
       scanf("%d",&arr2[i][j]);
       }
     }
    int index,cnt = 0;
     for(int i=0;i<4;i++){
       for(int j=0;j<4;j++){
         if(arr1[ans1-1][i] == arr2[ans2-1][j]){
            index = i;
            cnt++;
          }
       }
     }
    if(cnt == 1){

      printf("Case #%d: %d\n",test,arr1[ans1-1][index]);

    }
    else if(cnt == 0){

      printf("Case #%d: Volunteer cheated!\n",test);
    }
    else{
      
      printf("Case #%d: Bad magician!\n",test);

    }

  }
}
