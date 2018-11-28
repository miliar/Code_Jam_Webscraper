#include <stdio.h>
#include <stdlib.h>

int main()
{
	int t, n, i, j, k, count, number, tmp;
	int dp[4] = {0};
	int dp2[4] = {0};

	scanf(" %d", &t);

	for(i=0 ; i<t ; i++)
	{
		scanf(" %d", &n);
		for(j=0 ; j<4 ; j++)
		{
			if (j == n-1)
			{
				for(k=0 ; k<4 ; k++)
					scanf(" %d", &dp[k]);
			}
			else
			{
				for(k=0 ; k<4 ; k++)
					scanf(" %d", &tmp);
			}
		}

		scanf(" %d", &n);
		for(j=0 ; j<4 ; j++)
		{
			if (j == n-1)
			{
				for(k=0 ; k<4 ; k++)
					scanf(" %d", &dp2[k]);
			}
			else
			{
				for(k=0 ; k<4 ; k++)
					scanf(" %d", &tmp);
			}
		}

		count = 0;
		number = 0;
		for(j=0 ; j<4 ; j++)
		{
			for(k=0 ; k<4 ; k++)
			{
				if (dp[j] == dp2[k])
				{
					count++;
					number = dp[j];
				}
			}
		}

		if (count == 0)
		{
			printf("case #%d: Volunteer cheated!\n", i+1);
		}
		else if (count == 1 )
		{
			printf("case #%d: %d\n", i+1, number);
		}
		else
		{
			printf("case #%d: Bad magician!\n", i+1);
		}
	}
	return 0;
}