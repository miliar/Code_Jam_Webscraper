#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int main( void )
{
	int T, cnt = 1;
	freopen("test.in","rt",stdin);
	freopen("test.out","wt",stdout);
	scanf("%d",&T);
	while( T-- ) {
		unsigned long long M;
		int N, ans = 100000000;
		char win[ 100 ];
		scanf("%llu%d",&M, &N );
		int A[ N + 1 ];
		for( int i = 1; i <= N; i++ ) {
			scanf("%d",&A[ i ] );
		}
		sort( A + 1, A + N + 1 );
		if( M == 1 ) {
			printf("Case #%d: %d\n", cnt++ , N );
			continue;
		}
		for( int i = 0; i <= N; i++ ) {
			unsigned long long mass = M;
			int cost = 0;
			for( int j = 1; j <= i; j++ ) {
				while( mass <= A[ j ] ) {
					mass += mass - 1;
					cost++;
				}
				mass += A[ j ];
			}
			cost += N - i;
			ans = min( ans, cost );
		}
		printf("Case #%d: %d\n",cnt++, ans);
	}
	return 0;
}
