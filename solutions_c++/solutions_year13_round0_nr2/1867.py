#include<stdio.h>
#include<string.h>

int lawn[100][100];
int maxL[100], maxC[100];

int main(){
	int tc = 1, n, N, M;
	scanf("%d", &n);
	while(n--){
		scanf("%d %d", &N, &M);
		printf("Case #%d: ", tc++);
		memset(maxL,0,sizeof(maxL));
		memset(maxC,0,sizeof(maxC));
		for(int l = 0; l < N; l++)
			for(int c = 0; c < M; c++){
				scanf("%d", &lawn[l][c]);
				if(maxL[l] < lawn[l][c]) maxL[l] = lawn[l][c];
				if(maxC[c] < lawn[l][c]) maxC[c] = lawn[l][c];
			}
		int flag = 1;
		for(int l = 0; l < N && flag; l++)
			for(int c = 0; c < M && flag; c++)
				if(maxL[l] > lawn[l][c] && maxC[c] > lawn[l][c]) flag = 0;
				
		if(!flag) puts("NO");
		else puts("YES");
	}
	return 0;
}
