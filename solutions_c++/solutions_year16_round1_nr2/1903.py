#include<stdio.h>
int main()
{
	long long t, i;
	long long n, k, j;
	int hight;
	int HightofGrid[2600];
	int HightList[50];
	int count;
	freopen("inputB.txt", "r", stdin);
	freopen("outputB.txt", "w", stdout);
	scanf("%lld", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%lld", &n);

		for (j = 0; j < 2510; j++)
			HightofGrid[j] = 0;

		for (j=0;j<n;j++)
		{
			for (k = 0; k < 2 * n-1; k++)
			{
				scanf("%d", &hight);
				HightofGrid[hight]++;
			}
		}

		count = 0;
		for (j = 0; j < 2510; j++)
		{
			if (HightofGrid[j] % 2)
			{
				HightList[count] = j;
				count++;
			}
		}


		printf("case #%lld: ",i+1);
		for (j = 0; j < count ;j++)
			printf("%d ", HightList[j]);
		printf("\n");
	}
	return 0;
}