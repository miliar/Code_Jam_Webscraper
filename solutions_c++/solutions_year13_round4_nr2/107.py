#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

int n;
int64 p;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%I64d", &n, &p);

		int q;
		for (q = 0; q<n; q++)
			if (p < (1LL<<q))
				break;
		int64 canwin = (1LL<<n) - (1LL<<(n-q+1));

		for (q = 0; q<n; q++)
			if (!((p-1) & (1LL<<(n-1-q)))) break;
		int leadu = q;
		int64 mustwin = (1LL<<(leadu+1)) - 2;

		if (p == (1LL<<n)) {
			canwin = (1LL<<n) - 1;
			mustwin = (1LL<<n) - 1;
		}


		printf("Case #%d: %I64d %I64d\n", tt, mustwin, canwin);
		fflush(stdout);
	}
	return 0;
}
