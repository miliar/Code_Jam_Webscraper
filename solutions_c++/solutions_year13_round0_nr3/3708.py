#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;
long long int p,f;
long long int y,z,g;
int is_pal(int x)
{
	z=0;
	y=x;
	while(x)
	{
		z = (z*10)+x%10;
		x = x/10;
	}
	if(z==y)
	g = 1;
	else
	g = 0;
	return g;
}
int main()
{
	long long int t,counter,a,b,k,i,number;
	scanf("%lld",&t);
	for(k=1; k<=t; k++)
	{
		counter=0;
		scanf("%lld",&a);
		scanf("%lld",&b);
		for(i=a; i<=b; i++)
		{
			double m = sqrt(i);
			if(!(m-(int)m))
			{
				if( is_pal(sqrt(i)) && is_pal(i) ) //(is_prime(i))&&
				{
					counter++;
					//printf("%lld\n",i);
				}
			}
		}
		printf("Case #%lld: %lld\n",k,counter);
	}
	return 0;
}