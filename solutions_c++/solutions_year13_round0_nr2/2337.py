#include<stdio.h>
#include<string.h>

int v[105][105];
int map[105][105];
int main()
{
	int T;
	int N, M;
	scanf("%d", &T);
	int Case = 1;
	while ( T-- ) {
		scanf("%d%d", &N, &M);
		memset(v,0,sizeof(v));
		
		for ( int i = 1 ; i <= N ; i++ ) {
			for ( int j = 1 ; j <= M ; j++ ) {
				scanf("%d", &map[i][j]);
			}
		}
		int ans = 1;
		for ( int h = 1 ; h <= 100 && ans ; h++ ) {
			for ( int i = 1 ; i <= N ; i++ ) {
				int check = 1;
				for ( int j = 1 ; j <= M && check ; j++ ) {
					if ( !v[i][j] && map[i][j] > h )
						check = 0;
				}
				if ( check ) {
					for ( int j = 1 ; j <= M ; j++ ) {
						v[i][j] = 1;
					}
				}
			}
			
			for ( int i = 1 ; i <= M ; i++ ) {
				int check = 1;
				for ( int j = 1 ; j <= N && check ; j++ ) {
					if ( !v[j][i] && map[j][i] > h )
						check = 0;
				}
				if ( check ) {
					for ( int j = 1 ; j <= N ; j++ ) {
						v[j][i] = 1;
					}
				}
			}
			
			for ( int i = 1 ; i <= N && ans ; i++ ) {
				for ( int j = 1 ; j <= M ; j++ ) {
					if ( map[i][j] == h && !v[i][j] ) {
						ans = 0;
						break;
					}
				}
			}
		}
		
		if ( ans )
			printf("Case #%d: YES\n", Case++);
		else
			printf("Case #%d: NO\n", Case++);
	}
	
	return 0;
}
