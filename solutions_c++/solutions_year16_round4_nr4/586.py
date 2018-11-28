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

int n;
bool can[5][5];
bool good[5][1 << 16];
bool valid[5][1 << 16];
int d[5][1 << 16];
char buf[100];

void init()
{
	memset(can, 0, sizeof(can));
	scanf ("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf ("%s", &buf);
		for (int j = 0; j < n; j++)
		{
			can[i][j] = (buf[j] == '1');
		}
	}
}

bool used[5];
bool could[5][5];

int rec(int n, int w, int m)
{
	if (m >= n)
	{
		int res = 0;
		for (int i = 0; i < 4; i++)
		{
			if (used[i])
			{
				res++;
			}
		}
		return res;
	}
	else
	{
		if (!could[w][m])
		{
			return rec(n, w, m + 1);
		}
		else
		{
			int res = 0;
			for (int i = 0; i < n; i++)
			{
				if (could[i][m] && i != w && !used[i])
				{
					used[i] = true;
					res = max(res, rec(n, w, m + 1));
					used[i] = false;
				}
			}
			return res;
		}
	}
}

bool check(int n, int mask)
{
	memset(could, 0, sizeof(could));
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			could[i][j] = (mask & (1 << (i * 4 + j)));
		}
	}
	for (int i = 0; i < n; i++)
	{
		int mcnt = 0;
		for (int j = 0; j < n; j++)
		{
			if (could[i][j])
			{
				mcnt++;
			}
		}
		int r = rec(n, i, 0);
		if (r >= mcnt)
		{
			return false;
		}
	}
	return true;
}

int get_mask()
{
	int mask = 0;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (can[i][j])
			{
				mask |= (1 << i * 4 + j);
			}
		}
	}
	return mask;
}

void solve()
{
	init();
	int init_mask = get_mask();
	printf("Case #%d: %d\n", test, d[n][init_mask]);
}

bool is_valid(int n, int mask)
{
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			bool could = (mask & (1 << (i * 4 + j)));
			if (could && (i >= n || j >= n))
			{
				return false;
			}
		}
	}
	return true;
}

void precalc()
{
	memset(d, 127, sizeof(d));
	for (int i = 1; i <= 4; i++)
	{
		for (int mask = 0; mask < (1 << 16); mask++)
		{
			valid[i][mask] = is_valid(i, mask);
			if (valid[i][mask])
			{
				good[i][mask] = check(i, mask);
				if (good[i][mask])
				{
					d[i][mask] = 0;
					/*if (i <= 2)
					{
						fprintf(stderr, "n %d mask %d\n", i, mask);
					}*/
				}
			}
		}
		for (int mask = (1 << 16) - 1; mask > 0; mask--)
		{
			if (valid[i][mask])
			{
				for (int j = 0; j < 16; j++)
				{
					if (mask & (1 << j))
					{
						int smask = mask ^ (1 << j);
						d[i][smask] = min(d[i][smask], d[i][mask] + 1);
					}
				}
			}
		}
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