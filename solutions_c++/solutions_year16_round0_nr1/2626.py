#include <iostream>
#include <stdio.h>


using namespace std;

int cal(int k) {
	int flag = 0;
	int kk = 0;
	int kkk;
	while (flag != 0x3ff) {
		kk = kk + k;
		kkk = kk;
		while (kkk>0) {
			flag |= 1 << (kkk % 10);
			kkk /= 10;
		}
	}
	return kk;
}

int main() {
	FILE *fpi;
	FILE *fpo;
	int n;
	int i = 1;
	fpi = fopen("input.txt", "r");
	fscanf(fpi, "%d", &n);
	fpo = fopen("output.txt", "w");
	while (n--) {
		int k;
		fscanf(fpi, "%d", &k);
		if (k>0) {
			k = cal(k);
			fprintf(fpo, "Case #%d: %d\n", i++, k);
		}
		else {
			fprintf(fpo, "Case #%d: INSOMNIA\n", i++);
		}
	}
	fclose(fpi);
	fclose(fpo);
	return 0;
}

