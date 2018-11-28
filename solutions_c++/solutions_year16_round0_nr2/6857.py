#include<bits/stdc++.h>
using namespace std;

int main(){
  int T,ans,len;
  string s;
  char c;
  cin>>T;
  for(int i=0;i<T;i++){
    cin>>s;
    ans=0;
    c=s[0];
    len=s.size();
    for(int j=0;j<len;j++)
      if(c!=s[j])c=s[j],ans++;
    if(s[len-1]=='+')ans--;
    cout<<"Case #"<<i+1<<": "<<ans+1<<endl;
  }
  return 0;
}
