#include "stdio.h"
#include "string.h"
#include "string"
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
char quaternions(char a, char b)
{
	//1, -1, i, j, k, -i, -j, -k
	if (a == 1 || a == -1 || b == 1 || b == -1)
		return a*b;
	
	int sign = 1;
	if (a * b < 0)
		sign = -1;
	a = abs(a);
	b = abs(b);

	if (a == b)
		return -1 * sign;
	else if (a == 'i' && b == 'j')
		return 'k' * sign;
	else if (a == 'i' && b == 'k')
		return -'j' * sign;
	else if (a == 'j' && b == 'i')
		return -'k' * sign;
	else if (a == 'j' && b == 'k')
		return 'i' * sign;
	else if (a == 'k' && b == 'i')
		return 'j' * sign;
	else if (a == 'k' && b == 'j')
		return -'i' * sign;
	else
	{
		printf("ERROR!!!!!!!!!!!!!\n");
		fprintf(stderr, "ERROR!!!!!\n");
		return 1;
	}
}

bool solve(int L, int X, char* pattern)
{
	for (int x = 1; x <= X; ++x)
		for (int l = 0; l < L; ++l)
			pattern[L*x+l] = pattern[l];

	char result = 1;
	char found = 0;
	for (int i = 0; i < L*X; ++i)
	{
		debug(">> i=%d\n", i);
		result = quaternions(result, pattern[i]);
		if (found == 0)
		{
			if (result == 'i')
			{
				result = 1;
				found = 1;
			}
		}
		else if (found == 1)
		{
			if (result == 'j')
			{
				result = 1;
				found = 2;
			}
		}
	}
	if (found == 2 && result == 'k')
		return true;
	else
		return false;
}

int main()
{
	int tt, T;

	scanf("%d\n", &T);
	
	for (tt = 1; tt <= T; ++tt)
	{
		int L, X;
		char pattern[10240];
		scanf("%d %d\n", &L, &X);
		scanf("%s\n", &pattern);
		printf("Case #%d: %s\n", tt, solve(L, X, pattern)?"YES":"NO");
	}
	return 0;
}
