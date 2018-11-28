#include<iostream>
#include<string>
using namespace std;
int main(){
 int t,s,fr,aud,i,temp;
 string str;
 cin>>t;
 for(int j=1;j<=t;++j){
  cin>>s>>str;
  fr=0;
  aud=(int)(str[0]-48);
  for(i=1;i<=s;++i){
   temp=(int)(str[i]-48);
   if(temp>0 && i>aud){
    fr+=(i-aud);
    aud+=fr;
   }
   aud+=temp;
  }
  cout<<"Case #"<<j<<": "<<fr<<endl;
 }
 return 0;}
