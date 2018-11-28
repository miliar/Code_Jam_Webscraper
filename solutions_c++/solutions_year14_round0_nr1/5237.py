#include <iostream>
#include <stdio.h>
using namespace std;

int first[4][4], second[4][4], counter[17];

int main()
{
	int i, j, ans1, ans2, T, t, count, index;

	scanf("%d", &T);
	for(t=1; t<=T; t++)
	{
		for(j=0; j<17; j++)
		counter[j]=0;

		/* ********INPUT*********** */

		scanf("%d", &ans1);

		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				scanf("%d", &first[i][j]);
				if(i==ans1-1)
				{
					counter[first[i][j]] += 2;

				}
			}
		}

		scanf("%d", &ans2);

		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				scanf("%d", &second[i][j]);
				if(i==ans2-1)
				{
					counter[second[i][j]]--;

				}

			}
		}
		/* ******************************** */
		count=0;
		for(j=0; j<17; j++)
		{
			if(counter[j]==1)
			{
				count++;
				index = j;
			}
		}
		if(count==1)
		printf("Case #%d: %d\n", t, index);
		else if(count>1)
		printf("Case #%d: Bad magician!\n", t);
		else if(count==0)
		printf("Case #%d: Volunteer cheated!\n", t);
	}
	return 0;
}
