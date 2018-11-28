#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
const char p = '+';
const char m = '-';
int main() {
  int T,res;
  string s;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << i+1 << ": ";
    res = 0 ;
    cin >> s;
    char tmp = s[0];
    for ( string::iterator it = s.begin() + 1; it != s.end(); ++it) {
      char c = *it;
      if ( c != tmp ){
        ++res;
      }
      tmp = c;
    }
    if(s[0] == m ){
      if(res % 2 == 0 ) ++res;
    }else{
      if(res % 2 == 1 ) ++res;
    }

    cout << res << endl;


  }
  return 0;
}
