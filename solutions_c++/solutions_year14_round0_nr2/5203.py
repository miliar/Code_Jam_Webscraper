#include<stdio.h>
int main()
{
	long long int n,k=1;
	double c,f,x,r,t;	
	scanf("%lld",&n);
	while(n--)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		r=2.0;
        t = 0.0;
        while((x-c)/r>(x/(r+f)))
        {
            t=t+c/r;
            r=r+f;
        }
        t=t+x/r;
        printf("Case #%lld: %lf\n",k++,t);
    }
    return 0;
}
