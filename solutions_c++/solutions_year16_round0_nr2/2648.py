#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

typedef unsigned long long ulong;
using namespace std;

int min_turn_count(const string& s) {
  char curchar;
  size_t idx = 0;
  int swaps = 0;
  while (idx < s.length() ) {
    curchar = s[idx];
    while ( idx < s.length() && s[idx] == curchar )
      idx++;
    if ( idx == s.length() ) {
      if ( s.back() == curchar && curchar == '-' ) {
        swaps++;
      }
    } else {
      swaps++;
    }
  }
  return swaps;
}

int main(void) {
  int T;
  cin >> T;
  string s;
  for (int i=0; i < T; i++) {
    cin >> s;
    int  mcount = min_turn_count( s );
    cout << "Case #" << i + 1 << ": " << mcount << endl;
  }
}
