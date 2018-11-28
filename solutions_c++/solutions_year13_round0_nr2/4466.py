#include <stdio.h>

#define max(a, b) ((a)>(b)?(a):(b))
#define min(a, b) ((a)<(b)?(a):(b))

int N, M;
int map[100][100];
int row[100], col[100];
int ans;

int main(void){
	int T, t;
	int i, j;
	
	scanf("%d", &T);
	for (t=1; t<=T; t++){
		scanf("%d%d", &N, &M);
		for (i=0; i<N; i++) for (j=0; j<M; j++) scanf("%d", &map[i][j]);

		for (i=0; i<N; i++){
			row[i] = map[i][0];
			for (j=1; j<M; j++) row[i] = max(row[i], map[i][j]);
		}

		for (j=0; j<M; j++){
			col[j] = map[0][j];
			for (i=1; i<N; i++) col[j] = max(col[j], map[i][j]);
		}

		for (i=0; i<N; i++){
			for (j=0; j<M; j++){
				if (map[i][j]!=min(row[i], col[j]))
					break;
			}
			if (j<M) break;
		}
		if (i<N) printf("Case #%d: NO\n", t);
		else printf("Case #%d: YES\n", t);
	}
	return 0;
}

