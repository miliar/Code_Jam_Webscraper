#include <cstdio>
using namespace std;

int main() {
	int T, t;
	int a, n;
	int i, j;
	bool b[17];
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d", &a);
		for (i = 1; i <= 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf("%d", &n);
				b[n] = (i == a);
			}
		}
		scanf("%d", &a);
		for (i = 1; i <= 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf("%d", &n);
				b[n] = b[n] && (i == a);
			}
		}
		n = 0;
		for (i = 1; i <= 16; i++) {
			if (b[i]) {
				n = (n == 0) ? i : -1;
			}
		}
		printf("Case #%d: ", t);
		if (n == 0) {
			puts("Volunteer cheated!");
		} else if (n == -1) {
			puts("Bad magician!");
		} else {
			printf("%d\n", n);
		}
	}
	return 0;
}