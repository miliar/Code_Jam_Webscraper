#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;cin>>T;
  string s;
  for(int t=1;t<=T;t++){
    cin>>s;
    string ans;
    ans+=s[0];
    for(int i=1;i<s.size();i++){
      if(s[i]>=ans[0])
        ans.insert(0,1,s[i]);
      else
       ans+=s[i];
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
}