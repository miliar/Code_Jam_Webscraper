#include <iostream>
using namespace std;
int main() {
  int t;
  cin>>t;
  for (int z = 1; z<=t;z++) {
    string s;
    cin>>s;
    int c = 0;
    if (s[s.size()-1]=='-') {
      c++;
    }
    for (int i=0;i<s.size()-1;i++) {
      if (s[i]!=s[i+1]) {
        c++;
      }
    }
    printf("Case #%d: %d\n", z, c);
  }
}
