#include <cstdio>
#include <algorithm>


int mask(long long n)
{
	if(n == 0)
		return 1;
	
	int mask = 0;
	while(n != 0)
	{
		mask |= 1 << (n % 10);
		n /= 10;
	}
	
	return mask;
}

long long naive(long long x)
{
	if(x == 0)
		return -1;
		
	int m = 0;
	for(long long i = 1; ; i++)
	{
		m |= mask(i * x);
		if(m == 0x3FF)
			return i * x;
	}
}

int main()
{
//	freopen("input.txt", "r");

	int tests;
	scanf("%i", &tests);
	
	for(int t = 1; t <= tests; t++)
	{
		printf("Case #%i: ", t);
		
		int n;
		scanf("%i", &n);
		long long res = naive(n);
		if(res < 0)
			printf("INSOMNIA\n");
		else
			printf("%lli\n", res);
	}

/*
	long long r = 0;
	for(int i = 0; i <= 1000000; i++)
	{
		long long c = naive(i);
		r = std::max(r, c);
//		printf("%i: %i\n", i, naive(i));
	}	
	printf("%lli\n", r);
	*/
	return 0;
}

