#include<cstdio>
#include<algorithm>
using namespace std;
int p[1005];
int main ()
{
  int z;
  scanf ( "%d", &z );
  for ( int t = 1; t <= z; t ++ ) 
  {
	int d;
	scanf ( "%d", &d );
	for ( int i = 1; i <= d; i ++ ) scanf ( "%d", &p[i] );
	int maxi = 1005;
	for ( int r = 1; r <= 1000; r ++ )
	{
	  int ans = r;
	  for ( int i = 1; i <= d; i ++ ) ans += ( p[i] - 1 ) / r ;
	  maxi = min ( maxi, ans );
	}
	printf ( "Case #%d: %d\n", t, maxi );
  }
  return 0;
}