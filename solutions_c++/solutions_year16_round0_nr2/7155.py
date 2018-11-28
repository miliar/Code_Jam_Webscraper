#include <stdio.h>
#include <string.h>

void flip(char stack[], int len, int nh_cnt, int *nstep) {
	if (nh_cnt == 0) return;
	int bound = 1;
	for (bound = 1; bound < len; ++bound) {
		if (stack[bound] != stack[0]) break;
	}
	for (int idx = 0; idx < bound; ++idx) {
		if (stack[idx] == '+') {
			stack[idx] = '-';
			++nh_cnt;
		} else {
			stack[idx] = '+';
			--nh_cnt;
		}	
	}
	(*nstep)++;
	// printf("%d: %s\n", *nstep, stack);
	flip(stack, len, nh_cnt, nstep);
}

int resolve(char stack[]) {
	int len = strlen(stack);
	int nh_cnt = 0;
	int nstep = 0;
	for(int idx = 0; idx < len; ++idx) {
		if (stack[idx] == '-') ++nh_cnt;
	}
	flip(stack, len, nh_cnt, &nstep);
	return nstep;
}

int main() {
	int T, idx = 0;
	char stack[128];
	scanf("%d", &T);
	while (idx < T) {
		scanf("%s", stack);
		// printf("%s\n", stack);
		int nstep = resolve(stack);
		printf("Case #%d: %d\n", idx+1, nstep);
		++idx;
	}

	return 0;
}