#include<cstdio>
int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("OutputD2.out","w",stdout);
	int i,t,x,r,c;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d%d%d",&x,&r,&c);
		printf("Case #%d: ",i);
		if (x==1)
			printf("GABRIEL\n");
		else if (x==2)
		{
			if ((r*c)%2)
				printf("RICHARD\n");
			else
				printf("GABRIEL\n");
		}
		else if (x==3)
		{
			if ((r*c)%3==0&&r*c!=3)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
		else
		{
			if (r*c==12||r*c==16)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}
	}
	return 0;
}
