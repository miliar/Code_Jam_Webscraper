#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int step(vector <int> &cnt, int n) {
	while (n) {
		cnt[n%10]++;
		n /= 10;
	}
	for (int i = 0; i < 10; i++)
		if (cnt[i] == 0) return 0;
	return 1;
}

int solve(int n) {
	vector <int> cnt(10, 0);
	for (int i = 1; i <= 10000; i++) {
		bool c = step(cnt, i*n);
		if (c) return i*n;
	}
	return -1;
}

int main() {
	freopen("A-large.in", "r", stdin);
	int t; scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		int n; scanf("%d", &n);
		printf("Case #%d: ", tt);
		int ret = solve(n);
		if (ret == -1) printf("INSOMNIA\n");
		else printf("%d\n", ret);
	}
	return 0;
}
