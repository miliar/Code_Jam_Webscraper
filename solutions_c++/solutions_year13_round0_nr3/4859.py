#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int t;
long long a,b,n,res=0;

long long pal(long long n)
{
    long long pom,last,check;
	pom = n;
	check = 0;
	while(pom)
	{
		last=pom%10;
		pom/=10;

		check=check*10 + last;
	}		
	return check;
}
	
int main()
{
	scanf("%d", &t);
	
	for(int i = 0; i < t; i++)
	{
		scanf("%lld %lld", &a, &b);
        res=0;
		n=(long long)sqrt((double)a);
		while(n*n<=b)
		{
            if(n*n>=a)
		    	if(pal(n)==n && n*n==pal(n*n))
    			    res++;

			n++;
		}

		printf("Case #%d: %lld\n", i, res);
	}
	return 0;
}