#include<iostream>
using namespace std;
int main(){
  
  int T;
  cin>>T;
  for(int i = 0 ;i < T; i++){
    int ans, next_ans;
    int mat_1[4][4], mat_2[4][4];
    cin>>ans;
    for(int m = 0; m < 4; m++ ){
      for(int n = 0; n < 4; n++){
	cin>>mat_1[m][n];
      }
    }
    cin>>next_ans;
    for(int m = 0; m < 4; m++ ){
      for(int n = 0; n < 4; n++){
	cin>>mat_2[m][n];
      }
    }
    
    //input ended
    int count = 0,key; 
    for(int j = 0; j < 4 ;j++ ){
      for(int k = 0; k < 4 ;k++){
	if(mat_1[ans-1][j] == mat_2[next_ans-1][k]){
	  count++;
	  key = mat_1[ans-1][j];
	}
      }
    }
    if(count > 1)
      cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    else if(count == 0)
      cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    else
      cout<<"Case #"<<i+1<<": "<<key<<endl;
  }
  return 0;
}