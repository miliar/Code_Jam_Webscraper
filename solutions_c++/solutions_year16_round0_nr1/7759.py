#include <bits/stdc++.h>
using namespace std ;

long long n , t , ck[15] , k , x , cse ;

int main()
{
    freopen( "A-large.txt", "r+" , stdin ) ;
    freopen( "A-large-at.txt", "w+", stdout ) ;
    cin >> t ;
    while(t-- )
    {
           cin >>  n ;
           long long p = 0 ;
           int f = 1 ;
           memset( ck, 0 , sizeof(ck) ) ;
           while( p < 100 )
           {
               p++ ;
               k = n * p ;
               //cout << "k = " << k << endl ;

               while( k )
               {
                   x = k%10 ;
                   ck[x] = 1 ;
                   k = k / 10 ;
               }
               f = 1 ;

               for( int i = 0 ; i < 10 ; i++ )
               {
                   if( ck[i] == 0 )
                   {
                       f = 0 ;
                       break ;
                   }
               }
               k = p * n ;
               if( f )
               {
                   printf("Case #%d: ", ++cse ) ;
                   cout << k << endl ;
                   break ;
               }
           }
           if( !f )printf("Case #%d: INSOMNIA\n", ++cse ,p*n ) ;

    }




return 0 ;
}
