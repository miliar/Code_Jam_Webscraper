#include<stdio.h>
int main()
{
	int t,h;
	scanf("%d",&t);
	for(h=1;h<=t;h++)
	{
		double i,j,k=0,l,n,m,c,f,x;
		l=2.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		m=x/l;
		n=c/l+(x/(l+f));
		while(m>=n)
		{
			k+=c/l;l=l+f;
			m=x/l;
			n=c/l+(x/(l+f));
		}
		k+=x/l;
		printf("Case #%d: %.7lf\n",h,k);
	}
	return 0;
}
