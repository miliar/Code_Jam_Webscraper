#include <stdio.h>

int main() {
	int T, N, n, i, check[11], cnt, ans, x, j;

	FILE *fin = fopen("A-large.in","r");
	FILE *fout = fopen("out.txt","w");

	fscanf(fin,"%d", &T);
	for (j = 1;j <= T;j++) {
		fscanf(fin,"%d", &N);
		ans = 0;
		cnt = 0;
		for (i = 0;i < 10;i++)
			check[i] = 0;

		if (N == 0) {
			fprintf(fout,"Case #%d: INSOMNIA\n",j);
			continue;
		}
		while (cnt != 10) {
			cnt = 0;
			ans++;
			x = N*ans;
			n = x;
			while (n != 0) {
				check[n % 10] = 1;
				n = n / 10;
			}
			for (i = 0;i < 10;i++) {
				if (check[i] == 1)
					cnt++;
			}
		}
		fprintf(fout,"Case #%d: %d\n",j, x);

	}
	return 0;
}