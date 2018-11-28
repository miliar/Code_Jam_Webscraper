#include <iostream>
#include <string>
using namespace std;

int main() {
  int cas, T;
  string s, res;

  cin>>T;
  for (cas=1; cas<=T; ++cas) {
    cin>>s; res="";
    res += s[0];
    for (int i=1; i<s.length(); ++i) {
      if (s[i]>=res[0]) res = s[i] + res;
      else res += s[i];
    }
    cout<<"Case #"<<cas<<": "<<res<<endl;
  }

  return 0;
}
