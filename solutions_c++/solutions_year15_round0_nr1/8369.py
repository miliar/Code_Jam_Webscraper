#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define SIZE 1001
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int t, smax, i, j, counter, sum, flag;
	char inp[SIZE];
	scanf("%d", &t);
	for(i=0; i<t; i++)
	{
		scanf("%d", &smax);
		scanf("%s", inp);
		if((1<=t<=100) && (0<=smax<=1000))
		{
			j = 0;
			counter = 0;
			flag = 0;
			sum = 0;
			while((flag == 0) && (inp[j] != '\0'))
			{
				if((inp[j]>=49) && (inp[j]<=57))
				{
					sum += inp[j]-48;
					j++;
					if(j >= 1000)
					{
						flag = 1;
					}
					else if(inp[j] != '\0')
					{
						flag = 0;
					}
					else
					{
						flag = 1;
					}
				}
				else if((inp[j] == 48) && (sum <= j))
				{
					sum++;
					counter++;
					j++;
				}
				else
				{
					j++;
				}
			}
			printf("Case #%d: %d\n", i+1, counter);
		}
	}
	return 0;
}
