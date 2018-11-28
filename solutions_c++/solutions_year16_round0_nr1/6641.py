#include <stdio.h>
#include <string.h>

int check[10];
int cnt;
int main(void) {
	int n,i = 0,j;
	int a, b;
	int t;
	FILE *fp;
	fopen_s(&fp, "A-large.in", "rt");
	FILE *fpp;
	fopen_s(&fpp,"output", "w+");
	fscanf_s(fp,"%d", &t);
	for (int j = 1; j <= t; j++) {
		fscanf_s(fp,"%d", &n);
		if (n == 0) {
			fprintf(fpp,"Case #%d: INSOMNIA\n", j);
			continue;
		}
		i = 0;
		cnt = 0;
		memset(check, 0, sizeof(check));
		while (1) {
			i++;
			b = n * i;
			while (b != 0) {
				a = b % 10;
				b = b / 10;
				if (check[a] == 0) {
					check[a] = 1;
					cnt++;
				}
				if (cnt == 10)
					break;
			}
			if (cnt == 10)
				break;
		}
		fprintf(fpp,"Case #%d: %d\n", j, n * i);
	}
	return 0;
}