#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
double a[10000], b[10000];
int main()
{
	int cas;
	int cc = 0;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		int n;
		scanf( "%d", &n );
		for ( int i = 0; i < n; i++ )
			scanf( "%lf", &a[i] );
		for ( int i = 0; i < n; i++ )
			scanf( "%lf", &b[i] );
		sort( a, a + n );
		sort( b, b + n );
		int j = 0;
		int t1 = 0;
		int t2 = 0;
		for ( int i = 0; i < n; i++ )
		{
			if ( a[i] > b[j] )
			{
				t1++;
				j++;
			}
		}
		j = 0;
		for ( int i = 0; i < n; i++ )
		{
			while ( j < n && a[i] > b[j] ) j++;
			if ( j >= n ) t2++;
			j++;
		}
		cc++;
		printf("Case #%d: %d %d\n", cc, t1, t2 );
	}

	return 0;
}
