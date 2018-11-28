#include<cstdio>
#include<cmath>

bool is_palyndrome(long long x)
{
	long long k = 0, xx = x;
	while(xx >= 10)
	{
		k = k*10 + xx%10;
		xx /= 10;
	}
	k = k*10 + xx;
	return k == x;
}

int main()
{
	int T; scanf("%d",&T);
	for(int ii = 0; ii < T; ii++)
	{
		long long A, B; scanf("%lld%lld",&A,&B);
		double _A = sqrt((double)A), _B = sqrt((double)B);
		long long res = 0;
		for(long long i = 1; i < 10000; i++)
		{
			long long k = 0, x = i, xx = i, m = i%10;
			while(x >= 10)
			{
				m *= 10;
				x /= 10;
				k += k*10 + x%10;
			}
			x = i;
			while(xx >= 10)
			{
				x *= 10;
				xx /= 10;
			}
			k += x;
			if(k >= _A && k <= _B)
			{
				long long r = k*k;
				if(is_palyndrome(r))
					res++;
			}
			k += x*9+m;
			if(k >= _A && k <= _B)
			{
				long long r = k*k;
				if(is_palyndrome(r))
					res++;
			}
		}
		printf("Case #%d: %lld\n",ii+1,res);
	}
	return 0;
}
