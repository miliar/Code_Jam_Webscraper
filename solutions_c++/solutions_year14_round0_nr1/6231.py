/*
 * aa.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: wd007
 */

#include <stdlib.h>
#include <stdio.h>


int main()
{
	int t, i, j, k, ans1, ans2, ans, T;

	int a[5][5], b[5][5];

	scanf("%d", &t);

	T = t;
	while(t--)
	{
		scanf("%d", &ans1);
		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
				scanf("%d", &a[i][j]);
		}

		scanf("%d", &ans2);
		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
				scanf("%d", &b[i][j]);
		}

		k = 0;

		for (i = 1; i <= 4; i++)
		{
			for (j = 1; j <= 4; j++)
			{
				if (a[ans1][i] == b[ans2][j])
				{
					k++;
					ans = a[ans1][i];
				}
			}
		}

		if (k == 1)
			printf("Case #%d: %d\n", T-t, ans);
		else if (k == 0)
			printf("Case #%d: Volunteer cheated!\n", T-t);
		else
			printf("Case #%d: Bad magician!\n", T-t);
	}
}

