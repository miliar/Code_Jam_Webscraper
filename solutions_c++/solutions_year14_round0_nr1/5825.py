#include <stdio.h>

int R[2], G[2][4][4];

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int t = 1; t <= T; t++)
	{
		for(int i = 0; i < 2; i++)
		{
			scanf("%d", R + i); R[i]--;
			for(int r = 0; r < 4; r++)
				for(int c = 0; c < 4; c++)
					scanf("%d", &G[i][r][c]);
		}
		
		int cnt = 0, card = -1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(G[0][R[0]][i] == G[1][R[1]][j])
					cnt ++, card = G[0][R[0]][i];
					
		if(cnt == 1)
			printf("Case #%d: %d\n", t, card);
		else if(cnt > 1)
			printf("Case #%d: Bad magician!\n", t);
		else
			printf("Case #%d: Volunteer cheated!\n", t);
		
		
	}
	
	
	return 0;
}
