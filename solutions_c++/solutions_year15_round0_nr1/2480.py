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
	int smax, T;
	char audience[1005];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		scanf("%d %s", &smax, audience);

		int ans = 0, numAudience = 0;

		REP(i, smax + 1) {
			if ((audience[i] != '0') && (ans + numAudience < i)) {
				ans = max(ans, i - numAudience);
			}

			numAudience += (audience[i] - '0');
		}

		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}
