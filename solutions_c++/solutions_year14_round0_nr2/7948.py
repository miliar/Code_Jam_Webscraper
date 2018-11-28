// To infinity and beyond...
// \m/ W!LSP! \m/

#include<stdio.h>

int main()
{
	long int t,x1=0;
	long double c,f,x,n,sum;
	scanf("%ld",&t);
	while(t--)
	{
		x1++;
		scanf("%Lf",&c);
		scanf("%Lf",&f);
		scanf("%Lf",&x);
		
		n=1.0;
		sum = 0.0;
		while((x-c)/(2.0+(n-1)*f) > (x/(2+n*f)))
		{
			sum = sum + (c/(2+ (n-1)*f));
			n = n+1;
		}
	
		sum = sum + (x/ (2+(n-1)*f));
	
		printf("Case #%ld: %.7Lf\n",x1,sum);
	}
	return 0;	
}
