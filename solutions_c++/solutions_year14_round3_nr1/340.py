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
unsigned long long gcd ( unsigned long long a, unsigned long long b )
{
  unsigned long long c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

unsigned long long P, Q;
int gen;
void solve()
{
	unsigned long long g = gcd(P, Q);
	P /= g;
	Q /= g;

	mpz_class max_acc ("1099511627776", 10);
	char buf[30] = {0};
	char buf2[30] = {0};
	sprintf(buf, "%llu", P);
	sprintf(buf2, "%llu", Q);
	mpz_class p(buf);
	mpz_class q(buf2);
	if (max_acc % q != 0)
	{
		gen = -1;
		return;
	}
	mpz_class acc = (mpz_class)(max_acc / q) * p;
	mpz_class power = max_acc;

	for (int i = 1; i < 40; ++i)
	{
		power /= 2;
		if (acc >= power)
		{
			gen = i;
			return;
		}
	}

	gen = -1;
	return;
}

int main()
{
	int tt, T;
	int N, X, Y;

	scanf("%d\n", &T);

	for (tt = 1; tt <= T; ++tt)
	{
		scanf("%llu/%llu\n", &P, &Q);
		solve();
		if (gen > 0)
			printf("Case #%d: %d\n", tt, gen);
		else
			printf("Case #%d: impossible\n", tt);
	}
	return 0;
}
