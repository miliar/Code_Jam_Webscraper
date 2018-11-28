#include<stdio.h>
int main()
{
	freopen ("a.in", "r", stdin);
   freopen ("output.txt", "w", stdout);
	int t,x,r,c,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		scanf("%d %d %d",&x,&r,&c);
		if(x==1)
		{
				printf("Case #%d: GABRIEL\n",k);
		}
		else if(x==2)
		{
			if((r*c)%2==1)
			{
				printf("Case #%d: RICHARD\n",k);
			}
			else
			{
					printf("Case #%d: GABRIEL\n",k);
			}
		}
		else if(x==3)
		{
			if((r*c)==6||(r*c)==9||(r*c)==12)
			{
				printf("Case #%d: GABRIEL\n",k);
				
			}
			else
			{
				printf("Case #%d: RICHARD\n",k);	
			}
			
			
		}
		else
		{
			if((r*c)==12||(r*c)==16)
			{
				printf("Case #%d: GABRIEL\n",k);
				
			}
			else
			{
				printf("Case #%d: RICHARD\n",k);	
			}
			
		}
	}
	return 0;
}
