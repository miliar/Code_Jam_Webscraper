#include <iostream>
#include <cstdio>

using namespace std;

int n, t, i, j, nn, nnn;
bool b[11];

bool complete() {
	int ci;
	for (ci = 0; ci <= 9; ++ci)
		if (!b[ci]) return false;
	return true;
}

int main() {
	//freopen("./a.in", "r", stdin);
	//freopen("./a.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; ++i) {
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		for (j = 0; j <= 9; ++j) b[j] = false;
		nn = n;
		while (1 == 1) {
			nnn = nn;
			while (nnn != 0) {
				b[nnn % 10] = true;
				nnn /= 10;
			}
			if (complete()) break;
			nn += n;
		}
		printf("Case #%d: %d\n", i, nn);
	}
	return 0;
}
