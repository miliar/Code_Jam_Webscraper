#include<stdlib.h>
#include<stdio.h>
#include<string.h>



double calc(int A, int B, int K) {
	int z = 0;
	printf("%i %i %i\n", A, B, K);
	for(int i = 0; i < A; i++) {
		for (int j = 0; j < B; j++) {
			
			if ((i&j) < K) {
				z++;
			}
			 
		}
	}
	return z;
		
}
int main() {

	FILE *fin;
	FILE *fout;
	fin = fopen("./small.in", "r");
	fout = fopen("./Output_Cookie.txt", "w");

	char line[1024];
	double cost;
	double rate;
	double goal;
	char *stopstring;
	double seconds;
	int linecount = 0;
	while(fgets(line, 1024, fin)) {
		if (linecount != 0) {
			char *tempdata = strdup(line);
			cost = strtod(line, &stopstring);
			rate = strtod(stopstring, &stopstring);
			goal = strtod(stopstring, &stopstring);
			seconds = calc(cost, rate, goal);	
			printf("%.7lf\n", seconds);
			fprintf(fout, "Case #%i: %i\n", linecount,  (int)seconds);
		}
		linecount++;
	}
}		
