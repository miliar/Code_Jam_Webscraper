#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

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
#include <unordered_map>
#include <unordered_set>
#include <bitset>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<int64, int> pli;

const int INF = (int)(1e9+1e5);
const int64 LINF = (int64)(4e18);
const double EPS = 1e-10;
const int MOD = (int)1e9 + 7;
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)0)++)
#define y0 y00

int tnum;

const int MAXN = 1005;

char s[MAXN];
int n, k;

void init()
{
	scanf ("%s %d", &s[1], &k);
	n = strlen(s + 1);
}

void solve()
{
	init();
	int ans = 0;
	for (int i = 1; i + k - 1 <= n; i++)
	{
		if (s[i] == '-')
		{
			ans++;
			for (int j = i; j < i + k; j++)
			{
				s[j] = s[j] == '+' ? '-' : '+';
			}
		}
	}
	for (int i = 1; i <= n; i++)
	{
		if (s[i] == '-')
		{
			ans = -1;
			break;
		}
	}
	printf("Case #%d: ", tnum);
	if (ans == -1)
	{
		printf("IMPOSSIBLE\n");
	}
	else
	{
		printf("%d\n", ans);
	}
}

int main()
{
	//srand(time(0)); testgen(10, 5, 30);
    ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#endif

    double st = clock();
    int tests = 1;
    scanf ("%d", &tests);
    for (tnum = 1; tnum <= tests; tnum++)
    {
    	solve();
    }

    //fprintf(stderr, "%.3lf\n", (clock() - st) / CLOCKS_PER_SEC);
    return 0;
}
