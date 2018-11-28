#include <stdio.h>

const int MAX_N = 1000000;

inline int get_bit(int num) {
	int res = 0;
	for (int t = num; t; t /= 10) {
		res |= 1 << (t % 10);
	}
	return res;
}

int main() {
	int T, t, i;

	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &T);

	for (t = 1; t <= T; t++) {
		fscanf(fin, "%d", &i);

		int res = 0, nn, cnt = 0, num = i, te = 0;
		while (true) {
			nn = get_bit(num);
			res |= nn;
			cnt++;

			if (res == (1 << 10) - 1) {
				break;
			}

			if (cnt % 100 == 0) {
				if (te == res) {
					cnt = -1;
					break;
				}
				te = res;
			}

			num += i;
		}

		fprintf(fout, "Case #%d: ", t);
		if (cnt == -1)
			fprintf(fout, "INSOMNIA\n");
		else
			fprintf(fout, "%d\n", num);
	}


	return 0;
}