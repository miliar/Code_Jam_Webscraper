#include <iostream>
#include <cstdio>
using namespace std;
int T;
int Smax, S, res, sum;
int main() {
	FILE *f, *fo;
	f = fopen("A-large.in", "r");
	fo = fopen("output.txt", "w");
	fscanf(f, "%d", &T);
	for (int tcase = 1; tcase <= T; tcase++) {
		fscanf(f, "%d", &Smax);
		res = sum = 0;
		for (int k = 0; k <= Smax; k++) {
			fscanf(f, "%1d", &S);
			if (k != 0 && k > sum) {
				res += k - sum;
				sum += k - sum;
			}
			sum += S;
		}
		fprintf(fo, "Case #%d: %d\n", tcase, res);
	}
	fclose(fo);
	fclose(f);
	return 0;
}