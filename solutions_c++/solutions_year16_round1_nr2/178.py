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
#include <queue>

using namespace std;

int a[10005];
int main() {
	int t, cas = 0;
	int i, j, k, n;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		k = 0;
		for (i = 0; i < 2 * n - 1; ++i) {
			for (j = 0; j < n; ++j) {
				scanf("%d", &a[k]);
				k++;
			}
		}

		sort(a, a + k);
		int last = -1;
		printf("Case #%d:", cas);
		for (i = 0; i < k; ++i) {
			if (last == -1) {
				last = a[i];
			} else if (last != a[i]) {
				printf(" %d", last);
				last = a[i];
			} else {
				last = -1;
			}
		}
		if (last != -1) {
			printf(" %d", last);
		}
		puts("");
	}
}
