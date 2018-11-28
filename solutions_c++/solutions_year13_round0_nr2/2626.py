#include <cstdio>
#include <cmath>


int main(){
	freopen("C:\\googlecj\\B-small-attempt0.in", "r", stdin);
	freopen("C:\\googlecj\\B-small-attempt0.out", "w", stdout);
	int tc, M, N, i, j, k, caseNum=1, area[105][105];
	bool possible;

	scanf("%d", &tc);
	while(tc--){
		scanf("%d %d", &M, &N);
		for(i=0; i<M; i++){
			for(j=0; j<N; j++)
				scanf("%d", &area[i][j]);
		}

		possible = true;
		for(i=0; possible && i<M; i++){
			for(j=0; possible && j<N; j++){
				if(area[i][j]==1){
					for(k=0; k<M; k++)
						if(area[k][j]!=1)
							possible = false;

					if(!possible){
						possible = true;
						for(k=0; k<N; k++)
							if(area[i][k]!=1)
								possible = false;
					}
				}				
			}
		}

		if(possible)
			printf("Case #%d: YES\n", caseNum++);
		else
			printf("Case #%d: NO\n", caseNum++);
	}

	return 0;
}

