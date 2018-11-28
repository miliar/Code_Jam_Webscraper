#include <cstdio>
#include <cmath>

using namespace std;

bool palin( int i )
{
	int arr[ 150 ], size = 0;
	while( i > 0 ) {
		arr[ size++ ] = i % 10;
		i /= 10;
	}
	for( int i = 0; i < size; i++ ) {
		if( arr[ i ] != arr[ size - i - 1 ] ) {
			return false;
		}
	}
	return true;
}

int main( void )
{
	freopen("test.in","rt",stdin);
	freopen("test.out","wt",stdout);
	int T;
	scanf("%d",&T);
	for( int z = 1; z <= T; z++ ) {
		int N,M,ans = 0,start = N;
		scanf("%d%d",&N,&M);
		for( int i = N ; i > 0; --i ) {
			if( i*i >= N ) {
				start = i;
			}
		}
		for( int i = start; i*i <= M; i++ ) {
			if( palin( i ) && palin( i*i ) ) {
				ans++;
			}
		}
		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}
