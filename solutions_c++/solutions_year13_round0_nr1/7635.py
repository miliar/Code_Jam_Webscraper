#include <stdio.h>
#include <math.h>
#include <algorithm>

#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

// sort
//		for (int i = 0; i < candyNumber-1; i++)
//		{
//			for (int j = i; j < candyNumber; j++)
//			{
//				if (candies[i] > candies[j])
//				{
//					int temp = candies[i];
//					candies[i] = candies[j];
//					candies[j] = temp;
//				}
//			}
//		}

bool checkWinFor(char side, char table[4][4])
{
	bool result = false;
	for (int i = 0; i < 4; i++)
	{
		if ((table[i][0] == side || table[i][0] == 'T') &&
			(table[i][1] == side || table[i][1] == 'T') &&
			(table[i][2] == side || table[i][2] == 'T') &&
			(table[i][3] == side || table[i][3] == 'T'))
		{
			result = true;
			break;
		}

		if (result == false &&
			(table[0][i] == side || table[0][i] == 'T') &&
			(table[1][i] == side || table[1][i] == 'T') &&
			(table[2][i] == side || table[2][i] == 'T') &&
			(table[3][i] == side || table[3][i] == 'T'))
		{
			result = true;
			break;
		}
	}

	if (result == false &&
		(table[0][3] == side || table[0][3] == 'T') &&
		(table[1][2] == side || table[1][2] == 'T') &&
		(table[2][1] == side || table[2][1] == 'T') &&
		(table[3][0] == side || table[3][0] == 'T'))
	{
		result = true;
	}

	if (result == false &&
		(table[0][0] == side || table[0][0] == 'T') &&
		(table[1][1] == side || table[1][1] == 'T') &&
		(table[2][2] == side || table[2][2] == 'T') &&
		(table[3][3] == side || table[3][3] == 'T'))
	{
		result = true;
	}

	return result;
}

bool isNotComplited(char table[4][4])
{
	bool result = false;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (table[i][j] == '.')
			{
				result = true;
				break;
			}
		}
	}

	return result;
}

int main()
{
//	freopen("in.txt","r",stdin);freopen("out.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	
	int testCases = 0;
	scanf("%d\n",&testCases);
	
	char table[4][4];// = new char[4,4];

	for (int caseId = 1; caseId <= testCases; caseId=caseId+1)
	{
		scanf("%c%c%c%c\n", &table[0][0], &table[0][1], &table[0][2], &table[0][3]);
		scanf("%c%c%c%c\n", &table[1][0], &table[1][1], &table[1][2], &table[1][3]);
		scanf("%c%c%c%c\n", &table[2][0], &table[2][1], &table[2][2], &table[2][3]);
		scanf("%c%c%c%c\n", &table[3][0], &table[3][1], &table[3][2], &table[3][3]);

		//char c1 = table[0][0];
		//char c2 = table[0][1];
		//char c3 = table[0][2];
		//char c4 = table[0][3];

		//char c5 = table[1][0];
		//char c6 = table[1][1];
		//char c7 = table[1][2];
		//char c8 = table[1][3];

		//char c9 = table[2][0];
		//char c10 = table[2][1];
		//char c11= table[2][2];
		//char c12= table[2][3];

		//char c13= table[3][0];
		//char c14= table[3][1];
		//char c15= table[3][2];
		//char c16= table[3][3];

		if (checkWinFor('O', table))
		{
			printf("Case #%d: O won\n", caseId);
		}
		else
		if (checkWinFor('X', table))
		{
			printf("Case #%d: X won\n", caseId);
		}
		else
		if (!isNotComplited(table))
		{
			printf("Case #%d: Draw\n", caseId);
		}
		else
		{
			printf("Case #%d: Game has not completed\n", caseId);
		}
	}

	//delete [] table;

	return 0;
}