#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int main ()
{
	int no_testcases;
	scanf("%d", &no_testcases);
	
	
	
	for (int ijk=0; ijk<no_testcases; ijk++) {
		int N,M;
		scanf("%d",&N);
		scanf("%d",&M);
		
		int lawn[N+1][M+1];
		
		int row_max[N+1];
		int col_max[M+1];
		
		for (int i=1; i<=N; i++) {
			row_max[i] = 0;
		}
		for (int i=1; i<=M; i++) {
			col_max[i] = 0;
		}
		
		for (int i=1; i<=N; i++) {
			for (int j=1; j<=M; j++) {
				scanf("%d",&lawn[i][j]);
				if (lawn[i][j] > row_max[i]) {
					row_max[i] = lawn[i][j];
				}
				if (lawn[i][j] > col_max[j]) {
					col_max[j] = lawn[i][j];
				}
			}
		}
		
		bool ans = true;
		for (int i=1; i<=N; i++) {
			for (int j=1; j<=M; j++) {
				if (lawn[i][j] != min(row_max[i],col_max[j])) {
					ans	= false;
					break;
				}
			}
			if (ans==false) {
				break;
			}
		}
		if (ans == false) {
			printf("Case #%d: NO\n",ijk+1);
			continue;
		}
		printf("Case #%d: YES\n",ijk+1);
	}
	
	return 0;
}