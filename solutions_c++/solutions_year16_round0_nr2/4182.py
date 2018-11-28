#include<iostream>
using namespace std;
int f(string str){
  str+="+";
  int i = str.size()-1;
  while(i>0&&str[i]=='+')i--;
  int cnt=0;
  while(i >= 0){
    if(str[i]!=str[i+1])cnt++;
    i--;
  }
  return cnt;
}
      
    
int main(void){
  int T;
  string str;
  cin>>T;
  for(int i = 1;i<=T;i++){
    cin>>str;
    cout<<"Case #"<<i<<": "<<f(str)<<endl;

  }
  return 0;
}
