#include<iostream>

using namespace std;


long getMinFlip(string s){
  int minusGrp = 0;
  int isStartWithMinus = 0;
  for(int index = 0 ; index < s.length() ; index++){
    if(s[index] == '-'){
      if(index == 0){
        isStartWithMinus = 1;
      }
      else if(s[index - 1] != '-'){
        minusGrp++;
      }
    }
  }
  return (isStartWithMinus + 2*minusGrp);
}
// cout<<"Case #"<<_case<<": "<<"INSOMNIA"<<"\n";
// cout<<"Case #"<<_case<<": "<<lastNum<<"\n";

int main(){
  long t;
  cin>>t;
  long _case = 0;
  while(t--){
    _case++;
    string s;
    cin>>s;
    long minFlip = getMinFlip(s);
    cout<<"Case #"<<_case<<": "<<minFlip<<"\n";

  }
  return 0;
}
