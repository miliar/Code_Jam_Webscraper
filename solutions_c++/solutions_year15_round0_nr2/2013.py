#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fp, *fw;

int main() {
	//fp = fopen("D:\\GCJ\\in.txt", "r");
	fp = fopen("D:\\GCJ\\B-large.in", "r");
	fw = fopen("D:\\GCJ\\outBL.txt", "w");
	int cse, i, g = 1, n, tp, res, maxtp, maxa, a[1010], j, cnt;
	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d", &n);
		maxa = 0;
		res = 0;
		for(i = 0; i < n; ++i) {
			fscanf(fp, "%d", &a[i]);
			if(a[i] > maxa) {
				maxa = a[i];
			}
		}
		res = 1000000;
		for(i = 2; i <= maxa; ++i) {
			cnt = 0;
			for(j = 0; j < n; ++j) {
				if(a[j] > i) {
					cnt += a[j] / i - 1;
					if(a[j] % i != 0) cnt++;
				}
			}
			cnt += i;
			if(cnt < res) res = cnt;
		}
		if(res == 1000000) res = maxa;
		fprintf(fw, "Case #%d: %d\n", g++, res);
	}
	fclose(fp);
	fclose(fw);
	return 0;
}
