#include <bits/stdc++.h>
#include <string>
using namespace std;
 int main() {
  int t;
  cin>>t;
  int res;
  for(int c=1; c<=t; c++) {
    string str;
    string flip;
    cin>>str;
    stack<char> s;
    for(int i=0; i<str.length(); i++) {
      s.push(str[i]);
    }
    res = 0;
    while(str.find('-') != string::npos) {
      size_t found = str.find_last_of('-');
        flip = str.substr(0, found+1);
        for(int i=0; i<flip.size(); i++) {
          if(flip[i] == '+') flip[i] = '-';
          else flip[i] = '+';
        }
        str.replace(0, flip.length(), flip);

      res++;
    }
    cout<<"Case #"<<c<<": "<<res<<endl;
  }


   return 0;
 }
