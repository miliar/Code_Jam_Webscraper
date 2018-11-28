/*
 * =====================================================================================
 *
 *       Filename:  lawnmover.cc
 *
 *    Description:  Lawnmover
 *
 *        Version:  1.0
 *        Created:  04/13/2013 04:06:51 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Jan Sebechlebsky (js), sebecjan@fit.cvut.cz
 *        Company:  Faculty of Information Technology, CTU Prague
 *
 * =====================================================================================
 */

#include <cstdlib>
#include <cstdio>

int main() {
	int T,M,N;
	int map[100][100];
	int mask[100][100];
	scanf("%d",&T);
	for( int c = 1; c <= T; c++ ) {
		scanf("%d%d",&M,&N);
		for( int i = 0; i < M; i++ ) {
			for( int j = 0; j < N; j++ ) {
				scanf("%d",&map[i][j]);
				//printf("%d ",map[i][j]);
			}
			//putchar('\n');
		}

		bool res = true;

		for(int h = 1; h <= 100; h++ ) {
			int sumc = 0;
			for( int i = 0; i < M; i++ ) {
				for( int j = 0; j < N; j++ ){ 
					if(map[i][j]==h)sumc++;
						mask[i][j] = 0;
				}
			}
			//printf("sumc=%d\n",sumc);
			int counter = 0;
			//Count rows
			for( int i = 0; i < M; i++ ) {
				if( map[i][0] == h ) {
					int hc = 0;
					for(int j = 0; j < N; j++ ) {
						if( map[i][j] == h ) hc++;
					}
					if( hc == N) {
						for( int j = 0; j < N; j++ )
							mask[i][j] = 1;
					}
				}
			}

			for( int i = 0; i < N; i++ ) {
				if( map[0][i] == h ) {
					int hc = 0;
					for( int j = 0; j < M; j++ ) {
						if( map[j][i] == h ) hc++;
					}
					if( hc == M ) {
						for( int j = 0; j < M; j++ )
						mask[j][i] = 1;
					}
				}
			}
			
			//for( int i = 0; i < M; i++ ) {
			//	for( int j = 0; j < N; j++ ) {
			//		printf("%d ",mask[i][j]);
			//	}
			//	printf("\n");
			//}

			for( int i = 0; i < M; i++ )
				for( int j = 0; j < N; j++)
					counter += mask[i][j];

			//printf("counter = %d\n",counter);
			if( counter == sumc ) {
				for( int i = 0; i < M; i++ ) {
					for( int j = 0; j < N; j++ ) {
						if( map[i][j] == h ) {
							map[i][j]++;
						}
					}
				}
			} else {
				res = false;
			}
		}
		if(res) {
			printf("Case #%d: YES\n",c);	
		} else {
			printf("Case #%d: NO\n",c);
		}
	}
	return 0;
}

