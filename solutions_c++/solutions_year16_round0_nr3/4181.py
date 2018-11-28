#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <cmath>

int check(long long num) {
	for (long long i = 3; i*i <= num; i++) {
		if (num % i == 0)
			return i;
	}
	return 0;
}

int main(void) {
	int roop;
	scanf("%d", &roop);
	FILE * fp = fopen("output.txt", "w");

	for (int i = 1; i <= roop; i++) {
		int n, m;
		scanf("%d %d", &n, &m);
		int maxNum = m;
		int min = (1 << (n - 1)) + 1;
		int max = (1 << n) - 1;

		bool binary[17] = { 0, };
		int result[9] = { 0, };

		for (int k = min; k <= max; k+=2) {
			int x = k;
			int pos = 0;
			while (x >= 1) {
				binary[pos] = x % 2;
				x /= 2;
				pos++;
			}

			bool isJam = false;
			for (int bin = 2; bin <= 10; bin++) {
				long long num = 0;
				for (int a = n - 1; a >= 0; a--) {
					if (binary[a]) {
						num += (long long)pow(bin, a);
					}
				}
				int chk = check(num);
				if (chk == 0 || chk == 2) {
					isJam = false;
					break;
				}
				else {
					isJam = true;
					result[bin - 2] = chk;
				}
			}
			if (isJam && m > 0) {
				if (m == maxNum)
					fprintf(fp, "Case #%d:\n", roop);
				for (int a = n - 1; a >= 0; a--) {
					fprintf(fp, "%d", binary[a]);
				}
				fprintf(fp, " ");
				for (int l = 0; l < 9; l++) {
					fprintf(fp, "%d ", result[l]);
				}
				//printf("%d\n", m);
				fprintf(fp, "\n");
				m--;
			}
			if (m <= 0)
				break;
			isJam = false;
		}
	}

	return 0;
}