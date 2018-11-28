#include <iostream>
#include <fstream>
#include <limits>
#include <string>

typedef int Number;

Number find_n( std::string s, int k ) {
  if ( k == 0 )
    return -1;
  int res = 0;
  for ( int n = 0; n <= (int)s.size() - k; ++n ) {
    if ( s[n] == '-' ) {
      ++res;
      for ( int i = 0; i < k; ++i ) {
        s[n + i] = s[n + i] == '-' ? '+' : '-';
      }
    }
  }
  if ( s.find( '-' ) == std::string::npos )
    return res;
  return -1;
}

int main() {
  int t;
  std::ifstream is( "L:/cj17/A-large.in" );
  is >> t;
  int c = 1;
  while ( t-- > 0 ) {
    std::string s;
    is >> s;
    int k;
    is >> k;
    Number res = find_n( s, k );
    std::cout << "Case #" << c++ << ": ";
    if( res >= 0 )
      std::cout << res << std::endl;
    else
      std::cout << "IMPOSSIBLE" << std::endl;
  }
  return 0;
}