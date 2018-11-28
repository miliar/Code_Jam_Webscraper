#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>

using namespace std;

typedef long long ll;
typedef long long li;
typedef unsigned int uint;
typedef unsigned long long ull;

#define TASKNAME "delete"

void Solution();

int main()
{
#ifdef DEBUG
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#else
#endif
	Solution();
	return 0;
}

int used[20];

void Solution()
{
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		double c, f, x, v = 2, ct = 0;
		scanf("%lf%lf%lf", &c, &f, &x);
		while (true)
		{
			double t1 = x / v, t2 = (c / v) + x / (f + v);
			if (t1 + 1e-9 < t2) { ct += t1; break; }
			else ct += c / v, v += f;
		}
		printf("Case #%d: %.7lf\n", test, ct);
	}
}