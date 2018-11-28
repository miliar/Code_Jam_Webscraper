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
int a[10005];
int main() {
	int i, j, n, m;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		i = 0;
		j = n - 1;
		int ans = 0;
		while (1) {
			if (i > j)
				break;
			if (a[i] + a[j] <= m) {
				i++;
				j--;
				ans++;
			} else {
				j--;
				ans++;
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
