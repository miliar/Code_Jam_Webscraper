#include<stdio.h>
#include<string.h>


int main()
{

	FILE *in = fopen("A.in", "r");
	FILE *out = fopen("out.txt", "w");
	int T; fscanf(in, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fprintf(out, "Case #%d: ", t);
		
		int N, i, j, senator[1000], sum = 0, max_i;
		fscanf(in, "%d", &N);

		for (i = 0; i < N; i++) {
			int temp;
			fscanf(in, "%d", &temp);
			senator[i] = temp;
			sum += senator[i];
		}

		while (sum != 0) {
			char that[10] = { 0, }, temp = 0;
			max_i = 0;

			for (i = 1; i < N; i++) {
				if (senator[i] > senator[max_i]) max_i = i;
			}
			senator[max_i]--; sum--;
			temp = 'A' + max_i;
			that[0] = temp;

			max_i = 0;
			for (i = 1; i < N; i++) {
				if (senator[i] > senator[max_i])max_i = i;
			}
			senator[max_i]--; sum--;
			temp = 'A' + max_i;

			for (i = 0; i < N; i++) {
				if (((double)senator[i] / sum)>0.5) break;
			}

			if (i == N) {
				that[1] = temp;
			}
			else {
				senator[max_i]++; 
				sum++;
			}

			fprintf(out, "%s ", that);

		}

		fprintf(out, "\n");
	}

	return 0;
}