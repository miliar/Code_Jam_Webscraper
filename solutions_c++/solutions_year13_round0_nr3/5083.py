#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef long long int64;

int main(int argc, char* argv[])
{
	  // Process queries.
	int T;
	
	scanf("%d", &T);
	int tmp;
	
	for (int prob = 1; prob <= T; prob++)
	{
		int64 A, B;
		scanf("%lld %lld", &A, &B);

		int64 startAt = ceil(sqrt(double(A)));

		int64 stopAt = floor(sqrt(double(B)));

		int64 cnt = 0;
		for (int64 ii =  startAt; ii <= stopAt; ++ii)
		{
			int64 nn = ii;
			int64 copy = nn;
			int64 reversed = 0;
			while (nn > 0)
			{
				reversed = reversed * 10  + (nn % 10);
				nn = nn / 10;
			}

			if (copy == reversed)
			{
				nn = ii * ii;
				copy = nn;
				int64 reversed = 0;
				while (nn > 0)
				{
					reversed = reversed * 10  + (nn % 10);
					nn = nn / 10;
				}

				
				if (copy == reversed)
				{
					cnt++;
				}
			}
		}
		
		printf("Case #%d: %lld\n", prob, cnt);
		
	}



	return 0;
}