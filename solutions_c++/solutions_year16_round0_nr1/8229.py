#include <bits/stdc++.h>

void check(bool f[10], long long j) {
	while (j != 0) {
		f[j%10] = true;
		j /= 10;
	}
}

bool benar(bool f[10]) {
	for (int i = 0; i < 10; i++){
		if (!f[i]) return true;
	}
	return false;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int x;
		long long ans;
		bool f[10];
		memset(&f, false, sizeof(f));
		scanf("%d", &x);
		if (x == 0) {
			printf("Case #%d: %s\n", i, "INSOMNIA");
			continue;
		}
		for (long long j = x, k = 1; benar(f); j = (k+1)*x, k++) {
			ans = j;
			check(f, j);
		}
		printf("Case #%d: %lld\n", i, ans);
	}
}

