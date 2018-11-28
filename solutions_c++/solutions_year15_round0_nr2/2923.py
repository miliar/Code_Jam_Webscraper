#include<bits/stdc++.h>
using namespace std ;

long long  p[1000005] ;

long long dp[2005][2005] ;

int yes , d ;

int count1[100] ;

long long dp1()
{
    long long  ans = 0 ;
    for ( int i = 0 ; i < d  ; i++ )
    {
        ans = max( ans , p[i]) ;
    }
    return ans ;
}

int main()
{
   yes = 0 ;
   int t ;
   long long ans ;
   cin >> t ;
   for ( int x = 1 ; x <= t ; x++)
   {
       int odd = 0 ;
       ans = 5000 ;
       cin >> d ;
    //  memset ( count1 , 0 , sizeof( count1 )) ;

      for ( int i = 0 ; i < d ; i++)
      {
          cin >> p[i] ;
      }

  long long m1 = dp1() ;
  long long unit  = 0 ;
    for ( int i = 1 ; i <= m1 ; i++)
    {
         dp[i][d] = 0 ;
         unit = 0 ;
        for ( int j = 0 ; j < d ; j++)
        {
          if ( i >= p[j] )
          {
             if ( unit < p[j])
                unit = p[j] ;
             continue ;
          }
          else
          {
           if ( ( p[j] % i ) == 0  )
            {
             dp[i][d] += ( p[j] / i ) ;
             dp[i][d]-- ;
            }
            else
            {
                dp[i][d] += ( p[j] / i ) ;
            }
            if ( unit < i )
                unit = ( long long )( i ) ;
          }
        }
        dp[i][d] += unit ;
        //cout << dp[i][d] << endl
        ans = min ( ans , dp[i][d]) ;
   }
cout <<"Case #"<<x<<": "<<ans  << endl ;
}
return 0 ;
}

