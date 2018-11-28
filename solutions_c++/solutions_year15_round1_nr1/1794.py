#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fp, *fw;

int imin(int a, int b) {
	return a < b ? a : b;
}

int main() {
	fp = fopen("H:\\GCJ\\A-large.in", "r");
	fw = fopen("H:\\GCJ\\outAl.txt", "wt");
	int cse, i, n, a[1010], delta, res1, res2, g = 1;
	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d", &n);
		delta = 0;
		for(i = 0; i < n; ++i) {
			fscanf(fp, "%d", &a[i]);
			if(i) {
				if(a[i - 1] - a[i] > delta) delta = a[i - 1] - a[i];
			}
		}
		//printf("delta=%d\n", delta);
		res1 = res2 = 0;
		for(i = 0; i < n; ++i) {
			if(i && a[i] - a[i - 1] < 0) {
				res1 += a[i - 1] - a[i];
			}
			if(i < n - 1) res2 += imin(a[i], delta);
		}
		fprintf(fw, "Case #%d: %d %d\n", g++, res1, res2);
	}
	fclose(fp);
	fclose(fw);
	system("PAUSE");
	return 0;
}
