#include <cassert>
#include <cstdio>
#include <cstring>
#include <vector>


int main()
{
	int tests;
	scanf("%i", &tests);
	for(int t = 1; t <= tests; t++)
	{
		printf("Case #%i:", t);

		int k, c, s;
		scanf("%i %i %i", &k, &c, &s);
		assert(s == k);


		for(int i = 0; i < k; i++)
		{
			long long r = 0;
			for(int j = 1; j <= c; j++)
				r = r * k + i;
			printf(" %lli", r + 1);
		}

		printf("\n");	
	}
	
	return 0;
}

