#include <bits/stdc++.h>

int T, n;
bool a[10];

bool full() {
	for (int i = 0; i < 10; i++) {
		if (!a[i]) return false;
	}
	return true;
}

void sign(int n) {
	char s[20];
	sprintf(s, "%d", n);
	for (int i = 0, l = strlen(s); i < l; i++) {
		a[s[i] - '0'] = true;
	}
}

int main() {
	// freopen("input.txt", "r", stdin);
	std::cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		std::cin >> n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", cs);
			continue;
		}
		std::fill(a, a + 10, false);
		int tmp = n;
		for (; !full(); sign(tmp), tmp += n);
		printf("Case #%d: %d\n", cs, tmp - n);
	}
	return 0;
}
