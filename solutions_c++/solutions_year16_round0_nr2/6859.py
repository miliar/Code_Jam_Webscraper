#include <bits/stdc++.h>
using namespace std;

int main(){

  long long t;
  string s;
  cin>>t;
  for(int i=0;i<t;i++){
    cin>>s;
    long long ans=0,len=s.size();
    for(int j=1;j<len;j++){
      if(s[j]!=s[j-1]) ans++;
    }
    if(s[len-1]=='-') ans++;
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }
  return 0;
}
