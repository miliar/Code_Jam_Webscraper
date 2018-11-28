#include <stdio.h>
#include <stdlib.h>

int intpal(int num) {
	char tomb[100];
	snprintf(tomb, sizeof(tomb), "%d", num);

	int pale = 1;
	int i, hossz;
	for (hossz = 0; tomb[hossz]!= 0; hossz++);
	for (i=0; i < hossz/2; i++){
		if (tomb[i] != tomb[hossz-i-1]) {
			pale=0;
			break;
		}
	}
	return pale;
}

int squareAndFair(int a, int b) {
	int i, db = 0;
	for (i=0; i*i <= b; i++) {
		if (a <= i*i) {
			if (intpal(i) != 1) continue;
			int negyzet = i * i;
			if (intpal(negyzet) == 1) {
				db++;
			}
		}
	}
	return db;
}

int main()
{		
	FILE *in;
	FILE *out;

	in = fopen("C-small-attempt0.in", "r");
	out = fopen("output.txt", "w");

	int testCases;
	fscanf(in, "%d\n", &testCases);

	for (int t = 0; t < testCases; t++){
		int a, b;
		fscanf(in, "%d %d\n", &a, &b);
		fprintf(out, "Case #%d: %d\n", t + 1, squareAndFair(a, b));
	}

	fclose(in);
	fclose(out);
	return 0;
}	
