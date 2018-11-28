#include <iostream>
using namespace std;
int main( void )
{
  int T,X,R,C;
  cin >> T;
  for( int ti=1; ti<=T; ti++ ){
    cin >> X >> R >> C;
    int ret = 0;
    if( X == 1 ) ret = 1;
    if( X == 2 && (R*C) % 2 == 0 ){
      ret = 1;
    }
    if( X == 3 && (R*C) % 3 == 0 ) {
      if( R > 1 && C > 1 ) ret = 1;
    }
    if( X == 4 && (R*C) % 4 == 0 ){
      if( R >= 4 && C >= 3 ) ret = 1;
      if( R >= 3 && C >= 4 ) ret = 1;
    }
    if( ret ){
      cout << "Case #" << ti << ": GABRIEL" << endl;
    } else {
      cout << "Case #" << ti << ": RICHARD" << endl;
    }
  }
}
