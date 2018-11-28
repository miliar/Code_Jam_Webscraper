#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<list>
#include<string>
#include<cstring>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
using namespace std;

#define MAX 1000

int test_case;
int N, M;
int grid[ MAX ][ MAX ];
int maxRow[ MAX ];
int maxCol[ MAX ];
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("outputB_Large.txt", "w", stdout);
	int i,j;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%d %d", &N, &M);
		memset( maxRow, 0, sizeof( maxRow ) );
		memset( maxCol, 0, sizeof( maxCol ) );
		for( i = 0; i < N; i ++ ) {
			for( j = 0; j < M; j ++ ) {
				scanf("%d", &grid[ i ][ j ]);
				if( grid[ i ][ j ] > maxRow[ i ] ) maxRow[ i ] = grid[ i ][ j ];
				if( grid[ i ][ j ] > maxCol[ j ] ) maxCol[ j ] = grid[ i ][ j ];
			}
		}


		bool ok = true;
		for( i = 0; i < N; i ++ ) {
			for( j = 0; j < M; j ++ ) {
				if( grid[ i ][ j ] == maxRow[ i ] || grid[ i ][ j ] == maxCol[ j ] ) {
					continue ;
				} else {
					ok = false;
				}
			}
		}

		if( ok ) printf("Case #%d: YES\n", caseId);
		else printf("Case #%d: NO\n", caseId);
	}
	return 0;
}