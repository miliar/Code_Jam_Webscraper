#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int D[101];
	int testnum;
	char pancake[101];
	FILE *f = fopen("B-large.in", "r");
	FILE *fp = fopen("out_B2.txt", "w");
	fscanf(f,"%d", &testnum);
	for (int t = 1; t <= testnum; t++) {
		fscanf(f,"%s", pancake);

		int panlen = strlen(pancake);
		if (pancake[0] == '+')
			D[0] = 0;
		else
			D[0] = 1;
		for (int i = 1; i < panlen; i++) {
			if (pancake[i-1] != pancake[i]) {
				if (pancake[i] == '-')
					D[i] = D[i - 1] + 2;
				else
					D[i] = D[i - 1];
			}
			else
				D[i] = D[i - 1];	
		}

		fprintf(fp,"Case #%d: %d\n", t, D[panlen-1]);
	}
}