#include<cstdio>
#include<algorithm>
using namespace std;
double n[1005], k[1005];
int main ()
{
	int t;
	scanf ( "%d", &t );
	for ( int i = 1; i <= t; i ++ )
	{
		printf ( "Case #%d: ", i );
		int am;
		scanf ( "%d", &am );
		for ( int j = 0; j < am; j ++ ) scanf ( "%lf", &n[j] );
		for ( int j = 0; j < am; j ++ ) scanf ( "%lf", &k[j] );
		sort ( n, n + am );
		sort ( k, k + am );
		int p = 0, p2 = 0;
		int kr = 0;
		for ( int j = 0; j < am; j ++ )
		{
			if ( n[j] > k[kr] ) 
			{
				p ++;
				kr ++;
			}
		}
		kr = 0;
		for ( int j = 0; j < am; j ++ )
		{
			while ( kr < am and n[j] > k[kr] ) kr ++;
			if ( kr == am ) p2 ++;
			else kr ++;
		}
		printf ( "%d %d\n", p, p2 );
	}
	return 0;
}
			
		