#include <stdio.h>
#include <stdlib.h>

char buf[2000];

int
solve(char buf[]) {
	int invite = 0;
	int score = 0;

	for (int s = 0; buf[s]; s++) {
		int n = buf[s] - '0';
		if (n == 0) 
			continue;
		if (s > score) {
			invite += s - score;
			score = s;
		}
		score += n;
	}
	return invite;
}

int
main(void) {
	int T;
	char *buf = (char *) malloc(2000);
	int smax;

	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d%s", &smax, buf);

		printf("Case #%d: %d\n", i, solve(buf));
	}

	return 0;
}
