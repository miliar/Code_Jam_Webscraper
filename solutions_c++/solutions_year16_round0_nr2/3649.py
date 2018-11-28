#include <vector>
#include <string>
#include <iostream>
using namespace std;

int doit(string s) {
  for(int i=1;i<s.size();i++) if(s[i]!=s[i-1]) {
    for(int j=0;j<i;j++) {
      if(s[j]=='-') s[j]='+';
      else s[j]='-';
    }
    return 1+doit(s);
  }
  if(s[0]=='-') return 1;
  return 0;
}

int main() {
  int tests;
  cin>>tests;
  for(int i=0;i<tests;i++) {
    string s;
    cin>>s;
    int ret=doit(s);
    cout<<"Case #"<<(i+1)<<": "<<ret<<endl;
  }
  return 0;
}
