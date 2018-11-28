#include "bits/stdc++.h"
using namespace std;

int kase, Left, times;
long long n, cur;
bool Has[10];

void Check() {
	int copy = cur;
	if (copy <= 0 && !Has[0]) {
		Has[0] = true; Left -= 1;
	}
	while (copy != 0) {
		int c = copy % 10;
		if (!Has[c]) { Has[c] = true; Left -= 1; };
		copy /= 10;
	}
	cur += n;
	times += 1;
}

int main() {
	freopen("out", "w", stdout);
	freopen("in", "r", stdin);
	scanf("%d", &kase);
	for (int nCase = 1; nCase <= kase; ++nCase) {
		printf("Case #%d: ", nCase);
		scanf("%I64d", &n);
		Left = 10; cur = n; times = 0;
		memset(Has, 0, sizeof(Has));
		while (times < 1000000 && Left > 0)
			Check();
		if (times < 1000000)
			printf("%I64d\n", cur - n);
		else
			puts("INSOMNIA");
	}
	return 0;
}
