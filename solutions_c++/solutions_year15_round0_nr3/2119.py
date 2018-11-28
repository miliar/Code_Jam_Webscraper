#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

#define pb push_back

#define MAXN 10100

using namespace std;

struct let {
  char X;
  int S;
};

int X, L;
string S;

bool operator==( let A, let B ) {
  if( A.X == B.X && A.S == B.S ) return true;
  return false;
}

let multiply( let A, let B ) {
  let c;
  int newS = A.S * B.S;
  if( A.X == '1' && B.X == '1' ) c = ( let ) { '1', 1 };
  if( A.X == 'i' && B.X == '1'  ) c = ( let ) { 'i', 1 };
  if( A.X == 'j' && B.X == '1' ) c = ( let ) { 'j', 1 };
  if( A.X == 'k' && B.X == '1' ) c = ( let ) { 'k', 1 };

  if( A.X == '1' && B.X == 'i' ) c = ( let ) { 'i', 1 };
  if( A.X == 'i' && B.X == 'i'  ) c = ( let ) { '1', -1 };
  if( A.X == 'j' && B.X == 'i' ) c = ( let ) { 'k', -1 };
  if( A.X == 'k' && B.X == 'i' ) c = ( let ) { 'j', 1 };

  if( A.X == '1' && B.X == 'j' ) c = ( let ) { 'j', 1 };
  if( A.X == 'i' && B.X == 'j'  ) c = ( let ) { 'k', 1 };
  if( A.X == 'j' && B.X == 'j' ) c = ( let ) { '1', -1 };
  if( A.X == 'k' && B.X == 'j' ) c = ( let ) { 'i', -1 };

  if( A.X == '1' && B.X == 'k' ) c = ( let ) { 'k', 1 };
  if( A.X == 'i' && B.X == 'k'  ) c = ( let ) { 'j', -1 };
  if( A.X == 'j' && B.X == 'k' ) c = ( let ) { 'i', 1 };
  if( A.X == 'k' && B.X == 'k' ) c = ( let ) { '1', -1 };

  c.S *= newS;
  return c;
}


vector< int > idx;
bool suffix[ MAXN + 1 ];

int main( void ) {
  int T;
  freopen("test.in","rt",stdin);
  freopen("test.out","wt",stdout);
  cin >> T;
  for( int t = 0; t < T; t++ ) {
    string A;
    cin >> X >> L >> A;
    for( int i = 0; i < L; i++ ) {
      S.append( A );
    }

    bool status = false;
    let val = ( let ) { S[ 0 ], 1 };
    if( val == ( let ) { 'i', 1 } ) idx.pb( 0 );
    for( int i = 1; i < X * L; i++ ) {
      val = multiply( val, ( let) { S[ i ], 1 } );
      if( val == ( let ) { 'i', 1 } ) idx.pb( i );
    }
    val = ( let ) { S[ X * L - 1 ], 1 };
    if( val == ( let ) { 'k', 1 } ) suffix[ X * L - 1 ] = true;
    for( int i = X * L - 2; i >= 0; i-- ) {
      val = multiply( ( let ) { S[ i ], 1 }, val );
      if( val == ( let ) { 'k', 1 } ) {
        suffix[ i ] = true;
      }
    }
    for( int i = 0; i < idx.size(); i++ ) {
      int id = idx[ i ] + 1;
      val = ( let ) { S[ id ], 1 };
      for( int j = id + 1; j < S.length(); j++ ) {
        if( val == ( let ) { 'j', 1 } && suffix[ j ] ) {
          status = true;
          break;
        }
        val = multiply( val, ( let ) { S[ j ], 1 } );
      }
      if( status ) break;
    }
    cout << "Case #" << t + 1 << ": " << ( status ? "YES": "NO" ) << '\n';
    idx.clear();
    memset( suffix, 0, sizeof( suffix ) );
    S.clear();
  }
  return 0;
}
