#include <iostream>
#include <string>
using namespace std;

int valid(string& s, int len) {
  for (int i=0; i<len; ++i)
    if (s[i]!='+')
      return 0;
  return 1;
}


void oper(string& s, int len) {
  int id;
  for (id=len-1; id>=0; --id)
    if (s[id]!='+')
      break;
  for (;id>=0; --id)
    s[id] = (s[id]=='+'? '-':'+');
}

int main() {
  int cas, T, len, res;
  string str;

  cin>>T;
  for (cas=1; cas<=T; ++cas) {
    cout<<"Case #"<<cas<<": "; cin>>str;
    len = str.length(); res = 0;
    while (!valid(str,len)) {
      oper(str,len);
      ++res;
    }
    cout<<res<<endl;
  }

  return 0;
}
