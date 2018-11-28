#include <stdio.h>

char infile[] = "A-large.in";
char outfile[] = "out.txt";

int main() {
	FILE* fin = fopen(infile, "rb");

	if(!fin) {
		printf("file not found\n");
		return 0;
	}
		
	FILE* fout = fopen(outfile, "wb");

	int T, SM;
	fscanf(fin, "%d", &T);

	for(int i = 0; i < T; ++ i) {
		int DM = 0;
		int sum = 0;
		char c;

		fscanf(fin, "%d ", &SM);

		for(int s = 0; s <= SM; ++ s) {
			fscanf(fin, "%c", &c);

			if(s > sum) {
				DM += s - sum;
				sum += s - sum;
			}

			sum += c - '0';
		}

		fprintf(fout, "Case #%d: %d\n", i + 1, DM );
	}


	fcloseall();
	return 0;
}