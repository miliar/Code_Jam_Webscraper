#include<cstdio>
#include<algorithm>
using namespace std;
int lawn[100][100];
int rowmaxh[100];
int colmaxh[100];
int main(){
	int tests;
	scanf("%d", &tests);
	for(int t = 1; t <= tests; t++){
		int N, M;
		scanf("%d %d", &N, &M);
		for(int i = 0; i < N; i++)
			rowmaxh[i] = 1;
		for(int i = 0; i < M; i++)
			colmaxh[i] = 1;
		for(int i = 0; i < N; i++)
			for(int j = 0; j < M; j++){
				scanf("%d", &lawn[i][j]);
				rowmaxh[i] = max(rowmaxh[i], lawn[i][j]);
				colmaxh[j] = max(colmaxh[j], lawn[i][j]);
			}
		bool possible = true;
		for(int i = 0; i < N; i++)
			for(int j = 0; j < M; j++){
				if(lawn[i][j] != min(rowmaxh[i], colmaxh[j]))
					possible = false;
			}
		printf("Case #%d: %s\n", t, possible?"YES":"NO");
	}
		
}
