#include <stdio.h>
#include <vector>
#include <string>
#include <stack>
#include <map>
#include <iostream>
using namespace std;

int row1[4];
int row2[4];
int num1, num2;

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);


	int nCase;
	int tmp;
	int t, i, j;
	scanf("%d", &nCase);
	for (t = 1; t <= nCase; ++ t)
	{
		scanf("%d", &num1);
		for (i = 1; i <= 4; ++ i)
		{
			for (j = 0; j < 4; ++ j)
			{
				scanf("%d", &tmp);
				if (i == num1)
				{
					row1[j] = tmp;
				}
			}			
		}

		scanf("%d", &num2);
		for (i = 1; i <= 4; ++ i)
		{
			for (j = 0; j < 4; ++ j)
			{
				scanf("%d", &tmp);
				if (i == num2)
				{
					row2[j] = tmp;
				}
			}			
		}

		int cnt = 0;
		int theNum;
		for (i = 0; i < 4; ++ i)
		{
			for (j = 0; j < 4; ++ j)
			{
				if (row1[i] == row2[j])
				{
					cnt++;
					theNum = row1[i];
				}
			}
		}

		printf("Case #%d: ", t);
		if (cnt == 1)
		{
			printf("%d", theNum);
		}
		else if (cnt == 0)
		{
			printf("Volunteer cheated!");
		}
		else
		{
			printf("Bad magician!");
		}
		if (t < nCase)
		{
			printf("\n");
		}
	}

	//system("pause");
	return 0;
}

