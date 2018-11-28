#include <iostream>
#include <cmath>
#include <cstdio>


using namespace std;

int main()
{
    int cbeg[32] ,  c ,  i , l , num ;
    int T , z;
    unsigned long long  A, B , beg , tmp  ;
    long double d ;
    bool flag ;


    cin >> T ;

    for ( z=1 ; z <= T ; z++ ) {
      cin >> A >> B ;

      d = A ;
      beg = sqrt ( d ) ;

      while ( beg * beg < A ) ++beg ;

      num = 0 ;
      while ( beg*beg <= B ) {
          tmp = beg ; c = 0 ;
          while ( tmp > 0 ) {
            cbeg[c] = tmp % 10 ;
            tmp = tmp / 10 ;
            ++c ;
          }
          l = c / 2 ;   flag = true  ;
          for ( i=0 ; i < l ; i++ )
            if ( cbeg[i] != cbeg[c-1-i]) {
               flag = false ;
               break ;
            }
          if ( flag == false ) {
            ++beg ;
            continue ;
          }

          tmp = beg * beg ; c = 0 ;

          while ( tmp > 0 ) {
            cbeg[c] = tmp % 10 ;
            tmp = tmp / 10 ;
            ++c ;
          }

          l = c / 2 ;
          for ( i=0 ; i < l ; i++ )
            if ( cbeg[i] != cbeg[c-1-i]) {
               flag = false ;
               break ;
            }
          if ( flag == true  )  ++num ;
            //cout << "num " << beg << "  num * num " << beg * beg << endl ;
          ++beg ;
       }
       cout << "Case #" << z <<": " << num << endl ;
      }
    return 0;
}
