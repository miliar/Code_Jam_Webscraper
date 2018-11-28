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

LL n, m, r[101][101], max_row[101], max_col[101] ;

main()
{ 
      LL T, t ;
      Cin >> T ;
      FOR1( t, T )
      {
        LL i, j, k ; Cin >> n >> m ; 
        FOR1( i, n ) FOR1( j, m ) Cin >> r[i][j] ;
        FOR1( i, 100 ) max_row[i] = max_col[i] = 0 ;
        FOR1( i, n ) FOR1( j, m ) max_row[i] = max( max_row[i], r[i][j] ) ;
        FOR1( j, m ) FOR1( i, n ) max_col[j] = max( max_col[j], r[i][j] ) ;
        Cout << "Case #" << t << ": " ;
        FOR1( i, n )
        {
          FOR1( j, m ) if( r[i][j] != max_row[i] && r[i][j] != max_col[j] ) break ; 
          if( j != m+1 )
            break ;
        }    
        if( i == n+1 && j == m+1 ) Cout << "YES" ;
        else Cout << "NO" ;
        Cout << endl ;
      }
} 

