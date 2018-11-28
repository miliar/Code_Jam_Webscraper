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
using namespace std;
int a[1005], b[1005];
int main() {
	int i, j, k, n;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		for (i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b, b + n);
		int ans = 0;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < n; ++j) {
				if (a[j] == b[i])
					break;
			}
			int l, r;
			l = r = 0;
			for (k = 0; k < j; ++k) {
				if (a[k] > a[j])
					l++;
			}
			for (k = j + 1; k < n; ++k) {
				if (a[k] > a[j])
					r++;
			}
			ans += min(l, r);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
