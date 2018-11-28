#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<queue>
#include<map>
using namespace std;

int state[1<<20];

int key[25][205];
int Ki[25];
int lock[25];
int initKey[205];

int main()
{
	int T;
	int N, K;
	scanf("%d", &T);
	int Case = 1;
	while ( T-- ) {
		memset(initKey,0,sizeof(initKey));
		memset(key,0,sizeof(key));
		scanf("%d%d", &K, &N);
		for ( int i = 0 ; i < K ; i++ ) {
			scanf("%d", &initKey[i]);
		}
		for ( int i = 0 ; i < N ; i++ ) {
			scanf("%d%d", &lock[i], &Ki[i]);
			for ( int j = 0 ; j < Ki[i] ; j++ ) {
				scanf("%d", &key[i][j]);
			}
		}
		
		memset(state,-1,sizeof(state));
		queue<int> Q;
		Q.push((1<<N)-1);
		while ( !Q.empty() ) {
			int now = Q.front();
			Q.pop();
			for ( int i = 0 ; i < N ; i++ ) {
				if ( (now>>i) & 1 ) {
					int next = now&~(1<<i);
					if ( state[next] == -1 || state[next] > i ) {
						map<int, int> nowKey;
						for ( int j = 0 ; j < K ; j++ ) {
							nowKey[initKey[j]]++;
						}
						for ( int j = 0 ; j < N ; j++ ) {
							if ( (next>>j) & 1 ) {
								for ( int k = 0 ; k < Ki[j] ; k++ ) {
									nowKey[key[j][k]]++;
								}
							}
						}
						int open = 1;
						for ( int j = 0 ; j < N && open ; j++ ) {
							if ( (now>>j) & 1 ) {
								nowKey[lock[j]]--;
								if ( nowKey[lock[j]] < 0 )
									open = 0;
							}
						}
						if ( open ) {
							if ( state[next] == -1 )
								Q.push(next);
							state[next] = i;
						}
					}
				}
			}
		}
		
		if ( state[0] == -1 )
			printf("Case #%d: IMPOSSIBLE\n", Case++);
		else {
			printf("Case #%d:", Case++);
			int now = 0;
			for ( int i = 0 ; i < N ; now |= 1<<state[now] , i++ ) {
				printf(" %d", state[now]+1);
			}
			printf("\n");
		}
	}
	return 0;
}
