#include<cstdio>
#include<cstring>

#define MAX 100

short lawn[MAX][MAX];
short rows[MAX];
short cols[MAX];

int main()
{
	int T; scanf("%d", &T);
	for(int ii = 0; ii < T; ii++)
	{
		int N, M;
		scanf("%d%d",&N,&M);
		for(int i = 0; i < N; i++)
			for(int j = 0; j < M; j++)
				scanf("%hd", lawn[i]+j);
		for(int i = 0; i < N; i++)
		{
			rows[i] = 0;
			for(int j = 0; j < M; j++)
				if(rows[i] < lawn[i][j])
					rows[i] = lawn[i][j];
		}
		for(int j = 0; j < M; j++)
		{
			cols[j] = 0;
			for(int i = 0; i < N; i++)
				if(cols[j] < lawn[i][j])
					cols[j] = lawn[i][j];
		}
		bool good = true;
		for(int i = 0; i < N && good; i++)
			for(int j = 0; j < M; j++)
				if(lawn[i][j] != rows[i] && lawn[i][j] != cols[j])
				{
					good = false;
					break;
				}
		printf("Case #%d: %s\n",ii+1,(good)?"YES":"NO");
	}
	return 0;
}
