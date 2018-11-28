#include "stdio.h"
#include "string.h"
#include "math.h"
#include "set"
#include <gmpxx.h>

using namespace std;

/**************** debug ***************/
//#define DBG 1
#ifdef DBG
#define debug(...) { fprintf(stderr, "[%s:%d]", __func__, __LINE__);fprintf(stderr, __VA_ARGS__); };
#else
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

int A, N;
unsigned int v[128], tmp;
int trick;

void play(int A, int i, int cur_trick)
{
	debug("i=%d; A=%d; trick=%d\n", i, A, cur_trick);
	if (i == N)
	{
		SET_MIN(trick, cur_trick);
		return;
	}

	if (v[i] < A)
	{
		play(A+v[i], i+1, cur_trick);
		return;
	}
	
	if (A>1)
		play(A+A-1, i, cur_trick+1);
	play(A, i+1, cur_trick+1);
}

int main()
{
	int tt, T;
	int i, j;

	scanf("%d\n", &T);
	
	for (tt = 1; tt <= T; ++tt)
	{
		trick = 9999999;
		scanf("%d %d\n", &A, &N);
		for (i = 0; i < N; ++i)
			scanf("%d", &v[i]);

		for (i = N-1; i > 0; --i)
		{
			for (j = 1; j <= i; ++j)
			{
				if (v[j-1] > v[j])
				{
					tmp = v[j];
					v[j] = v[j-1];
					v[j-1] = tmp;
				}
			}
		}
#ifdef DBG
		fprintf(stderr, "[Case %d] %d: ", tt, A);
		for (i = 0; i < N; ++i)
			fprintf(stderr, "%d ", v[i]);
		fprintf(stderr, "\n");
#endif
#if 0
		for (i = 0; i < N; ++i)
		{
			if (v[i] < A)
			{
				A+=v[i];
				continue;
			}
			trick++;
			if (v[i] < A+A-1)
			{
				A+=(A-1);
				A+=v[i];
			}
		}
#endif
		play(A, 0, 0);
		printf("Case #%d: %d\n", tt, trick);
	}
	return 0;
}
