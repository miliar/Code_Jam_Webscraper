#include <cstdio>
#include <cstring>

int n;
long long p;

int maxRounds( long long a )
{
	int r = 0;
	long long k = 1;
	
	while ( a >= k )
	{
		//a -= k;
		r++;
		k = k + k + 1;
	}
	
	return r;
}

long long maxRank( int loss )
{
	long long ans = 0;
	for ( int i = 1; i <= loss; i++ )
	{
		ans += (1LL<<(n-i));
	}
	return ans;
}

long long minRank( int win )
{
	long long ans = 0;
	for ( int i = win+1; i <= n; i++ )
	{
		ans += (1LL<<(n-i));
	}
	return ans;
}

int main()
{
	int t, T;
	long long le, ri, mi;
	long long gar, could;
	scanf( "%d", &T );
	for ( t = 1; t <= T; t++ )
	{
		scanf( "%d %lld", &n, &p );
		
		le = 0; ri = (1LL<<n);
		while ( le + 1 < ri )
		{
			mi = (le+ri)/2;
			if ( maxRank( maxRounds( mi ) ) >= p )
				ri = mi;
			else
			{
//				printf( "winner %lld %d\n", mi, maxRounds( mi ) );
				le = mi;
			}
		}
		gar = le;
		
		le = 0; ri = (1LL<<n);
		while ( le + 1 < ri )
		{
			mi = (le+ri)/2;
			if ( minRank( maxRounds( (1LL<<n)-1-mi ) ) >= p )
				ri = mi;
			else
				le = mi;
		}
		could = le;
		printf( "Case #%d: %lld %lld\n", t, gar, could );
	}
	return 0;
}
