#include <stdio.h>

int board[100][100];

bool isPossible(int h, int w)
{
	for(int i=0; i<h; i++) {
		for(int j=0; j<w; j++) {
			bool bRow = true, bCol = true;

			// check row
			for(int k=0; k<w; k++) {	
				if (board[i][k] > board[i][j]) {
					bRow = false;
					break;
				}
			}

			// check column
			for(int k=0; k<h; k++) {
				if (board[k][j] > board[i][j]) {
					bCol = false;
					break;
				}
			}

			if (!bRow && !bCol) return false;
		}
	}

	return true;
}

int main()
{
	int t;

	scanf("%d", &t);

	for(int c=1; c<=t; c++) 
	{
		int N, M;

		scanf("%d %d", &N, &M);

		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				scanf("%d", &board[i][j]);
			}
		}

		printf("Case #%d: %s\n", c, isPossible(N, M) ? "YES" : "NO");
	}

	return 0;
}
