#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin>>t;
  for(int c=1; c<=t; c++) {
    string s;
    cin>>s;
    string str = "";
    str += s[0];
    string str1, str2;
    for(int i=1; i<s.length(); i++) {
      str1 = str + s[i];
      str2 = s[i] + str;
      if(str1 > str2) str = str1;
      else str = str2;
    }
    cout<<"Case #"<<c<<": "<<str<<endl;
  }
   return 0;
}
