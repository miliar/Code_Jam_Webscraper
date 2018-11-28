#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int mod = 1000002013;

struct el
{
	int cnt, p;
	int tp;
	
	bool operator<( const el& e ) const
	{
		if ( p != e.p )
			return p < e.p;
		return tp < e.tp;
	}
};

int n, m;
int le;
el e[2048];

el st[1024];
int sbot, stop;

int main()
{
	int t, T;
	int i, j, k, p;
	scanf( "%d", &T );
	long long sm, ans;
	long long city;
	for ( t = 1; t <= T; t++ )
	{
		scanf( "%d %d", &n, &m );
		le = 0;
		city = 0;
		long long pr;
		for ( i = 0; i < m; i++ )
		{
			scanf( "%d %d %d", &j, &k, &p );
			
			pr = j;
			pr *= k;
			if ( pr >= mod ) pr %= mod;
			pr *= p;
			if ( pr >= mod ) pr %= mod;
			
//			printf( "RM_C %lld\n", pr );
			city += pr;
			if ( city >= mod ) city %= mod;

			e[le].cnt = p;
			e[le].tp = 0;
			e[le].p = j;
			le++;
			
			e[le].cnt = p;
			e[le].tp = 1;
			e[le].p = k;
			le++;
		}
		
		sort( e, e + le );
		
		stop = 0;
		sbot = 1;
		sm = 0;
		for ( i = 0; i < le; i++ )
		{
			if ( e[i].tp == 0 )
			{
				st[++stop] = e[i];
			//	printf( "ADD %d %d\n", e[i].p, e[i].tp );
			}
			else
			{
				//printf( "ELSE!\n" );
				while ( e[i].cnt > 0 )
				{
					int rm = min( e[i].cnt, st[stop].cnt );
					e[i].cnt -= rm;
					st[stop].cnt -= rm;
						
					pr = e[i].p;
					pr *= st[stop].p;
					if ( pr >= mod )
						pr %= mod;
					pr *= rm;
					if ( pr >= mod ) pr %= mod;

					//printf( "RM_T %lld :: %d %d\n", pr, e[i].p, st[stop].p );
					
					sm += pr;
					if ( sm >= mod )
						sm %= mod;

					if ( st[stop].cnt == 0 )
						stop--;
				}
			}
		}
		
		ans = city-sm + mod;
		if ( ans >= mod )
			ans %= mod;
		
		
		printf( "Case #%d: %lld\n", t, ans );
	}
	return 0;
}
