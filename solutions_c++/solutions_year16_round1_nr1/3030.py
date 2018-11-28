#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm> 
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main() {
  int T;
  cin >> T;
  string S;
  string res; 
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << i+1 << ": ";
    cin >> S;
    res = S[0];
    for ( string::iterator it = S.begin() + 1; it != S.end(); ++it) {
        char c = *it; 
        char d = res[0];
        if( d <= c ){
            res = c + res;
        }else{
            res = res+ c; 
        }
    }
    cout << res<< endl;
  }
  return 0;
}
