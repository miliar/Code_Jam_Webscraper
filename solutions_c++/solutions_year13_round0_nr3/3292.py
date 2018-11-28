#include <cstdio>
#include <cmath>

inline int sq(const int& x)
{
	return x*x;
}
inline int pow10(int e)
{
	int out=1;
	for(int cur=0; cur < e; cur++)
		out*=10;
	return out;
}

int extractLeft(int& nb)
{
	int pw=(int)log10(nb);
	int out=nb/pow10(pw);
	nb-=out*pow10(pw);

	return out;
}

int extractRight(int& nb)
{
	int out=nb%10;
	nb/=10;
	return out;
}

bool isPalin(int nb)
{
	while(nb>=10)
	{
		if(extractLeft(nb) != extractRight(nb))
			return false;
	}
	return true;
}

int nbInIv(int a, int b)
{
	int out=0;
	int sqrtA = ceil(sqrt(a)), sqrtB = floor(sqrt(b));
	
	for(int cur=sqrtA; cur <= sqrtB; cur++)
	{
		if(isPalin(cur) && isPalin(sq(cur)))
			out++;
	}
	return out;
}

int main(void)
{
	int nbTests;
	scanf("%d", &nbTests);

	for(int test=0; test < nbTests; test++)
	{
		int a,b;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", test+1, nbInIv(a,b));
	}

	return 0;
}

