#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

#define AB 256

using namespace std;

string A[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int occ[ AB + 1 ];

bool find( int k ) {
  string K = A[ k ];
  int newocc[ AB + 1 ] = { 0 };
  for( int i = 0; i < K.length(); i++ ) {
    newocc[ K[ i ] ]++;
    if( newocc[ K[ i ] ] > occ[ K[ i ] ] ) return false;
  }
  for( int i = 0; i < AB; i++ ) occ[ i ] -= newocc[ i ];
  return true;
}

int main( void ) {
  int T;
  freopen("A.txt","rt",stdin);
  freopen("Aout.txt","wt",stdout);
  cin >> T;
  for( int t = 1; t <= T; t++ ) {
    memset( occ, 0, sizeof( occ ) );
    string S;
    cin >> S;
    cout << "Case #" << t << ": ";
    for( int bit = 0; bit < ( 1 << 10 ); bit++ ) {
      bool valid = true;
      int number[ 10 ] = { 0 };
      memset( occ, 0, sizeof( occ ) );
      for( int i = 0; i < S.length(); i++ ) occ[ ( int )S[ i ] ]++;
      bool status = false;
      do {
        status = false;
        for( int i = 0; i < 10; i++ ) {
          if( bit & ( 1 << i ) ) {
            if( find( i ) ) {
              number[ i ]++;
              status = true;
            }
          }
        }
      } while( status );
      for( int i = 0; i < AB; i++ ) if( occ[ i ] ) valid = false;
      if( valid ) {
        for( int i = 0; i < 10; i++ ) {
          for( int j = 0; j < number[ i ]; j++ ) {
            cout << i;
          }
        }
        cout << endl;
        break;
      }
    }
  }
  return 0;
}
