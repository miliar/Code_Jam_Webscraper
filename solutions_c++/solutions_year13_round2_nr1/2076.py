#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
using namespace std;

#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define sys_p system( "pause" )
#define End return 0
#define pb push_back 
#define mp make_pair

typedef long long LL ;

ifstream Cin( "input.txt" );
ofstream Cout( "output.txt" );

LL pow2( LL st )
{
      LL x = 1 ;
      while( st ) x *= 2, st -= 1 ;
      return x ;
}

main()
{
      LL T, t ;
      Cin >> T ;
      FOR1( t, T )
      {
            LL cur, n, i, ind = 0, ans = 0 ;
            Cin >> cur >> n ; vector < LL > r(n) ;
            FOR0( i, n ) Cin >> r[i] ; sort( r.begin(), r.end() ) ;
            if( cur == 1 ) { ans = n ; }
            else
            while( ind < (LL)r.size() ) 
            {
              //cout << ind << " " << cur << " " << ans << endl ; 
              if( cur > r[ind] ) 
              {
                cur += r[ind] ; ind++ ;
              }
              else
              {
                LL case1 = (LL)r.size() - ind, case22 ;
                double case2 = (r[ind]-1.0)*1.0/(cur-1.0) ; case2 = log(case2) / log(2.0) ; case22 = (LL)( case2 ) + 1 ;
                //cout << case1 << " " << case22 << endl ;
                if( case1 <= case22 )
                {
                  ans += case1 ; break ;
                }
                else
                {
                  ans += case22 ; cur = pow2(case22) * ( cur-1 ) + 1 ;
                  cur += r[ind] ; ind++ ;
                }
              }
            }
            Cout << "Case #" << t << ": " << ans << endl ; 
      }
      //sys_p ;
} 
