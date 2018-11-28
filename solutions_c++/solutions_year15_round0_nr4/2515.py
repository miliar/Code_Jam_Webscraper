#include<stdio.h>
int main()
{
	freopen("abc.txt","r",stdin);
	freopen("test.txt","w",stdout);
	long long int f1,f,q,a,b,x,t;
	scanf("%lld",&f);
	for(f1=1;f1<=f;f1++)
	{
		scanf("%lld %lld %lld",&q,&a,&b);
		if(a>b)
		{
			t=a;
			a=b;
			b=t;
		}
		x=0;
		if(q==1)
		x=1;
		if(q==2)
		{
			if((a*b)%2==0)
			x=1;
		}
		if(q==3)
		{
			if((a*b)%3==0)
			x=1;
			if(a==1)
			x=0;
		}
		if(q==4)
		{
			if((a*b)%4==0)
			x=1;
			if(a==1)
			x=0;
			if(a==2)
			x=0;
		}
		if(x==0)
		printf("Case #%lld: RICHARD\n",f1);
		else
		printf("Case #%lld: GABRIEL\n",f1);
	}
	return 0;
}
