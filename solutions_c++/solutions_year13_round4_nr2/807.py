#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <climits>
#include <sstream>
#include <cstring>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define INF (INT_MAX/3)

typedef long long lint;

using namespace std;

lint bla(int n, lint manywin)
{
	lint bits[n];
	lint ret = 0;

//	fprintf(stderr, "Many win = %lld\n", manywin);

	for (lint i = 0; i < n; i++) {
		bits[i] = manywin&1;
		manywin >>= 1;
	}      

	for (int i = 0; i < n; i++) {
		if (bits[i])
			ret += 1<<(n-1-i);
	}

//	fprintf(stderr, "Ret = %lld\n", ret);
	
	return ret;
}

int main(int argc, char ** argv)
{
	lint ntest;

	scanf("%lld", &ntest);

	for (lint test = 0; test < ntest; test++) {
		lint n, manywin;
		lint maxalways = 0, maxcan = 0;

		scanf("%lld %lld", &n, &manywin);

		if (manywin == 1LL<<(n)) {
			printf("Case #%d: %lld %lld\n", test+1, (1LL<<n)-1, (1LL<<n)-1);
			continue;
		}

		manywin --;


		lint copy = manywin;

		lint bits[n];

		for (lint i = 0; i < n; i++) {
			bits[i] = manywin&1;
			manywin >>= 1;
		}

		manywin = copy;

		for (lint i = n-1; i >= 0; i--) {
			if (bits[i])
				maxalways += 1<<(n-i);
			else
				break;
		}

		for (lint x = 0; x <= manywin; x++)
			maxcan = max(maxcan, bla(n, x));

		for (lint i = 0; i < n; i++) {
		}


		printf("Case #%d: %d %d\n", test+1, maxalways, maxcan);
	}

	return 0;
}
