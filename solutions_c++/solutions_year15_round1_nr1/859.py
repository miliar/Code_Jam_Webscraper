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

using namespace std;

int a[1005];
int main() {
	int i, j, k, n;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		__int64 ans1, ans2;
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		ans1 = ans2 = 0;
		ans2 = 0;
		__int64 mx = 0;
		for (i = 1; i < n; ++i) {
			ans1 += max(a[i - 1] - a[i], 0);
			mx = max(mx, (__int64) a[i - 1] - a[i]);
		}
		for (i = 0; i < n - 1; ++i) {
			ans2 += min(mx, (__int64) a[i]);
		}

		printf("Case #%d: %I64d %I64d\n", cas, ans1, ans2);
	}
}

