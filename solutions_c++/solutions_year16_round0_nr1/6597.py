#include<cstdio>
using namespace std;

void fill(int x, bool check[10]) {
	while (x) {
		check[x % 10] = true;
		x = x / 10;
	}
}

bool fallasleep(bool check[10]) {
	for (int i = 0; i < 10; i++)
		if (!check[i])
			return false;
	return true;
}

int main(void) {
	int T;
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; testcase++) {
		int N;
		scanf("%d", &N);

		printf("Case #%d: ", testcase);

		if (N == 0) {
			printf("INSOMNIA\n");
		} else {
			bool check[10] = {false, };
			for (int i = 1;; i++) {
				fill(i * N, check);
				if (fallasleep(check)) {
					printf("%d\n", i * N);
					break;
				}
			}
		}
	}
	return 0;
}

