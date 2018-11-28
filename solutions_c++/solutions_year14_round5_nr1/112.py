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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
using namespace std;
__int64 a[1000005];
int main() {
	int i;
	int t, cas = 0;
	int n, p, q, r, s;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
		for (i = 0; i < n; ++i) {
			a[i] = ((__int64) i * (__int64) p + (__int64) q) % (__int64) r
					+ (__int64) s;
		}
		int j;
		__int64 sum1, sum2, sum3, sum;
		j = 0;
		sum1 = 0;
		sum2 = 0;
		sum3 = 0;
		sum = 0;
		for (i = 0; i < n; ++i) {
			sum3 += a[i];
		}
		sum = sum3;
		__int64 ans = sum;
		for (i = 0; i <= n; ++i) {
			//printf("%I64d %I64d %I64d\n", sum1, sum2, sum3);
			while (sum3 > sum2) {
				sum2 += a[j];
				sum3 -= a[j];
				j++;
			}
			ans = min(ans, max(sum1, max(sum2 - a[j - 1], sum3 + a[j - 1])));
			ans = min(ans, max(sum1, max(sum2, sum3)));
			if (i == n)
				break;
			sum1 += a[i];
			sum2 -= a[i];
		}
		printf("Case #%d: %.12lf\n", cas, (double) (sum - ans) / (double) sum);
	}
}
