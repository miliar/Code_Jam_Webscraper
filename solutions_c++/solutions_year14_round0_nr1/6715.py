#include <iostream>
#include <cstdio>

using namespace std;

void getdata(int data[4][4]){
  for(int i=0;i<4;++i){
    for(int j=0;j<4;++j){
      scanf("%d", &data[i][j]);
    }
  }
}

int checkdata(int a1[][4], int a2[][4], int c1, int c2, int& ans){
  int count=0;
  for(int i=0;i<4;++i){
    int digit = a1[c1][i];
// cout<<"checking from a1 "<<digit<<endl;
    for(int j=0;j<4;++j){
      if(digit == a2[c2][j]) {
        ans = a2[c2][j];
        count++;
      }
    }
  }
 //cout<<"returning "<<count<<endl;
  return count;
} 

main(){
  int t;
  scanf("%d",&t); 
  int a1[4][4]; 
  int a2[4][4]; 
  for(int k=1;k<=t;++k) {
    int c1, c2;
    scanf("%d", &c1);
    getdata(a1);
    scanf("%d", &c2);
    getdata(a2);
    int ans;
    int output = checkdata(a1, a2, c1-1, c2-1, ans);
    printf("Case #%d: ", k);
    switch(output){
      case 1: 
        printf("%d\n", ans);
        break;
      case 2: 
      case 3: 
      case 4: 
        printf("Bad magician!\n");
        break;
      case 0: 
        printf("Volunteer cheated!\n");
        break;
    }
  }
}

