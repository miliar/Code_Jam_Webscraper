#include<iostream>
#include<string>
using namespace std;
int main(void){
  int T;
  cin>>T;
  for(int Ti=1;Ti<=T;Ti++){
    string S;
    cin>>S;
    string res = S.substr(0,1);
    S.erase(S.begin());
    while(S.size()){
      if(res[0]<=S[0]){
        res = S.substr(0,1) + res;
      }else{
        res += S.substr(0,1);
      }
      S.erase(S.begin());
    }
    
    
    cout<<"Case #"<<Ti<<": "<<res<<endl;

  }
}
