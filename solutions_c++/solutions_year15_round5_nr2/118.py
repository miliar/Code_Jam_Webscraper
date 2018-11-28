#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 1020;

int n, k, sum[MAX];

void input() {
	scanf("%d%d", &n, &k);

	int i;
	for(i = 0; i < n-k+1; i++)
		scanf("%d", &sum[i]);
}

int diff[MAX], minDelta[MAX], maxDelta[MAX];

void calcDiff() {
	int i;
	for(i = 0; i < k; i++)
		minDelta[i] = maxDelta[i] = 0;
	for(i = 0; i < k; i++) {
		int now = i, delta = 0;
		while(now + k < n) {
			delta += sum[now+1]-sum[now];
			minDelta[i] = min(minDelta[i], delta);
			maxDelta[i] = max(maxDelta[i], delta);

			now += k;
		}
	}
}

int solve() {
	int maxDiff = 0;

	int i;
	for(i = 0; i < k; i++)
		maxDiff = max(maxDiff, maxDelta[i]-minDelta[i]);

	int margin = 0, mins = 0;
	for(i = 0; i < k; i++) {
		margin += maxDiff - (maxDelta[i]-minDelta[i]);
		mins -= minDelta[i];
	}

	int remain = (sum[0]-mins)%k;
	if(remain < 0) remain += k;
	return remain > margin ? maxDiff+1 : maxDiff;
}

int main() {
	freopen("B.out", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);

	for(nowCase = 1; nowCase <= numCase; nowCase++) {
		input();

		calcDiff();
		printf("Case #%d: %d\n", nowCase, solve());
	}

	return 0;
}