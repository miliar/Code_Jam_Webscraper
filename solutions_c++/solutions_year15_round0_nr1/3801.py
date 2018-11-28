#include<stdio.h>

void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int shy[2000], T, S, cumulative[2000];
	char buffer[2000];
	scanf("%d",&T);
	for(int c=1;c<=T;c++)
	{
		scanf("%d %s",&S, buffer);
		for(int i=0;i<=S;i++)
			shy[i] = buffer[i]-'0';

		cumulative[0]=shy[0];
		for(int i=1;i<=S;i++)
			cumulative[i]=cumulative[i-1]+shy[i];

		int max=0;
		for(int i=1;i<=S;i++)
		{
			int diff = i - cumulative[i-1];
			max = diff > max ? diff : max;
		}

		printf("Case #%d: %d\n",c,max);
	}
}