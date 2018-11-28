#include<cstdio>
#include<cmath>

int main()
{
	int t,k;
	double f,c,x,s,y,a,b,d,e;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		y=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		s=2.0;
		a=x/s;
		b=c/s + x/(s+f);
		while(a>b)
		{
			d=floor(c/s);
			e=(c - s*d)/s;
			y+=d+e;
			s+=f;
			a=x/s;
			b=c/s + x/(s+f); 
		}
		d=floor(x/s);
		e=(x - d*s)/s;
		y+=e + d;
		printf("Case #%d: %.7lf\n",k,y);
	}
	return 0;
}
