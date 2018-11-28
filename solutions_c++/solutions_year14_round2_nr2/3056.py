#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	long long T;
	scanf("%lld", &T);

	for(long long turn = 1; turn <= T; turn++)
	{
		long long A, B, K;
		scanf("%lld %lld %lld", &A, &B, &K);

		long long max = 0;
		long long min = 0;
		if(A > B)
		{
			max = A;
			min = B;
		}
		else
		{
			max = B;
			min = A;
		}

		long long count = 0;
		for(long long i = 0; i < max; i++)
		{
			for(long long ii = 0; ii < min; ii++)
			{
				if((i & ii) < K) count++;
			}
		}

		printf("Case #%lld: %lld\n", turn, count);
	}
	return 0;
}