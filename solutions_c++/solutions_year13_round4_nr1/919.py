#include <stdio.h>
#include <iostream>

int T;
int N, M;
int ans[101];
int oa, na;

int main()
{
	scanf( "%d", &T );
	for( int p = 0; p < T; ++p )
	{
		for( int i = 1; i <= 100; ++i )
			ans[i] = 0;
		oa = na = 0;
		scanf( "%d %d", &N, &M );
		for( int j = 0; j < M; ++j )
		{
			int n, m, p;
			scanf( "%d %d %d", &n, &m, &p );
			oa += ((-(m-n)*(m-n-1))/2+(m-n)*N)*p;
			for( int k = n+1; k <= m; ++k )
				ans[k] += p;
		}
		while( true )
		{
			int fnz = 0, lnz = 0;
			int mi = 0x7fffffff;
			for( int i = 2; i <= N; ++i )
				if( ans[i] != 0 )
				{
					fnz = i;
					break;
				}
			if( fnz == 0 )
				break;
			for( int i = fnz; i <= N; ++i )
			{
				if( ans[i] == 0 )
				{
					lnz = i-1;
					break;
				}
				mi = mi < ans[i] ? mi : ans[i];
			}
			if( lnz == 0 )
				lnz = N;
			na += ((-(lnz-fnz+1)*(lnz-fnz))/2+(lnz-fnz+1)*N)*mi;
			for( int i = fnz; i <= lnz; ++i )
				ans[i] -= mi;
		}
		printf( "Case #%d: %d\n", p+1, oa-na );
	}
	return 0;
}