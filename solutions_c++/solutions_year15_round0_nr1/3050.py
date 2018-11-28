#include<bits/stdc++.h>
using namespace std ;
int main()
{
  int t , m1 ;
  long long  extra , ans ;
  cin >> t ;
  string s ;
  for ( int x = 1 ; x <= t ; x++)
  {
      extra = ans = 0 ;
      cin >> m1 ;
      cin >> s ;
      long long sum[m1+5] ;

      sum[0] = s[0] - '0' ;

      for ( int i = 1 ; i <= m1 ; i++)
      {
          if ( sum[i-1] >= i )
          {
             sum[i] = sum[i-1] + ( s[i] - '0' ) ;
          }
          else
          {
           ans = i - sum[i-1] ;
           extra += ans ;
           sum[i] = sum[i-1] + ( s[i] - '0' ) + ( ans ) ;
          }
      }
      cout <<"Case #"<<x<<": "<<extra << endl ;

  }

return 0 ;
}
