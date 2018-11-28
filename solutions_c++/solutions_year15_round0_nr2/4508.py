#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int cnt[10];

int minMinutes(int i) {
	if (i <= 1) return i;
	if (cnt[i] == 0) return minMinutes(i-1);
	
	int sol = i;
	for (int j = i/2; j > 0; --j) {
		cnt[i-j] += cnt[i];
		cnt[j] += cnt[i];
		sol = min(sol, cnt[i] + minMinutes(i-1));
		cnt[i-j] -= cnt[i];
		cnt[j] -= cnt[i];
	}
	return sol;
}

int main() {
	int T, D, P;
	
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B.txt", "w", stdout);
	
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		memset(cnt, 0, 10 * sizeof(int));
		scanf("%d", &D);
		while (D--) {
			scanf("%d", &P);
			++cnt[P];
		}
		printf("Case #%d: %d\n", t, minMinutes(9));
	}
	
	return 0;
}
