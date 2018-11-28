#include <stdio.h>
#include <string.h>

int N,M;
int board[100][100];

int isOK() {
	int ok = 0;

	for(int i = 0; i < N ; i++) {
		for (int j = 0; j < M ; j++)
		{
			ok = 1;
			for (int k = 0; k < N ; k++)
			{
				if (board[i][j] < board[k][j])
				{
					ok = 0;
					break;
				}
			}
			if (ok == 1)
			{
				continue;
			}
			ok = 1;
			for (int k = 0; k < M ; k++)
			{
				if (board[i][j] < board[i][k])
				{
					ok = 0;
					break;
				}
			}
			if (ok == 0)
			{
				return 0;
			}
		}
	}

	return 1;
}

int main() {
	int T;
	char c;
	scanf("%d\n", &T);
	for (int k = 1 ; k <= T ; k++)
	{
		memset(board, 0 , sizeof(board));
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N ; i++)
		{
			for (int j = 0 ; j < M; j++)
			{
				scanf("%d", &board[i][j]);
			}
		}
		c = isOK();
	
		printf("Case #%d: ", k);
		if (c)
		{
			printf("YES\n");
		}else
			printf("NO\n");
	}
	return 0;
}