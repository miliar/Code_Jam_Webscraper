#include <stdio.h>
int main() {
	freopen("A-small-attempt1 (1).in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int count = 1; count <= t; count++) {
		int r, t;
		scanf("%d%d", &r, &t);
		int times = 0;
		int time = 2 * r + 1;
		while(t >= time) {
			t -= time;
			times++;
			time += 4;
		}
		printf("Case #%d: %d\n", count, times);
	}
}