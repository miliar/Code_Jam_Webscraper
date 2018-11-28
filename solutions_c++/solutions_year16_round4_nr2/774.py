#pragma comment (linker, "/STACK:256000000")
 
#define _USE_MATH_DEFINES
#define _CRT_NO_DEPRECEATE
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <memory.h>
#include <sstream>
#include <cassert>
#include <ctime>
#include <complex>
//#include <random>
 
using namespace std;
 
typedef unsigned int uint32;
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<int64, int> pli;
typedef pair<pii, pii> piiii;
typedef pair<int64, int> pli;
 
#define pb push_back
#define sq(x) ((x)*(x))
#define tmin(x,y,z) (min(min((x),(y)),(z)))
#define rand32() (((unsigned int)(rand()) << 16) | (unsigned int)(rand()))
#define rand64() (((unsigned int64)(rand32()) << 16) | (unsigned int64)(rand32()))
#define bit(mask, b) ((mask >> b) & 1)
#define biton(mask, bit) (mask | (((uint64)(1)) << bit))
#define bitoff(mask, bit) (mask & (~(((uint64)(1)) << bit)))
#define bitputon(mask, bit) (mask |= (((uint64)(1)) << bit))
#define bitputoff(mask, bit) (mask &= (~(((uint64)(1)) << bit)))
#define FAIL() (*((int*)(0)))++
#define INF ((int)(1e9) + 1337)
#define EPS (1e-3)
#define y1 yy1
#define y0 yy0
#define j0 jj0

const long double PI = acosl((long double)-1.0);

const int64 LINF = ((1ull << 63) - 1ull);

int test;

const int MAXN = 17;

int bc[1 << MAXN];

int n, k;
double p[MAXN];
double yes[1 << MAXN], no[1 << MAXN];
double val[1 << MAXN];
double ans;

void init()
{
	scanf ("%d%d", &n, &k);
	for (int i = 1; i <= n; i++)
	{
		scanf ("%lf", &p[i]);
	}
}

void solve()
{
	init();
	for (int mask = 0; mask < (1 << n); mask++)
	{
		if (bc[mask] == k / 2)
		{
			yes[mask] = no[mask] = 1.0;
			for (int i = 1; i <= n; i++)
			{
				if (mask & (1 << i - 1))
				{
					yes[mask] *= p[i];
					no[mask] *= 1.0 - p[i];
				}
			}
			//fprintf(stderr, "%d %.5lf %.5lf\n", mask, yes[mask], no[mask]);
		}
	}
	for (int mask = 0; mask < (1 << n); mask++)
	{
		if (bc[mask] == k)
		{
			val[mask] = 0.0;
			for (int smask = mask; smask; smask = mask & (smask - 1))
			{
				if (bc[smask] == k / 2)
				{
					int smask2 = mask ^ smask;
					val[mask] += yes[smask] * no[smask2];
				}
			}
			//fprintf(stderr, "%d %.5lf\n", mask, val[mask]);
		}
	}
	ans = 0.0;
	for (int mask = 0; mask < (1 << n); mask++)
	{
		if (bc[mask] == k)
		{
			ans = max(ans, val[mask]);
		}
	}
	printf("Case #%d: %.10lf\n", test, ans);
}

void precalc()
{
	for (int mask = 1; mask < (1 << 16); mask++)
	{
		bc[mask] = bc[mask & (mask - 1)] + 1;
	}
}

int main()
{
    //ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
    //freopen(TASK ".in", "rt", stdin); freopen(TASK ".out", "wt", stdout);
#endif
    srand(25);
	
	precalc();
	int tests = 1;
	
	scanf ("%d", &tests);
	for (test = 1; test <= tests; test++)
	{
		solve();
	}
	
    return 0;
}