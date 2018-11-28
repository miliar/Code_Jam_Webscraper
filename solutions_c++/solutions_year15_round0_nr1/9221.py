#include <iostream>
#include <cstdlib>
#include <cstdio>

int main () {
	FILE *f = fopen("/tmp/AL.in", "r");
	FILE *fo = fopen("/tmp/Asre.out", "w");
	char line[3000];
	int tl, len;
	char nper[2000];
	fgets(line, 3000, f);
	sscanf(line, "%i", &tl);
	int i, k, c, n, g, fal;
	for(i = 1;i <= tl; i++){
		fgets(line,3000,f);
		sscanf(line, "%i %s", &len, nper);
		c = 0;
		n = 0;
		for(k = 0; k <= len; k++) {
			g = nper[k] - 48;
			if(g && k>c) {
				fal = k - c;
				n = n + fal;
				c = c + g + fal;
				continue;
			} 
			c = c + g;
		}
		fprintf(fo, "Case #%i: %i\n", i, n);
	}
	fclose(fo);
	return 0;
}
