#include<stdio.h>

#pragma warning(disable:4996)
int main()
{
	FILE *fi = fopen("input.txt", "r");
	FILE *fo = fopen("output.txt", "w");
	int t,p,x,r,c;
	
	fscanf(fi,"%d", &t);
	for (p = 1; p <= t; p++){
		fscanf(fi, "%d %d %d", &x, &r, &c);

		if ((r < x && c < x) || (r*c) % x != 0 || x >= 7){
			fprintf(fo,"Case #%d: RICHARD\n", p);
			continue;
		}
		if (x == 1){
			fprintf(fo, "Case #%d: GABRIEL\n", p);
			continue;
		}
		if (x == 2){
			fprintf(fo, "Case #%d: GABRIEL\n", p);
			continue;
		}
		if (x == 3){
			if (r >= 2 && c >= 2){
				fprintf(fo, "Case #%d: GABRIEL\n", p);
				continue;
			}
			else {
				fprintf(fo, "Case #%d: RICHARD\n", p);
				continue;
			}
		}
		if (x == 4){
			if (r>=3 && c >=3){
				fprintf(fo, "Case #%d: GABRIEL\n", p);
				continue;
			}
			else {
				fprintf(fo, "Case #%d: RICHARD\n", p);
				continue;
			}
		}
		if (x == 5){
			if (r >= 4 && c >= 4){
				fprintf(fo, "Case #%d: GABRIEL\n", p);
				continue;
			}
			else {
				fprintf(fo, "Case #%d: RICHARD\n", p);
				continue;
			}
		}
		if (x == 6){
			if (r >= 5 && c >= 5){
				fprintf(fo, "Case #%d: GABRIEL\n", p);
				continue;
			}
			else {
				fprintf(fo, "Case #%d: RICHARD\n", p);
				continue;
			}
		}
	}
	return 0;
}