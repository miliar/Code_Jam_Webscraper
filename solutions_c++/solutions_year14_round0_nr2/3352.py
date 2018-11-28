#include<stdio.h>
int main()
{
	double c,f,x,r,a;
	int t,i,j,k,u;
	scanf("%d",&t);
	for(u=1;u<=t;u++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		r=2; a=0;
		while(x>c&&c/f<(x-c)/r)
		{
			a+=c/r;
			r+=f;
		}
		a+=x/r;
		printf("Case #%d: %.7lf\n",u,a);
	}
}
