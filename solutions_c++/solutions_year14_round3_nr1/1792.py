#include <stdio.h>

typedef struct q
{
	long long up;
	long long down;
	q()
	{
		up=0;
		down=1;
	}
	q(int a,int b)
	{
		up = a;
		down = b;
	}
}Q;

int can(Q myq,int depth)
{
	if(depth >=40)
	{
		return -123456778;
	}
	if(myq.up == 0 || myq.down == myq.up)
	{
		return 0;
	}
	if(2*myq.up >= myq.down)
	{
		if(can(Q(myq.up*2 - myq.down,myq.down),depth+1) >= 0)
		{
			return 1;
		}
		else
		{
			return -123456778;
		}
	}
	else
	{
		return 1+can(Q(myq.up*2,myq.down),depth+1);
	}
}

int main()
{
	int T,c = 1;

	scanf("%d",&T);

	while(T--)
	{
		int a,b,ct;

		scanf("%d/%d",&a,&b);
		ct = can(Q(a,b),0);
		if(ct < 0)
		{
			printf("Case #%d: impossible\n",c++);
		}
		else
		{
			printf("Case #%d: %d\n",c++,ct);	
		}
	}
	return 0;
}