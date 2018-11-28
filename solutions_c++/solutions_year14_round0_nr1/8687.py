#include <cstdio>
#include <algorithm>
#include <cstring>

#define MAXN 4

using namespace std;

int occ[ MAXN + 1 ][ MAXN * MAXN + 1 ];
int grid[ MAXN + 1 ][ MAXN + 1 ];

int main( void )
{
	int T;
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	scanf("%d", &T );
	for( int k = 0; k < T; k++ ) {
		int c, z, ans = 0, cnt = 0;
		memset( occ, 0, sizeof( occ ) );
		scanf("%d", &c );
		for( int i = 1; i <= MAXN; i++ ) {
			for( int j = 1; j <= MAXN; j++ ) {
				scanf("%d", &grid[ i ][ j ] );
				occ[ i ][ grid[ i ][ j ] ]++;
			}
		}
		scanf("%d", &z );
		for( int i = 1; i <= MAXN; i++ ) {
			for( int j = 1; j <= MAXN; j++ ) {
				scanf("%d", &grid[ i ][ j ] );
				if( i == z ) {
					if( occ[ c ][ grid[ i ][ j ] ] > 0 ) {
						ans = grid[ i ][ j ];
						cnt++;
					}
				}
			}
		}
		printf("Case #%d: ", k + 1 );
		if( cnt == 0 ) printf("Volunteer cheated!\n");
		else if( cnt > 1 ) printf("Bad magician!\n");
		else printf("%d\n", ans );
	}
	return 0;
}
