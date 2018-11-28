#include<iostream>
#include<cstdio>

int main()
{
	int T;
	scanf("%d", &T);
	int sMax;
	char dataSet[1010];
	int i;
	int people, reqPeople;
	for (i=0; i<T; i++)
	{
		people = 0;
		reqPeople = 0;
		scanf("%d ", &sMax);
		int j;
		for (j = 0; j<=sMax; j++)
		{
			scanf("%c", &dataSet[j]);
		}
		
		for (j = 0; j <= sMax; j++)
		{
			if(dataSet[j]!='0')
			{
				if (people < j)
				{
					reqPeople += j - people;
					people += reqPeople;
				}
				people += int(dataSet[j] - '0');
			}
		}
		printf("Case #%d: %d\n", i+1, reqPeople);
	}
	return 0;
}
