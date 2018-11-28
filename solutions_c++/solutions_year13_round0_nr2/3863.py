#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <memory.h>
using namespace std;

#define MAXN 101

int main()
{
	int cases;
	int casenum = 1;
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);

	int N, M;
	int lawn[ MAXN ][ MAXN ];
	bool isYes;

	scanf("%d", &cases);
	while(cases--)
	{
		isYes = true;
		scanf("%d%d", &N, &M);

		// IO
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				scanf("%d", &lawn[i][j]);
			}
		}

		// search
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				int h = lawn[ i ][ j ];
				bool legalrow = true;
				bool legalcol = true;

				// check row
				for(int k = 0; k < N; k++){
					if( lawn[ k ][ j ] > h ) {
						legalrow = false;
						break;
					}
				}
				// check col
				for(int k = 0; k < M; k++){
					if( lawn[ i ][ k ] > h ) {
						legalcol = false;
						break;
					}
				}
				if( !legalrow && !legalcol ){
					isYes = false;
					break;
				}
			}
		}

		if( isYes ) printf("Case #%d: YES\n", casenum++);
		else		printf("Case #%d: NO\n", casenum++);

	}
	return 0;
}

