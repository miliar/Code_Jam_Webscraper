#include <iostream>

using namespace std;

int main()
{
    int T , z , n  ;
    long long t , r  , i , j ;
    long long s ;

    cin >> T ;

    for ( z=1 ; z <= T ; z++) {
      cin >> r >> t ;
      s = 0 ; n= 0 ; i = r  ; j = r+1 ;
      while ( 1 ) {
          s = s +  ( j*j - i*i) ;
          if ( s > t ) break ;
          ++n ;
          i += 2 ; j+=2 ;


      }

      cout << "Case #" << z << ": " << n << endl ;

    }

    return 0;
}
