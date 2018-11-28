#include <algorithm>
#include <string>
#include <utility>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;

int motes[ 1000014 ];
int n;

int t ( int curr, int pos )
{
  int res = 0;
  while ( pos != n )
  {
    if ( curr >= 1000000 ) return res + ( n - pos );
    while ( motes[ pos ] < curr && pos < n && curr < 1000000 ) 
    {
      curr += motes[ pos++ ]; 
    }
    if ( pos != n )
    {
      int p;
      if ( 2 * curr - 1 != curr ) p = t( 2 * curr - 1, pos );
      else p = 500000;
      int q = t( curr, pos + 1 );
      return min( p, q ) + res + 1;
    }
  }
  return res;
}

int main ( int argc, char * argv [] )
{
  int cases;
  scanf( "%d", &cases );
  for ( int z = 1; z <= cases; z++ )
  {
    int a;
    scanf( "%d%d", &a, &n );
    for ( int i = 0; i < n; i++ )
    {
      scanf( "%d", &motes[ i ] ); 
    }
    sort( motes, motes + n );
    printf( "Case #%d: %d\n", z, t( a, 0 ) ); 
  }
  
  return 0;
}