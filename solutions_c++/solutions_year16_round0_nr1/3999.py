#include <stdio.h>
#include <iostream>
using namespace std;

int t, n, now, res;
bool flag[10];

void check(int now) {
	int k;

	while (now > 0) {
		k = now % 10;
		if (not flag[k]) {
			res--;
			flag[k] = true;
		}
		now /= 10;
	}
}

int solve(int n) {
	int k;

	if (n == 0) return -1;

	for (int i = 0;i < 10;++i)
		flag[i] = false;
	res = 10;
	k = 1;
	while (res > 0) {
		//printf("%d\n", res);
		now = k * n;
		check(now);
		k += 1;
	}

	return now;


}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//printf("sdf");
	scanf("%d", &t);
	for (int i = 1;i <= t;++i) {
		scanf("%d", &n);
		int ans = solve(n);
		printf("Case #%d: ", i);
		if (ans == -1) printf("INSOMNIA\n");
		else printf("%d\n", ans);
	}

	return 0;
}