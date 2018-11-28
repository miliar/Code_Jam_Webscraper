#include "stdio.h"
#include <math.h>

long long how_much(long long r,long long n)
{
	return 2*r*n + 2*n*n - n;
}

int main()
{
	char str[10][10];
	int N;
	scanf("%d",&N);
	gets(str[0]);
	for(int I=1; I<=N; ++I)
	{
		long long r, t;
		scanf("%I64d%I64d",&r, &t);
		printf("Case #%d:", I);

		long long min = 0;
		long long max = 1;
		if( how_much(r, 1) == t )
			min = 1;
		else if( how_much(r, 1) < t )
		{
			min = 1;
			max = 2;
			while( how_much(r, max) < t )
			{
				min = max;
				max *= 2;
			}
			if( how_much(r, max) == t )
				min = max;
			else // r,max > t > r,min
			{
				while( min < max )
				{
					long long mid = (min+max)/2;
					if( mid == min )
						break;
					if( how_much(r, mid) == t )
					{
						min = mid;
						break;
					}
					else if( how_much(r, mid) < t )
					{
						min = mid;
					}
					else
						max = mid;
				}
			}
		}
		printf(" %I64d\n", min);
	}
	return 0;
}

