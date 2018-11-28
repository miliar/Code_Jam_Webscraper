#include <cstdio>

int T, n, s;
bool p[10];

bool all(const bool p[]) {
	bool res = true;
	for (int i = 0; i < 10; ++i) res &= p[i];
	return res;
}

int main() {
	scanf("%d", &T);
	for (int iT = 1; iT <= T; ++iT) {
		printf("Case #%d: ", iT);
		scanf("%d", &n);
		if (n == 0) {
			puts("INSOMNIA");
			continue;
		}
		for (int i = 0; i < 10; ++i) p[i] = false;
		s = 0;
		for (;;) {
			s += n;
			for (int i = s; i; i /= 10) p[i % 10] = true;
			if (all(p)) {
				printf("%d\n", s);
				break;
			}
		}
	}
	return 0;
}
