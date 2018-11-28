#include "stdafx.h"

#define VOLCHEAT "Volunteer cheated!"
#define BADMAG "Bad magician!"

int _tmain(int argc, _TCHAR* argv[])
{
	int ucT = 0;
	int ucFirstAns = 0;
	int ucSecondAns = 0;

	int ucFirstSet[4][4] = {0};
	int ucSecSet[4][4] = {0};

	scanf("%d", &ucT);
	int i = 0, j =0, k = 0;
	for(; k < ucT; k++)
	{
		scanf("%d", &ucFirstAns);
		for(i = 0; i < 4; i++)
		{
			scanf("%d %d %d %d", &ucFirstSet[i][0],&ucFirstSet[i][1],&ucFirstSet[i][2],&ucFirstSet[i][3]);
		}
		scanf("%d", &ucSecondAns);
		for(i = 0; i < 4; i++)
		{
			scanf("%d %d %d %d", &ucSecSet[i][0],&ucSecSet[i][1],&ucSecSet[i][2],&ucSecSet[i][3]);
		}
		if(ucFirstAns > 16 || ucSecondAns > 16)
			printf("Case #%d: %s\n", k, VOLCHEAT);
		
		int ucFound = 0;
		int ucFoundVal = 0;
		for(i = 0 ; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				if(ucFirstSet[ucFirstAns-1][i] == ucSecSet[ucSecondAns-1][j])
				{
					ucFoundVal = ucFirstSet[ucFirstAns-1][i];
					ucFound++;
				}
			}
		}
		if(ucFound > 1)
			printf("Case #%d: %s\n", k+1, BADMAG);
		else if(ucFound == 1)
			printf("Case #%d: %d\n", k+1, ucFoundVal);
		else 
			printf("Case #%d: %s\n", k+1, VOLCHEAT);
	}

	return 0;
}

