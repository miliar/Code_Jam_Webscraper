#define _CRT_SECURE_NO_WARNINGS 1

#include "stdio.h"
#include "stdio.h"

int main(int argc, char **argv) {
	
	//FILE *f = fopen("sample.in", "r");
	//FILE *g = fopen("sample.out", "w");
	//FILE *f = fopen("A-small-attempt0.in", "r");
	//FILE *g = fopen("A-small-attempt0.out", "w");
	FILE *f = fopen("A-large.in", "r");
	FILE *g = fopen("A-large.out", "w");
	
	int t;

	fscanf(f, "%d\n", &t);
	printf("NoLine:%d\n", t);
	for(int line = 0; line < t; line++) {
		int invited = 0;
		int standing = 0;

		int max;
		fscanf(f, "%d ", &max);
		printf("Line:%d Length:%d\n", line, max);
		for(int i = 0; i <= max; i++) {
			int v = 0;
			fscanf(f, "%c", &v);
			v -= '0';
			printf("Line:%d Length:%d Index:%d Value:%d\n", line, max, i, v);
			if(v > 0 && i - standing > 0) {
				invited += (i - standing);
				standing += v + (i - standing);
			} else {
				standing += v;
			}
			printf("Invited:%d Standing:%d\n", invited, standing);
		}
		printf("Invited:%d\n", invited);
		fprintf(g, "Case #%d: %d\n", (line + 1), invited);

		fscanf(f, "\n");
	}
	fclose(f);
	fclose(g);
	return 0;
}