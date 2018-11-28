#include <cstdio>
#include <algorithm>

using namespace std;

int main( void )
{
	freopen("test.in","rt",stdin);
	freopen("test.out","wt",stdout);
	int T;
	scanf("%d",&T);
	for( int z = 1; z <= T; z++ ) {
		int N,M;
		scanf("%d%d",&N,&M);
		bool status = true;
		int grid[ N ][ M ];
		for( int i = 0; i < N; i++ ) {
			for( int j = 0; j < M; j++ ) {
				scanf("%d",&grid[ i ][ j ] );
			}
		}
		for( int i = 0; i < N; i++ ) {
			for( int j = 0; j < M; j++ ) {
				bool case1 = false, case2 = false;
				for( int k = 0; k < N; k++ ) {
					if( grid[ k ][ j ] > grid[ i ][ j ] ) {
						case1 = true;
					}
				}
				for( int k = 0; k < M; k++ ) {
					if( grid[ i ][ k ] > grid[ i ][ j ] ) {
						case2 = true;
					}
				}
				if( case1 && case2 ) {
					status = false;
				}
			}
		}
		printf("Case #%d: ",z);
		if( status ) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}		
	}
	return 0;
}
