#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
int test,i,j,k,t;
int max,shy[1002];
int ps=0,no=0;
scanf("%d",&test);
for(t=1;t<=test;t++)
{
	scanf("%d",&max);
	scanf("%d",&k);
	i=max;
	for(j=0;j<=max;j++)
	{
	shy[i]=k%10;
	k=k/10;
	i--;
	}
	no=0;ps=0;
	ps=shy[0];
	for(i=1;i<=max;i++)
	{
		if(shy[i]!=0)
		{
			if(ps>=i)
			{
				ps+=shy[i];
			}
			else
			{
				no+=i-ps;
				ps=ps+no+shy[i];
			}
		}
	}
	printf("Case #%d: %d\n",t,no);
}
return 0;
}
