#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const char ch[] = {'P', 'R', 'S'};
int T, n, m, r, p, s;
char str[1 << 20];

void gao(int k) {
	if (2 * k + 1 >= m) return;
	if (str[k] == 'P') {
		str[2 * k + 1] = 'P';
		str[2 * k + 2] = 'R';
	} else if (str[k] == 'R') {
		str[2 * k + 1] = 'R';
		str[2 * k + 2] = 'S';
	} else if (str[k] == 'S') {
		str[2 * k + 1] = 'S';
		str[2 * k + 2] = 'P';
	}
	gao(2 * k + 1);
	gao(2 * k + 2);
}

void adj(int k, int len) {
	if (len-- == 0) return;
	adj(k, len);
	adj(k + (1 << len), len);
	if (strncmp(str + k, str + k + (1 << len), 1 << len) > 0) {
		for (int i = 0; i < (1 << len); ++i) {
			swap(str[k + i], str[k + (1 << len) + i]);
		}
	}
}

bool check() {
	int a = 0, b = 0, c = 0;
	for (int i = m >> 1; i < m; ++i) {
		a += str[i] == 'P';
		b += str[i] == 'R';
		c += str[i] == 'S';
	}
	return a == p && b == r && c == s;
}

int main() {
	scanf("%d", &T);
	for (int tT = 1; tT <= T; ++tT) {
		printf("Case #%d: ", tT);
		scanf("%d%d%d%d", &n, &r, &p, &s);
		m = (1 << n + 1) - 1;
		str[m] = '\0';
		for (int i = 0; i < 3; ++i) {
			str[0] = ch[i];
			gao(0);
			if (check()) {
				adj(m >> 1, n);
				break;
			}
		}

		puts(check()? str + (m >> 1) : "IMPOSSIBLE");
	}

	return 0;
}
