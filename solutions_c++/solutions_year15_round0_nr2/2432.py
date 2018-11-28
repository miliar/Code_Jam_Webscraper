#include <stdio.h>
#include <string.h>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <map>
#include <bitset>

#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c --a)
#define pb push_back
#define mp make_pair
using namespace std;

int main() {
	int n, T, pancake[1005];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		int ans = 0;

		scanf("%d", &n);

		REP(i, n) {
			scanf("%d", &pancake[i]);
			ans = max(pancake[i], ans);
		}

		FORU(i, 1, ans) {
			int addTime = 0;

			REP(j, n) {
				if (pancake[j] <= i)
					continue;

				addTime += (pancake[j] - i) / i;

				if (pancake[j] % i != 0)
					++addTime;
			}

			ans = min(ans, addTime + i);
		}

		printf("Case #%d: %d\n", tc, ans);
	}	

	return 0;
}
