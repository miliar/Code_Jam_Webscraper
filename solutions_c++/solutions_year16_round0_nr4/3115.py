#include <stdio.h>

int main() {
	FILE* in = fopen("problem.txt", "r");
	FILE* out = fopen("solve.txt", "w");

	int T;
	fscanf(in, "%d", &T);
	
	for (int times = 1; times <= T;times++){
		int K, C, S;
		fscanf(in, "%d %d %d", &K, &C, &S);
		fprintf(out, "Case #%d: ", times);
		for (int i = 1; i <= K; i++) {
			fprintf(out, "%d ", i);
		}
		fprintf(out, "\n");
	}

}