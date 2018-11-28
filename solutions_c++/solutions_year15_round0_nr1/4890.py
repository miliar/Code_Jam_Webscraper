#include "stdio.h"
#include "string.h"
#include "math.h"
#include "set"
#include "algorithm"
#include <gmpxx.h>

using namespace std;

/**************** debug ***************/
//#define DBG 1
#ifdef DBG
#define chkpoint(...) { fprintf(stderr, "[%s:%d]", __func__, __LINE__);fprintf(stderr, __VA_ARGS__); };
#define debug(...) { fprintf(stderr, __VA_ARGS__); };
#else
#define chkpoint(...) 
#define debug(...) 
#endif
/**************** debug ***************/

/**************** Useful macro ***************/
#define MIN(a, b) (((a)<(b))?(a):(b))
#define MAX(a, b) (((a)>(b))?(a):(b))
#define SET_MIN(a, b) a = MIN(a, b)
#define SET_MAX(a, b) a = MAX(a, b)
#define MPZ2STR(x) (x.get_str(10).c_str())
/**************** Useful macro ***************/
double solve(int N, int X, int Y)
{
	return 0;
}

int main()
{
	int tt, T;

	scanf("%d\n", &T);
	
	for (tt = 1; tt <= T; ++tt)
	{
		int N, x, more = 0, missing = 0;
		scanf("%d ", &N);
		for (int i = 0; i <= N ; ++i)
		{
			scanf("%1d", &x);
			if (x == 0)
			{
				if (more > 0)
					more --;
				else
					missing++;
			}
			else
				more += (x-1);
		}
		printf("Case #%d: %d\n", tt, missing);
	}
	return 0;
}
