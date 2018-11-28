#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main(){

  int T,S,row;
  vector<int> row1(4);
  vector<int> row2(4);
    
  cin >> T;
  int a,b,c,d;

  for(int t=1; t<=T; t++){
    
    cin >> row;
    for(int i = 1;i<=4;i++){
   
      if(i == row){
        cin >> row1[0] >> row1[1] >> row1[2] >> row1[3];
      }else 
        cin >> a >> b >> c >> d;
    }
    
    cin >> row;
    for(int i = 1;i<=4;i++){
   
      if(i == row){
        cin >> row2[0] >> row2[1] >> row2[2] >> row2[3];
      }else 
        cin >> a >> b >> c >> d;
    }

    int count = 0;
    for(auto x:row1){

      auto it = find(row2.begin(),row2.end(),x);
      if(it != row2.end()){
        count++; 
        S=x;   
      }

    }

    if(count == 1)
      printf("Case #%d: %d\n",t,S);  
    else if(count == 0)
      printf("Case #%d: Volunteer cheated!\n",t);  
    else if(count > 1)
      printf("Case #%d: Bad magician!\n",t);  
 }

 return 0;
}

