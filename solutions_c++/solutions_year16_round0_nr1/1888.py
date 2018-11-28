#include <stdio.h>

int f(int x) {
	int mask=0;
	while (x>0){
		mask |= (1<<(x%10)); x/=10;
	}
	return mask;
}

int main() {
	int T; scanf("%d",&T);
	for (int t = 1; t <= T; ++t) {
		int N; scanf("%d",&N);
		printf("Case #%d: ", t);
		if (N == 0) {
			puts("INSOMNIA");
		} else {
			int s = N;
			int mask=f(N);
			while (mask != ((1<<10)-1)) {
				s+=N;
				mask |= f(s);
			}
			printf("%d\n", s);
		}

	}
	return 0;
}
