#include <stdio.h>
#include <string.h>
int main()
{
	int T,i,j,length,flag;
	char S[10000];
	long long int count;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%s",S);
		length = strlen(S);
		if(S[0] == '+')
		{
			count = 0;
			flag = 0;
			for(j=1;j<length;j++)
			{
				if(S[j] == '+')
				{
					flag = 0;
					continue;
				}
				else if (flag == 1)
					continue;
				else
				{
					flag = 1;
					count+=2;
				}
			}
			printf("Case #%d: %lld\n",i,count);
		}
		else
		{
			j = 0;
			while(S[j]=='-')
			{
				j++;
			}
			count = 1;
			flag = 0;
			for(j;j<length;j++)
			{
				if(S[j] == '+')
				{
					flag = 0;
					continue;
				}
				else if (flag == 1)
					continue;
				else
				{
					flag = 1;
					count+=2;
				}
			}
			printf("Case #%d: %lld\n",i,count);
		}
	}
	return 0;
}
