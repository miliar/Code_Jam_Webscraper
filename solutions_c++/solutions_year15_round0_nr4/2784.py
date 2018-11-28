#include<stdio.h>
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("ddaa.in","w",stdout);
	int T,X,R,C,count=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d %d %d",&X,&R,&C);
		if(X==1)
		{
			printf("Case #%d: GABRIEL\n",count++);
		}
		else if(X==2)
		{
			if((R*C)%2==1)
				printf("Case #%d: RICHARD\n",count++);
			else
				printf("Case #%d: GABRIEL\n",count++);
		}
		else if(X==3)
		{
			if( ( (R*C)%3!=0||R*C==3 ) || (R<3)&&(C<3) )
					printf("Case #%d: RICHARD\n",count++);
			else
				printf("Case #%d: GABRIEL\n",count++);				
		}
		else if(X==4)
		{
			if(R*C<12)
					printf("Case #%d: RICHARD\n",count++);
			else
				printf("Case #%d: GABRIEL\n",count++);
		}
	}
	return 0;
}
