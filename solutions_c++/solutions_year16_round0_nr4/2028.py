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
int main() {
	int t, cas = 0;
	__int64 k, c, s;
	__int64 i, j;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%I64d%I64d%I64d", &k, &c, &s);
		if (s < (k + c - 1) / c) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		} else {
			printf("Case #%d:", cas);
			for (i = 0; i < k; i += c) {
				__int64 ans = 0;
				for (j = 0; j < c && (i + j < k); ++j) {
					ans *= k;
					ans += (i + j);
				}
				printf(" %I64d", ans + 1);
			}
			printf("\n");
		}
	}
}
