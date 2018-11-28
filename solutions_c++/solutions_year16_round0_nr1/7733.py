#include <stdio.h>
#include <memory.h>
const int NMAX = 200;

int visited[10];

bool checkNumbers(int a) {

	while (a != 0) {
		visited[a % 10] = 1;
		a /= 10;
	}
	for (int i = 0; i <= 9; i++) {
		if (visited[i] == 0) return false;
	}
	return true;
}
int main() {

	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T, n, z;
	scanf("%d", &T);
	for (z = 1; z <= T; z++) {
		memset(visited, 0, sizeof(visited));
		scanf("%d", &n);
		int j;
		if (n < 0) n = n*(-1);
		else if (n == 0) {
			printf("Case #%d: INSOMNIA\n",z); continue;
		}
		for (j = 1;; j++) {
			if (n * j < 0) break;
			if (checkNumbers(n * j)) {
				break;
			}
		}
		if (n * j < 0) printf("Case #%d: INSOMNIA\n",z);
		else printf("Case #%d: %d\n", z,n*j);
	}
	return 0;
}