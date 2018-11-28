#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef map<int, int> mii;

int T;
int R, C;
int W;

void solve()
{
	if (W == C) {
		printf("%d", W);
		return;
	}

	if (W == 1) {
		printf("%d", R * C);
		return;
	}

	int tot = 2 * W - 1;
	int cnt = 1;
	if (tot >= C) {
		printf("%d", W + 1);
		return;
	}

	while (tot < C) {
		++cnt;
		tot += W;
	}
	cnt += W - 1;
	if (tot - W + 1 < C) {
		cnt++;
	}
	cnt *= R;
	printf("%d",cnt);
}

int main()
{
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d %d", &R, &C, &W);
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
	return 0;
}
