#include<stdio.h>
#include<math.h>

int main() {
	FILE* ifp = fopen("input.txt", "r");
	FILE* ofp = fopen("output.txt", "w");

	int cases, cn = 0;
	int r, t, n;
	fscanf(ifp, "%d", &cases);

	while(cases--) {
		cn++;

		fscanf(ifp, "%d %d", &r, &t);
		n = floor(sqrt((2.*r-1)*(2.*r-1)+8.*t)) + 1 - 2*r;
		n /= 4;

		fprintf(ofp, "Case #%d: %d\n", cn, n);
	}

	fclose(ifp);
	fclose(ofp);
	return 0;
}