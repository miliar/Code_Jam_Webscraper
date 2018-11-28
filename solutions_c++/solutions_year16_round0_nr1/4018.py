#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int N;
		long long cnt, next = 0;
		int target = (1 << 10) - 1;
		scanf("%d", &N);
		next = N;

		if (N == 0)
		{
			printf("Case #%d: INSOMNIA\n",i);
		}
		else
		{
			int res = 0;
			int magic = 71;

			while (magic--)
			{
				int len = (int)log10((double)next) + 1;
				int div = 10;
				int intermediate = next;

				for (int i = 0; i < len; i++)
				{
					int remainder = intermediate % 10;
					intermediate -= remainder;
					intermediate /= 10;

					if (remainder == 0)
					{
						remainder = 10;
					}

					int mask = (1 << remainder - 1);
					res |= mask;
					if (res == target)
					{
						break;
					}
				}
				if (res == target)
				{
					break;
				}
				next += N;
			}
			printf("Case #%d: %lld\n",i,next);
		}
	}
	return 0;
}