#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

int main()
{
	int test,i;
	scanf("%d", &test);
	for(int t=0;t<test;t++)
	{
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d: ",t+1); 
		if(k==1)
			printf("1\n");
		else if(c==1)
		{
			if(s==k)
			{
				for(i=0;i<k;i++)
					printf("%d ",i+1);
				printf("\n");
			}
			else
			{
				printf("IMPOSSIBLE\n");
			}
		}
		else
		{
			if(s<k-1)
			{
				printf("IMPOSSIBLE\n");
			}
			else
			{
				for(i=2;i<=k;i++)
					printf("%d ",i);
				printf("\n");
			}
		}
	}
}
