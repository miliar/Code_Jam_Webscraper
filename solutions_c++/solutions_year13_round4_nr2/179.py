#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double ldouble;

ll n, p;

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int tst; scanf("%d", &tst);
	for (int ts = 1; ts <= tst; ts++)
	{
		printf("Case #%d: ", ts);
		scanf("%lld%lld", &n, &p);
		ll x = 1, t = 0;
		if ((1ll << n) == p) printf("%lld", p - 1);
		else
		{
			while (x <= n && (t + (1ll << (n - x)) < p)) t += (1ll << (n - x)), x++; x--;
			printf("%lld", (1ll << (x + 1ll)) - 2ll);
		}
		x = 0;
		while ((1ll << x) <= p) x++; x--;
		x = n - x;
		printf(" %lld\n", (1ll << n) - (1ll << x));
	}

	return 0;
}