#include <iostream>
#include <stdio.h>


#define MAX 1010

int main() {
	char *input = "input.txt";
	char *output = "output.txt";
	FILE *f_in = fopen(input, "r");
	FILE *f_out = fopen(output, "w");

	int TC = 0;
	fscanf(f_in, "%d", &TC);
	for(int k = 1; k <= TC; k++) {
		int max = 0, stand = 0, result = 0, i = 0;
		char s[MAX];
		fscanf(f_in, "%d", &max);
		fscanf(f_in, "%s", s);

		while (1) {
			for (; i <= max && i <= stand; i++) {
				stand += s[i] - '0';
			}
			if (i > max) break;
			result++;
			stand++;
		}
		fprintf(f_out, "Case #%d: %d\n", k, result);
	}

	
	fclose(f_in);
	fclose(f_out);
	return 0;
}
