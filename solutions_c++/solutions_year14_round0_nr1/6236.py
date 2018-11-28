#include <stdio.h>

int main()
{
	int T, i, j, TestCase, r1, r2, ans = -1, arr1[4][4], arr2[4][4];
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d",&T);


	for(TestCase = 0; TestCase < T; TestCase++)
	{
		scanf("%d", &r1);
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				scanf("%d", &arr1[i][j]);
				
		scanf("%d", &r2);
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				scanf("%d", &arr2[i][j]);

		ans = -1;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				if(arr1[r1-1][i] == arr2[r2-1][j])
				{
					if(ans == -1) ans = arr1[r1-1][i];
					else ans = -2;
				}
			}
		}

		if(ans == -1) printf("Case #%d: Volunteer cheated!\n", TestCase+1);
		else if(ans == -2) printf("Case #%d: Bad magician!\n", TestCase+1);
		else printf("Case #%d: %d\n", TestCase+1, ans);

	}

}
