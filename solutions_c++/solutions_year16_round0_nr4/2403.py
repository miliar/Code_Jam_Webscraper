#include <stdio.h>

int T, K, C, S;

// for small input
/**********************************************/
int main() {
	//FILE *fi = fopen("sample.in", "r");
	//FILE *fi = fopen("D-large.in", "r");
	FILE *fi = fopen("D-small-attempt0.in", "r");
	FILE *fo = fopen("output.txt", "w");

	int T;
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%d %d %d", &K, &C, &S);
		fprintf(fo, "Case #%d:", t);
		for (int i = 1; i <= S; i++) {
			fprintf(fo, " %d", i);
		}
		fprintf(fo, "\n");
	}
	fclose(fi);
	fclose(fo);
	return 0;
}
/***********************************************/

// for all input
/***********************************************
int main() {
	FILE *fi = fopen("sample.in", "r");
	//FILE *fi = fopen("D-large.in", "r");
	//FILE *fi = fopen("D-small-attempt0.in", "r");
	FILE *fo = fopen("output.txt", "w");

	int T;
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
	}
	fclose(fi);
	fclose(fo);
	return 0;
}
/************************************************/