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

int main()
{
//	freopen("in.in","r",stdin);freopen("out.out","w",stdout);
	freopen("A-small-attempt0.in","r",stdin);freopen("small-attempt.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	
	int testCases = 0;
	scanf("%d",&testCases);

	for (int caseId = 1; caseId <= testCases; caseId++)
	{
		int answer1 = 0;
		scanf("%d",&answer1);

		int case1[4][4]; 
		scanf("%d %d %d %d", &case1[0][0], &case1[0][1], &case1[0][2], &case1[0][3]);
		scanf("%d %d %d %d", &case1[1][0], &case1[1][1], &case1[1][2], &case1[1][3]);
		scanf("%d %d %d %d", &case1[2][0], &case1[2][1], &case1[2][2], &case1[2][3]);
		scanf("%d %d %d %d", &case1[3][0], &case1[3][1], &case1[3][2], &case1[3][3]);


		int answer2 = 0;
		scanf("%d",&answer2);

		int case2[4][4]; 
		scanf("%d %d %d %d",&case2[0][0], &case2[0][1], &case2[0][2], &case2[0][3]);
		scanf("%d %d %d %d",&case2[1][0], &case2[1][1], &case2[1][2], &case2[1][3]);
		scanf("%d %d %d %d",&case2[2][0], &case2[2][1], &case2[2][2], &case2[2][3]);
		scanf("%d %d %d %d",&case2[3][0], &case2[3][1], &case2[3][2], &case2[3][3]);


		int result = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (case1[answer1-1][i] == case2[answer2-1][j])
				{
					if (result > 0)
						result = -1;

					if (result == -1)
						continue;

					result = case1[answer1-1][i];
				}
			}
		}
		
		if (result > 0)
			printf("Case #%d: %d\n", caseId, result);
		else if (result == -1)
			printf("Case #%d: Bad magician!\n", caseId);
		else 
			printf("Case #%d: Volunteer cheated!\n", caseId);
	}

	return 0;
}