#include<iostream>
#include<cstdio>

void test(int);

int main()
{
	int t,i=1;
	scanf("%d",&t);
	while(t--)
	{
		test(i);
		i++;
	}
	return 0;
}

void test(int num)
{
	double c,f,x,pro=2.00;
	int e=0;
	double tme=0.00;
	scanf("%lf%lf%lf",&c,&f,&x);
	while(true)
	{
		if(x/pro < ((c/pro)+(x/(pro+f))))
		{
			tme+=x/pro;
			break;
		}
		tme=tme + (c/pro);
		pro+=f;
	}
	printf("Case #%d: %lf\n",num,tme);
}