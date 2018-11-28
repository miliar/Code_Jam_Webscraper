#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main(void) {
	FILE* fi = fopen("c:\\input.txt", "rt");
	FILE* fout = fopen("c:\\output.txt", "wt");
	int n; fscanf(fi, "%d", &n);

	for (int i = 0; i < n; i++) {
		int len; fscanf(fi, "%d", &len);
		char str[1005]; int arr[1005];
		fscanf(fi, "%s", str);

		for (int j = 0; j <= len; j++) {
			arr[j] = str[j] - '0';
		}
		int sum = 0; int cnt = 0;
		for (int j = 0; j <= len; j++) {
			if (sum < j) {
				cnt += j - sum;
				sum += j-sum;
			}
			sum += arr[j];
		}
		fprintf(fout, "Case #%d: %d\n", i+1, cnt);
	}

	return 0;
}