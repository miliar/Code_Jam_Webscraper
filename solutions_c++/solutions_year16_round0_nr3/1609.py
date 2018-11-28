#include <stdio.h>

const long long base = 100000000000000000LL;

struct num{
	long long p1, p2;

	num() : p1(0), p2(0) {}
	num(long long x) { *this = x; }

	num operator =(long long x)
	{
		p1 = x % base, p2 = x / base;
		return *this;
	}
	num operator *(long long x)
	{
		num retv = *this;
		retv.p1 *= x;
		retv.p2 *= x;
		retv.p2 += (retv.p1 / base);
		retv.p1 %= base;
		return retv;
	}
	num operator +(num x)
	{
		num retv = *this;
		retv.p1 += x.p1;
		retv.p2 += x.p2;
		retv.p2 += (retv.p1 / base);
		retv.p1 %= base;
		return retv;
	}
	long long operator %(long long x)
	{
		return ((p1%x)+(((p2%x)*(base%x))%x))%x;
	}
	num ant()
	{
		num retv = *this;
		retv.p1--;
		if(retv.p1 < 0)
			retv.p2--, retv.p1 += base;
		return retv;
	}
};

num pot[11][35];

bool composite(num x)
{
	for(long long i = 2; i < 10; i++)
		if(x % i == 0)
			return true;
	return false;
}

bool composite_print(num x)
{
	for(long long i = 2; i < 10; i++)
		if(x % i == 0)
		{
			printf(" %lld", i);
			return true;
		}
	return false;
}


int
main(void)
{
	for(int i = 2; i <= 10; i++)
	{
		pot[i][0] = 1LL;
		for(int j = 1; j <= 32; j++)
			pot[i][j] = pot[i][j-1] * i;
	}
	long long n, q;
	scanf("%*d %lld %lld", &n, &q);
	printf("Case #1:\n");
	for(long long i = (1LL << (n-1LL)); q && i < (1LL << n); i++)
	{
		if((i&1LL) == 0) continue;
		bool ok = true;
		for(int j = 2; ok && j <= 10; j++)
		{
			num x = 0;
			for(int k = 0; k < n; k++)
				if(i & (1LL << k))
					x = x + pot[j][k];
			if(!composite(x))
				ok = false;
		}
		if(!ok)
			continue;
		for(int k = n-1; k >= 0; k--)
			if(i & (1LL << k))
				printf("1");
			else
				printf("0");
		for(int j = 2; ok && j <= 10; j++)
		{
			num x = 0;
			for(int k = 0; k < n; k++)
				if(i & (1LL << k))
					x = x + pot[j][k];
			if(!composite_print(x))
				ok = false;
		}
		printf("\n");
		q--;
	}
}
