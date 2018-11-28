#include <cstdio>



int main(void)
{
	int casis;
	int row;
	int Board[4][4];
	int fCase[4];
	int sCase[4];
	int result;
	int i, j, k;

	freopen("A-small-attempt0.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	
	scanf("%d", &casis);

	for(i = 0; i < casis; i++)
	{
		result = 0;

		//set fCase
		scanf("%d", &row);
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				scanf("%d", &Board[j][k]);
		for(j = 0; j < 4; j++)
			fCase[j] = Board[row - 1][j];

		//set sCase
		scanf("%d", &row);
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				scanf("%d", &Board[j][k]);
		for(j = 0; j < 4; j++)
			sCase[j] = Board[row - 1][j];


		//check with fCase, sCase
		for(j = 0; j < 4; j++)
			for(k = 0; k < 4; k++)
				if(fCase[j] == sCase[k])
				{
					if(result == 0)
						result = fCase[j];
					else if(result != 0)
						result = -1;
				}

		//print result
		printf("Case #%d: ", i + 1);
		switch(result)
		{
		case -1:
			printf("Bad magician!\n");
			break;
		case 0:
			printf("Volunteer cheated!\n");
			break;
		default :
			printf("%d\n", result);
			break;
		}
	}
}