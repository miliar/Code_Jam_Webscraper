#include <cstdio>
#include <vector>

using namespace std;

typedef vector<int> vi;

bool verify(vi &v) {
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == 0) return false;
	}

	return true;
}

void add(vi &v, unsigned long long n) {
	while (n > 0) {
		v[n % 10]++;
		n /= 10;
	}
}

int main(void) {
	int t;
	scanf("%d", &t);

	// Para cada caso de teste.
	for (int tc = 1; tc <= t; tc++) {
		int n;
		scanf("%d", &n);

		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", tc);
			continue;
		}

		vi v(10, 0);
		unsigned long long nn = n;
		unsigned long long f = 1;

		while (!verify(v)) {
			add(v, nn);
			nn = ++f * n;
		}

		nn = --f * n;

		printf("Case #%d: %llu\n", tc, nn);
	}

	return 0;
}