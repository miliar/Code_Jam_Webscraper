#include <bits/stdc++.h>
using namespace std ;


int t , n , ans , f , cse ;
string s ;
int main()
{
    freopen("B-large.txt", "r", stdin ) ;
    freopen( "B_lans.txt", "w+", stdout ) ;

     cin >> t ;

     while( t-- )
     {
         cin >> s ;
         n = s.size() ;
         ans  = 0 ;
         f = 0 ;
         for( int i = 0 ; i < n-1 ; i++ )
         {
             if( s[i] != s[i+1] ) ans ++ ;
         }
         if( s[n-1] == '-' ) ans++ ;
         printf("Case #%d: ", ++cse ) ;
         cout << ans << endl ;

     }





    return 0 ;
}
