#include <iostream>
#include <fstream>
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
#define sor(x) sort(x.begin(),x.end())
#define rsor(x) sort(x.rbegin(),x.rend())
#define sys_p system( "pause" )
#define End return 0
#define pb push_back 
#define mp make_pair

typedef long long LL ;

ifstream Cin("input.txt");
ofstream Cout( "output.txt" );

LL Is_p[1001], Num[1001] = {} ;

bool is_p( LL x )
{
      string t ; LL i ;
      while( x ) t += char( '0' + x%10 ) , x /= 10 ;
      FOR0( i, t.length()/2 ) if( t[i] != t[ t.length() - i - 1 ] ) return false ;
      return true ;
}

bool good( LL x )
{
      LL sq = (LL)sqrt( x ) ; if( sq*sq != x ) return false ;
      return Is_p[ sq ] ;
}

main()
{ 
      LL i, T, t, a, b ; FOR1( i, 1000 ) Is_p[i] = is_p(i) ; FOR1( i, 1000 ) if( Is_p[i] && good(i) ) Num[i] = Num[i-1] + 1 ; else Num[i] = Num[i-1] ;
      Cin >> T ; 
      FOR1( t, T )
      {
        Cin >> a >> b ; Cout << "Case #" << t << ": " << Num[b] - Num[a-1] << endl ;
      }
} 

