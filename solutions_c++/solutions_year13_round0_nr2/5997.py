#include <stdio.h>

int main()
{
	int testCase;
	scanf("%d", &testCase);
	
	for (int t=1; t<=testCase; t++) {
		int N,M;
		scanf("%d %d", &N, &M);
		int height[101];
		for (int i=0;i<101;i++)
			height[i] = 0;
		int map[N][M], input[N][M], max;
		max = 0;
		for (int i=0;i<N;i++) {
			for (int j=0;j<M;j++) {
				scanf("%d", &input[i][j]);
				height[input[i][j]] = 1;
				if (input[i][j]>max) max = input[i][j];
			}
		}
		for (int i=0;i<N;i++) {
			for (int j=0;j<M;j++) 
				map[i][j] = max;
		}
		for (int h=100;h>=1;h--) {
			if (height[h]==1) {
				int i, j;
				for (i=0;i<N;i++) {
					for (j=0;j<M;j++) {
						if (input[i][j]>height[h])
							break;
					}
					if (j==M) {
						for (j=0;j<M;j++)
							map[i][j] = height[h];
					}
				}
				for (j=0;j<M;j++) {
					for (i=0;i<N;i++) {
						if (input[i][j]>height[h])
							break;
					}
					if (i==N) {
						for (i=0;i<N;i++)
							map[i][j] = height[h];
					}
				}
		/*
			for (int i=0;i<N;i++) {
				for (int j=0;j<M;j++)
					printf("%d ", map[i][j]);
				puts("");
			}
		*/
			}				
		}
	
		int i,j, flag;
		flag = 0;
		for (i=0;i<N;i++) {
			for (j=0;j<M;j++) {
				if (input[i][j]!=map[i][j])
					flag = 1;
			}
		}

		if (flag==0) 
			printf("Case #%d: YES\n", t);
		else 
			printf("Case #%d: NO\n", t);
	}

	return 0;
}
