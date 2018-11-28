#include<stdio.h>
#include<string.h>
int po(int a)
{
	int count=0;
	while(a!=1)
	{
		if(a%2!=0)
			return -1;
		a/=2;
		count++;
	}
	return count;
}
int powe(int a)
{
	int count=0;
	while(a!=1)
	{
		a/=2;
		count++;
	}
	return count;
}
int main()
{
	int t,p,q,i;
	char str[10];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		
		scanf("%d/%d",&p,&q);
		printf("Case #%d: ",i);
		//printf("%d %d\n",p,q);
		int power=po(q);
		
		if(power<0)
			printf("impossible\n");
		else
			printf("%d\n",power-powe(p));

	}
}
