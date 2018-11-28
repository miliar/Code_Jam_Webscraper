#include<iostream>
#include<string>
using namespace std;
int main(){
  int n;
  cin>>n;
  for(int i=1;i<=n;i++){
    string s;
    int a=1;
    cin>>s;
    for(int j=0;j<s.size()-1;j++){
      if(s[j]!=s[j+1])a++;
    }
    if(s[s.size()-1]=='+')a--;
    cout<<"Case #"<<i<<": "<<a<<endl;
  }
  return 0;
}
