#include <stdio.h>
FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int T;
long long int N;
long long int state;
int res;

int main() {
	int t, i;
	fscanf(in, "%d", &T);
	for (t = 1; t <= T; t++) {
		fscanf(in, "%lld", &N);
		state = 0; res = -1;
		for (i = 1; i <= 1000000000; i++) {
			long long int temp = N * i;
			while (true) {
				if (temp == 0) break;
				state |= (1 << (temp % 10));
				temp /= 10;
			}
			if (state == 1023) { res = i; break; }
		}
		fprintf(out, "Case #%d: ", t);
		if (res < 0) fprintf(out, "INSOMNIA\n");
		else fprintf(out, "%lld\n", N * res);
	}
	return 0;
}