#include <iostream>
#include <string>
using namespace std;

int main(){
  int t;
  cin>>t;
  for(int j=1;j<=t;j++){
    string s,ans="";
    cin>>s;
    for(int i=0;i<(int)s.size();i++){
      if(s.substr(i,1)>=ans.substr(0,1)) ans= s.substr(i,1)+ans;
      else ans+=s.substr(i,1);
    }
    cout<<"Case #"<<j<<": "<<ans<<endl;
  }
  return 0;
}
