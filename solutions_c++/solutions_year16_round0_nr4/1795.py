#include <algorithm>
#include <string>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void sheep(int n);
int main() {
  int t, k,c,s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> k >> c >> s;  // read n and then m.
    cout << "Case #" << i << ": " ;
    for( int j = 1; j<=k; ++j){
        cout<<j<<" ";
    }
    cout<<endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
