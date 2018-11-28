#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	scanf("%d\n",&t);
	for (int cs=1;cs<=t;cs++)
	{
		int k,c,s;
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d: ",cs);

		int mini = (k+c-1)/c;
		if (s==k)
		{
			for (int i=1;i<=k;i++)
			{
				printf("%d",i);
				if (i==k)
				{
					printf("\n");
				}
				else
				{
					printf(" ");
				}
			}
		}
		else if (s>=mini)
		{
			for (int i=1;i<=mini;i++)
			{
				int temp = (i-1)*c;
				for (int j=1;j<=min(c-1,k-1);j++)
				{
					temp = (temp * k) + j;
				}
				temp++;

				printf("%d",temp);
				if (i==mini)
				{
					printf("\n");
				}
				else
				{
					printf(" ");
				}
			}
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}