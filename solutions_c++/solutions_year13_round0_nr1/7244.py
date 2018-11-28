#include <cstdio>

int T;
char A[5][5];

int main()
{
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);
	scanf("%d%*c",&T);
	int t;
	for(t = 1; t <= T; t++)
	{
		int i,j,cnt;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
				scanf("%c",&A[i][j]);
			scanf("%*c");
		}
		scanf("\n");
		for(i = 0; i < 4; i++)
		{
			//X won
			cnt = 0;
			j = 0;
			while (A[i][j] == 'X' || A[i][j] == 'T')
			{
				cnt++;
				j++;
			}
			if (cnt == 4)
			{
				printf("Case #%d: X won\n",t);
				goto test;
			}
			cnt = 0;
			j = 0;
			while (A[j][i] == 'X' || A[j][i] == 'T')
			{
				cnt++;
				j++;
			}
			if (cnt == 4)
			{
				printf("Case #%d: X won\n",t);
				goto test;
			}
			//O won
			cnt = 0;
			j = 0;
			while (A[i][j] == 'O' || A[i][j] == 'T')
			{
				cnt++;
				j++;
			}
			if (cnt == 4)
			{
				printf("Case #%d: O won\n",t);
				goto test;
			}
			cnt = 0;
			j = 0;
			while (A[j][i] == 'O' || A[j][i] == 'T')
			{
				cnt++;
				j++;
			}
			if (cnt == 4)
			{
				printf("Case #%d: O won\n",t);
				goto test;
			}
		}
		//X diagonals
		i = 0; 
		j = 0;
		cnt = 0;
		while (A[i][j] == 'X' || A[i][j] == 'T')
		{
			cnt++;
			i++;
			j++;
		}
		if (cnt == 4)
		{
			printf("Case #%d: X won\n",t);
			goto test;
		}
		i = 0;
		j = 3;
		cnt = 0;
		while (A[i][j] == 'X' || A[i][j] == 'T')
		{
			cnt++;
			i++;
			j--;
		}
		if (cnt == 4)
		{
			printf("Case #%d: X won\n",t);
			goto test;
		}
		//O diagonals
		i = 0;
		j = 0;
		cnt = 0;
		while (A[i][j] == 'O' || A[i][j] == 'T')
		{
			cnt++;
			i++;
			j++;
		}
		if (cnt == 4)
		{
			printf("Case #%d: O won\n",t);
			goto test;
		}
		i = 0;
		j = 3;
		cnt = 0;
		while (A[i][j] == 'O' || A[i][j] == 'T')
		{
			cnt++;
			i++;
			j--;
		}
		if (cnt == 4)
		{
			printf("Case #%d: O won\n",t);
			goto test;
		}
		bool notFinished = false;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
				if (A[i][j] == '.')
				{
					notFinished = true;
					break;
				}
			if (notFinished)
			{
				printf("Case #%d: Game has not completed\n",t);
				goto test;
			}
		}
		printf("Case #%d: Draw\n",t);
		test : 
		{
		}
	}
	return 0;
}