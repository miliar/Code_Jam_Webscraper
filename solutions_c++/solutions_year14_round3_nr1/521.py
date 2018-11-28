#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <math.h>

#include <algorithm>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>

#define FOR(var, size) for (int (var) = 0; (var) < (size); (var)++)

using namespace std;
const int inf = 0x7fffffff;
typedef long long int llint;
const double eps = 1e-10;
//const double inf = 1e+309;

llint gcd(llint a, llint b)
{
	return b > 0 ? gcd(b, a % b) : a;
}

void solve()
{
	llint p, q, g;
	scanf("%lld/%lld", &p, &q);
	g = gcd(p, q);
	p /= g;
	q /= g;
	
	if ((q&(q-1)) != 0) {
		printf("impossible\n");
		return;
	}
	
	int sol = 0;
	while (q > p) {
		q /= 2;
		sol++;
	}

	printf("%d\n", sol);
}


int main()
{
	int t, i;
	
	scanf("%d", &t);
	
	for (i = 0; i < t; i++) {
		printf("Case #%d: ", i+1);
		solve();
	}
	
	return 0;
}

