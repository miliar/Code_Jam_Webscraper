#include <iostream>

using namespace std;

int main()
{
    int T , N , M ;
    int z , i , j , k , s ;
    int a[101][101] ;
    bool d ;
    cin >> T ;

    for ( z=1 ; z <= T ; z++){
      cin >> N >> M ;
      for ( i=0 ; i < N ; i++)
        for ( j=0 ; j < M ; j++)
         cin >> a[i][j];
    /*
      cout <<endl << endl ;
      for ( i=0 ; i < N ; i++) {
        cout << endl ;
        for ( j=0 ; j < M ; j++)
         cout << a[i][j];

      }
    */

       d = true ;
       for ( i=0 ; i < N ; i++) {
        if ( d == false )  break ;
        for ( j=0 ; j < M ; j++) {
          if ( d == false )  break ;

             s = 0 ;
             for ( k=0 ; k < M ; k++ )
               if ( a[i][j] < a[i][k] )  {
                   //cout << "trace 1 i = " << i << " j =  " <<  j  << " k = " << k << endl ;
                   ++s ;
                   break ;
               }
             for ( k=0 ; k < N ; k++ )
                if ( a[i][j] < a[k][j] )  {
                   //cout << "trace 2 i = " << i << " j =  " <<  j  << " k = " << k << endl ;
                   ++s ;
                   break ;
                }
             if ( s == 2 ) {
                 d = false ;
                 break ;
            }
        }
       }


        if ( d == true )
          cout << "Case #" << z << ": YES"  << endl ;
        else
          cout << "Case #" << z << ": NO"  << endl ;
    }

    return 0;
}
