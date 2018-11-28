#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

string itos( int x ) {
  ostringstream os;
  os << x;
  return os.str( );
}

bool pali( int x ) {
  string a = itos( x ), b = a;;
  reverse( a.begin( ), a.end( ) );
  return a == b;
}

int main( ) {
  freopen( "input.txt", "r", stdin );
  freopen( "output.txt", "w", stdout );
  
  int T, A, B, C;
  cin >> T;
  
  for( int cs = 1; cs <= T; ++cs ) {
    C = 0;
    cin >> A >> B;
    
    for( int x = A; x <= B; ++x ) {
      int sq = sqrt( x );
      if( sq*sq != x ) continue;
      if( pali( x ) && pali( sq ) ) {
        C++;
      }
    }
    
    cout << "Case #" << cs << ": " << C << endl;
  }
  
  return 0;
}
  
  
  