#include <cstdio>
#include <cstring>
using namespace std;

char state[1003], click[1003];

void proc(int caseidx) {
	memset(state, 0, sizeof(state));
	memset(click, 0, sizeof(click));
	int n, k;
	scanf("%s %d", state, &k);
	n = strlen(state);
	for (int i = 0; i < n; ++i) {
		char val = (state[i] == '-') ? 1 : 0;
		state[i] = val;
	}

	printf("Case #%d: ", caseidx);
	int sum = 0, ans = 0;
	for (int i = 0; i < n; ++i) {
		int f = i - k, r = i - 1;
		if (f >= 0) {
			sum -= click[f];
		}
		if (r >= 0) {
			sum += click[r];
		}
		if (i <= n - k) {
			click[i] = (state[i] + sum) % 2;
			ans += click[i];
		}
		else {
			if ((state[i] + sum) % 2) {
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	printf("%d\n", ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}