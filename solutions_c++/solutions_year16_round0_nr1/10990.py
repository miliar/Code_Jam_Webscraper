#include <cstdio>
#include <cstring>

bool c[10];

bool check(long long x) {
	bool flag = true;

	// to digit
	while (x > 0) {
		int y = x % 10;
		c[y] = true;
		x /= 10;
	}

	// checking c array
	for (int i = 0; i < 10; i++) {
		if (c[i] == false) {
			flag = false;
			break;
		}
	}

	return flag;
}

void init() {
	memset(c, 0, sizeof(c));
}

int main() {
	// freopen("A-small-attempt0.in", "r", stdin);
	// freopen("A-small-attempt0.out", "w", stdout);
	// freopen("A-large.in", "r", stdin);
	// freopen("A-large.out", "w", stdout);

	int t;

	scanf("%d", &t);
	for (int itr = 1; itr <= t; itr++) {
		init();

		long long n;

		scanf("%lld", &n);

		printf("Case #%d: ", itr);
		if (n == 0) {
			printf("INSOMNIA\n");
		}
		else {
			long long ans = 0;
			for (int i = 1; ; i++) {
				if (check(n * i)) {
					ans = n * i;
					break;
				}
			}
			printf("%lld\n", ans);
		}
	}

	return 0;
}