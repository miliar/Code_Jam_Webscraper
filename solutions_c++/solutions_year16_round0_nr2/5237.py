#include <cstdio>
#include <cstring>

char s[120];

void flip(const size_t &p) {
	for (int i = 0; i <= p; ++i) {
		if (s[i] == '+') {
			s[i] = '-';
		} else {
			s[i] = '+';
		}
	}
}

int solve() {
	size_t n = strlen(s);
	int res = 0;
	for (int i = n-1; i >= 0; --i) {
		if (s[i] == '+')
			continue;
		flip(i);
		++res;
	}
	return res;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		scanf("%s", s);
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}