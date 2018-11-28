#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[4000005];
int main(void) {
	FILE* fi = fopen("c:\\input.txt", "rt");
	FILE* fout = fopen("c:\\output.txt", "wt");
	int n; fscanf(fi, "%d", &n);
	
	for (int i = 0; i < n; i++) {
		int m; fscanf(fi, "%d", &m);
		int max = 0; int print_min;
		for (int j = 0; j < m; j++) {
			fscanf(fi, "%d", &arr[j]);
			if (max < arr[j]) max = arr[j];
		}

		print_min = max;
		for (int j = 1; j <= max; j++) {
			int sum = j;
			for (int k = 0; k < m; k++) {
				sum += (arr[k] - 1) / j;
			}

			if (sum < print_min) print_min = sum;
		}
		
		fprintf(fout, "Case #%d: %d\n", i + 1, print_min);
	}
}