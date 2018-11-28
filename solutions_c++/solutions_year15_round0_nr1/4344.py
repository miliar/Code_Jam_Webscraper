#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>

int main(void) {
	FILE * iff = fopen("in", "r");
	FILE * off = fopen("out", "w");
	long N;
	char s[1010];
	int T;
	long sum;
	fscanf(iff, "%d", &T);
	for (int cse = 1; cse <= T; ++cse) {
		sum = 0;
		long res = 0;
		fscanf(iff, "%ld %s", &N, s);
		for (long i = 0; i <= N; ++i) {

			long si = s[i] - '0';
			if (sum < i && si != 0) {
				res += i - sum;
				sum += i - sum;
			}
			sum += si;
		}
		fprintf(off, "Case #%d: %ld\n",cse, res);
	}
	fclose(iff);
	fclose(off);
	return 0;
}