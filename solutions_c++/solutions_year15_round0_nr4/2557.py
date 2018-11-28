#include<stdio.h>
bool ch(int x,int r,int c)
{
	if(x==1)	return 1;
	else if(x==2)
	{
		if((r*c)%2==0)
			return 1;
		else
			return 0;
	}
	else if(x==3)
	{
		int a=r*10+c;
		if(a==23 || a==32 || a==33 || a==43 || a==34)
			return 1;
		else
			return 0;
	}
	else if(x==4)
	{
		int a=r*10+c;
		if(a==43 || a==34 || a==44)
			return 1;
		else
			return 0;
	}
	return 0;
}
int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int a=1;a<=t;a++)
	{
		int x,r,c;
		scanf("%d%d%d",&x,&r,&c);
		if(ch(x,r,c))
			printf("Case #%d: GABRIEL\n",a);
		else
			printf("Case #%d: RICHARD\n",a);
	}
}
