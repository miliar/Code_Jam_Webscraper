#include <cstdio>

int main() {
	int T, r, total;
	int t;
	while(scanf("%d", &T) != EOF) {
		for (int cases = 1; cases <= T; ++cases) {
			scanf("%d %d", &r, &t);
			total = 0;
			//printf("t %d\n", t);
			while(1) {
				t -= (((r + 1) * (r + 1)) - (r * r));
				if(t >= 0)
					total++;
				else
					break;
				r += 2;

			}
			printf("Case #%d: %d\n", cases, total);
		}
	}
	return 0;
}
