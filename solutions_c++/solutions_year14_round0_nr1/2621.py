#include <cstdio>
#include <cstring>

const int N = 20;

int visit[N][N], n, m;

int main() {
	freopen("A.in", "r", stdin);
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; ++ t) {
		scanf("%d", &n);
		memset(visit, 0, sizeof(visit));
		for (int i = 1; i <= 4; ++ i) {
			for (int j = 1; j <= 4; ++ j) {
				int x;
				scanf("%d", &x);
				visit[i][x] = true;
			}
		}
		scanf("%d", &m);

		int result = 0;
		int answer = 0;
		for (int i = 1; i <= 4; ++ i) {
			for (int j = 1; j <= 4; ++ j) {
				int x;
				scanf("%d", &x);
				if (i == m && visit[n][x]) {
					result ++;
					answer = x;
				}
			}
		}
		printf("Case #%d: ", t);
		if (result == 0) {
			puts("Volunteer cheated!");
		} else if (result > 1) {
			puts("Bad magician!");
		} else {
			printf("%d\n", answer);
		}
	}
	return 0;
}
