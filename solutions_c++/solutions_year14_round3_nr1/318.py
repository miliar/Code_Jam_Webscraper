#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <string>
#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)
#define all(x) (x).begin(), (x).end()
#define se second
#define fi first
#define mp make_pair
#define pb push_back
#define op operator
typedef vector <int> vi;
typedef pair<int, int> pii;
typedef long long i64;

i64 gcd(i64 x, i64 y)
{
	if (x == 0 || y == 0)
		return x + y;
	if (x > y)
		return gcd(x % y, y);
	else return gcd(x, y % x);
}

inline void mk(i64 & x, i64 & y)
{
	i64 g = gcd(x, y);
	x /= g;
	y /= g;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	fore(test, 1, tests)
	{
		i64 P, Q;
		printf("Case #%d: ", test);
		scanf("%lld/%lld", &P, &Q);
		mk(P, Q);
		i64 tmp = 1;
		while(tmp < Q)
			tmp *= 2;
		if (tmp != Q)
		{
			printf("impossible\n");
			continue;
		}
		if (P * 2 >= Q)
		{
			printf("1\n");
			continue;
		}
		P *= 2;
		mk(P, Q);
		int it = 2;
		bool found = false;
		for (i64 choice = Q / 2; choice >= 1; choice /= 2, it++)
		{
			if (P >= choice)
			{
				printf("%d\n", it);
				found = true;
				break;
			}
		}
		if (!found)
			assert(false);
	}

	return 0;
}