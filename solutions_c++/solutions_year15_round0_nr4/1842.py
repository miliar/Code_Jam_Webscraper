#include<stdio.h>
int main()
{
	int t,i,x,c,r; 
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d%d",&x,&r,&c);
		if(x==1)
		{
			printf("case #%d: GABRIEL\n",i);
		}
		if(x==2)
		{
			if((r*c)%2==0)
			{
				printf("case #%d: GABRIEL\n",i);
			}
			else
			{
				printf("case #%d: RICHARD\n",i);
			}
		}
		if(x==3)
		{
			if((r*c)==6||(r*c)==9||(r*c)==12)
			{
				printf("case #%d: GABRIEL\n",i);
			}
			else
			{
				printf("case #%d: RICHARD\n",i);
			}
		}
		if(x==4)
		{
			if((r*c)==12||(r*c)==16)
			{
				printf("case #%d: GABRIEL\n",i);
			}
			else
			{
				printf("case #%d: RICHARD\n",i);
			}
		}
	}
	return 0;
}

