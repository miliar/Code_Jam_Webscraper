#include<stdio.h>

int main() {

	int t, n, i, j, k, l, cnt, temp, result;
	int chk[10], digits[30], original, original_len = 0;
	FILE *in, *ou;
	fopen_s(&in, "input.txt", "r");
	fopen_s(&ou, "output.txt", "w");
	fscanf_s(in, "%d", &t);
	for (i = 0; i < t; i++) {
		for (j = 0; j < 10; j++)
			chk[j] = 0;
		cnt = 0;
		fscanf_s(in, "%d", &n);
		if (n == 0) {
			fprintf(ou, "Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		original = n;
		result = 0;
		for (j = 0; j < 10000; j++) {
			result += original;
			temp = result;
			while (temp != 0) {
				if (chk[temp % 10] == 0) {
					chk[temp % 10] = 1;
					cnt++;
				}
				temp /= 10;
			}
			if (cnt == 10)
				break;
		}
		fprintf(ou, "Case #%d: %d\n", i + 1, result);

	}
	return 1;
}