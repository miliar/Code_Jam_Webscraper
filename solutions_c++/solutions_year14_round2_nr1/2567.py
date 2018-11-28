#include<cstdio>
#include<algorithm>
using namespace std;
char x[105][105];
int gdzie[105], ile[105];
int f ( int n )
{
	int sum = 0, ans = 0;
	for ( int i = 1; i <= n; i ++ )
	{
		gdzie[i] = 0;
		ile[i] = 0;
	}
	char c = x[1][0];
	while ( c )
	{
		sum = 0;
		for ( int i = 1; i <= n; i ++ )
		{
			while ( x[i][gdzie[i]] == c ) 
			{
				gdzie[i] ++;
				ile[i] ++;
			}
			sum += ile[i];
			if ( ile[i] == 0 ) return -1;
		}
		c = x[1][gdzie[1]];
		int a[2];
		a[0] = sum / n;
		a[1] = a[0] + 1;
// 		printf ( "a: %d, %d\n", a[0], a[1] );
		int ret[2];
		ret[0] = 0; ret[1] = 0;
		for ( int i = 1; i <= n; i ++ )
		{
			ret[0] += abs ( ile[i] - a[0] );
			ret[1] += abs ( ile[i] - a[1] );
			ile[i] = 0;
		}
		ans += min ( ret[0], ret[1] );
// 		printf ("ans: %d\n", ans );
	}
	for ( int i = 1; i <= n; i ++ ) if ( x[i][gdzie[i]] ) return -1;
	return ans;
}
int main ()
{
	int t;
	scanf ( "%d", &t );
	for ( int tt = 1; tt <= t; tt ++ )
	{
		printf ( "Case #%d: ", tt );
		int n;
		scanf ( "%d", &n );
		for ( int i = 1; i <= n; i ++ ) scanf ( " %s", x[i] );
		int p = f ( n );
		if ( p == -1 ) puts ( "Fegla Won" );
		else printf ( "%d\n", p );
	}
	return 0;
}