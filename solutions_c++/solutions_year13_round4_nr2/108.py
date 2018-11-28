#include<cstdio>

long long f (int n, long long p);


int main()
{
int T;
scanf("%d", &T);
for (int tt=1; tt<=T; tt++)
{
	printf("Case #%d: ", tt);
	
	int n;
	long long p;
	scanf("%d %lld", &n, &p);
	
	if(p==(1LL<<n))
	{
		printf("%lld %lld\n", (1LL<<n)-1, (1LL<<n)-1);
		continue;
	}
	if(p==1)
	{
		printf("0 0\n");
		continue;
	}
	printf("%lld ", f(n, p));
	long long n2 = (1LL << n);
	printf("%lld\n", n2-2 - f(n, n2-p));	
	
}
return 0;
}

long long f (int n, long long p)
{
	long long nm, nr;
	nm = (1LL << (n-1));
	nr = 1;
	int wyk = n-2;
	while(p>nm)
	{
		nm += (1LL << wyk);
		nr *= 2;
		wyk--;
		
	}
	return 2*nr-2;
}
