#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE *fi = fopen("A-small-attempt1.in.txt", "r");
	FILE *fo = fopen("output.txt", "w");
	int T;
	fscanf(fi,"%d", &T);
	for (int t = 0; t < T; t++){
		int r, c, w;

		fscanf(fi,"%d %d %d", &r, &c, &w);
		int check = c / w;
		if (c%w != 0)
			check++;
		check *= r;
		check += (w - 1);
		fprintf(fo,"Case #%d: %d\n", t + 1, check);
	}
	return 0;
}