#include <iostream>
#include <cstdio>
using namespace std;
int main() {
  int m;
  cin>>m;
  for(int i=1;i<=m;i++) {
    int n;
    string s;
    int o=0,c=0;
    cin>>n>>s;
    for (int j=0;j<s.size();j++) {
      if (c<j && s[j]>'0') {
        o+=j-c;
        c=j;
      }
      c+=s[j]-'0';
    }
    printf("Case #%d: %d\n",i,o);
  }
  return 0;
}
