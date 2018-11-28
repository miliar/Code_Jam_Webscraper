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

string best[13][3];
int cnt[13][3][3];
string c[3] = {"R", "P", "S"};

int x[3];
int n;

void init()
{
	scanf ("%d", &n);
	for (int i = 0; i < 3; i++)
	{
		scanf ("%d", &x[i]);
	}
}

void solve()
{
	init();
	string ans = "Z";
	for (int i = 0; i < 3; i++)
	{
		if (!best[n][i].empty() && cnt[n][i][0] == x[0] && cnt[n][i][1] == x[1] && cnt[n][i][2] == x[2])
		{
			ans = min(ans, best[n][i]);
		}
	}
	printf("Case #%d: ", test);
	if (ans.size() == (1 << n))
	{
		printf("%s\n", ans.c_str());
	}
	else
	{
		printf("IMPOSSIBLE\n");
	}
}

void precalc()
{
	for (int i = 0; i < 3; i++)
	{
		best[0][i] = c[i];
		cnt[0][i][i] = 1;
	}
	for (int l = 1; l <= 12; l++)
	{
		for (int i = 0; i < 3; i++)
		{
			vector <int> c;
			for (int j = 0; j < 3; j++)
			{
				c.push_back(cnt[l - 1][i][j] + cnt[l - 1][(i + 2) % 3][j]);
			}
			string s1 = best[l - 1][i] + best[l - 1][(i + 2) % 3];
			string s2 = best[l - 1][(i + 2) % 3] + best[l - 1][i];
			if (s2 < s1)
			{
				swap(s1, s2);
			}
			if (s1.size() == (1 << l))
			{
				best[l][i] = s1;
				for (int j = 0; j < 3; j++)
				{
					cnt[l][i][j] = c[j];
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