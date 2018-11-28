#include <stdio.h>
#include <string.h>
#include <vector>
#include <math.h>

int main() {

	FILE* in = fopen("D-small-attempt0.in", "rb");
	FILE* out = fopen("D-small-out.txt", "wb");

	int n = 0;
	fscanf(in, "%d", &n);

	for(int i = 1; i <= n; ++ i) {
		int K, C, S;

		fscanf(in, "%d%d%d", &K, &C, &S);
		
		fprintf(out, "Case #%d:", i);

		if(K == S) {
			for(int j = 0; j < K; ++ j) {
				fprintf(out, " %d", j + 1);
			}
			fprintf(out, "\n");
		} else {
			fprintf(out, " IMPOSSIBLE\n");
		}
	}

	return 0;
}