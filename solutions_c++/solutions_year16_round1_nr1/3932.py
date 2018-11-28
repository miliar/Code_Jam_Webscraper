#include<iostream>
#include<vector>

using namespace std;

int main(){

  int T;
  cin >> T; 
  vector<string> s(T);
  for(int i=0;i<T;i++){
    cin>> s[i]; 
  }
  vector<string> o(T);
  for(int i=0;i<T;i++){
    for(auto it:s[i]){
      if(o[i].length()==0){
        o[i]+=it;
      }else{
        if(o[i][0]<=it){
          o[i]=it+o[i];
        }else{
          o[i]+=it;
        }
      }
    }
  }
//output
  for(int i=0;i<T;i++){
    cout<<"Case #"<<i+1<<": "<<o[i]<<endl;
  }

}
