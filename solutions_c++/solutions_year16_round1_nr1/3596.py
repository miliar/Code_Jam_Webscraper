#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  string s;
  cin>>n;
  for(int i=1;i<=n;i++){
    string a;
    cin>>s;
    a=s[0];
    for(int j=1;j<s.size();j++){
      if(a[0]<=s[j])a=s[j]+a;
      else a+=s[j];
    }
    cout<<"Case #"<<i<<": "<<a<<endl;
  }
  return 0;
}
