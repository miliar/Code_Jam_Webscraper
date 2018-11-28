#include <stdio.h>

int T;
int R, C, W;

int main(void) {
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%d%d%d", &R, &C, &W);
		printf("Case #%d: %d\n", t, ((C - 1) / W + W) * R);
	}
	return 0;
}