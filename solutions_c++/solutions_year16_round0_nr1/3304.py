#include <bits/stdc++.h>

using namespace std;

int n, ctr;
long long num, cur;
bool found[10];

void trackDigits(long long x) {
	while (x != 0) {
		if (found[x % 10] == false) {
			found[x % 10] = true;
			ctr++;
		}
		x /= 10;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		memset(found, false, sizeof(found));
		ctr = 0;
		scanf("%lld", &num);
		for (long long j = 1; j <= 1000000; j++) {
			cur = num * j;
			trackDigits(cur);
			if (ctr == 10) {
				printf("Case #%d: %lld\n", i + 1, cur);
				break;
			}
		}
		if (ctr != 10) {
			printf("Case #%d: INSOMNIA\n", i + 1);
		}
	}
}
