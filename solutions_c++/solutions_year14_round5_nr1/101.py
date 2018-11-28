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
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif


const int SIZE = 1<<20;

int n, p, q, r, s;
int arr[SIZE];
int64 sum[SIZE];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
		for (int i = 0; i<n; i++)
			arr[i] = ((int64(i) * p + q) % r + s);

		sum[0] = 0;
		for (int i = 0; i<n; i++) sum[i+1] = sum[i] + arr[i];

		int64 ans = 2*sum[n];
		for (int i = 0; i<=n; i++) {
			int64 rem = sum[n] - sum[i];
			int pos = lower_bound(sum+i, sum+n+1, sum[i] + rem/2) - sum;
			
			for (int j = pos-1; j<=pos+1; j++) if (j >= i && j <= n) {
				int64 tres = max(max(sum[i], sum[j]-sum[i]), sum[n]-sum[j]);
				ans = min(ans, tres);
			}
		}

		double ret = 1.0 - double(ans) / sum[n];

		printf("Case #%d: %0.15lf\n", tt, ret);
		fflush(stdout);
	}
	return 0;
}
