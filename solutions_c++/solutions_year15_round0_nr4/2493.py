#include<stdio.h>
int main(){
	
	int t;
	FILE *in, *out;
	in = fopen("D-small-attempt3.in", "r");
	out = fopen("output.txt", "w");

	fscanf(in, "%d", &t);
	for (int z = 1; z <= t; z++){
		int x, r, c;
		fscanf(in, "%d %d %d", &x, &r, &c);
		
		if (x == 1){
			fprintf(out, "Case #%d: GABRIEL\n",z);
			continue;
		}
		if (x == 2){
			if ((r*c) % 2 == 0) fprintf(out, "Case #%d: GABRIEL\n", z);
			else fprintf(out, "Case #%d: RICHARD\n", z);
			continue;
		}
		if ((r*c) % x != 0){
			fprintf(out, "Case #%d: RICHARD\n", z);
			continue;
		}
		if (x == 3){
			if (r == 1 || c == 1){
				fprintf(out, "Case #%d: RICHARD\n", z);
			}
			else{
				fprintf(out, "Case #%d: GABRIEL\n", z);
			}
			continue;
		}
		if (x == 4){
			if (r*c<=8){
				fprintf(out, "Case #%d: RICHARD\n", z);
			}
			else{
				fprintf(out, "Case #%d: GABRIEL\n", z);
			}
			continue;
		}
	}

	fclose(in);
	fclose(out);

	return 0;
}