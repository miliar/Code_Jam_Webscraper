#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <list>
#include <map>
#include <string>

using namespace std;

#define ProblemName "C"
#define InputSize   "small"

typedef unsigned long long _uint64_t;

#define sqr(x) (x*x)

int main(int argc, char **argv)
{
	freopen(ProblemName "-" InputSize ".in", "rb", stdin);
	freopen(ProblemName "-" InputSize ".out", "wb", stdout);

	int T;
	scanf( "%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int count = 0;
		_uint64_t A, B;
		scanf("%llu %llu", &A, &B);
		//printf("%llu %llu\n", A, B);

		_uint64_t precalced[] = {1,2,3,121,212,22,11,111,1111,11111,111111,1111111};
		for(int i =0; i < sizeof(precalced)/sizeof(precalced[0]);i++)
		{
			if ( A<=sqr(precalced[i]) && B >= sqr(precalced[i]) )
			{
				//printf("%llu %llu\n", precalced[i], sqr(precalced[i]));
				count++;
			}
		}
		int power = 100;
		for(int i = 2; i <= 6; i++)
		{
			_uint64_t test = power + 1;
			_uint64_t test2 = 2 * test;
			if ( A <= sqr(test) && B >= sqr(test) )
			{
				//printf("%llu %llu\n", test, sqr(test));
				count++;
			}
			if ( A <= sqr(test2) && B >= sqr(test2) )
			{
				//printf("%llu %llu\n", test2, sqr(test2));
				count++;
			}
			power *= 10;
		}

		printf( "Case #%d: %d\n", t, count);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}