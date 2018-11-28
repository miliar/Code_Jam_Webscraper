#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int n;
	scanf("%d", &n);

	for(int i = 0; i < n; i++) {
		int start, end;
		scanf("%d %d", &start, &end);

		int count = 0;
		for(long int j = start; j <= end; j++) {
			long double num = j;
			long double result = sqrt(num);
			long int convert = (long int)result;

			if(convert * convert == j) {
				char str[16], str2[16];
				itoa(j, str, 10);
				itoa(convert, str2, 10);
				int len = strlen(str);
				int len2 = strlen(str2);
				int pivot = len / 2;
				int pivot2 = len2 / 2;

				int k = 0;
				for(k = 0; k < pivot; k++) {
					if(str[k] != str[len-k-1]) {
						break;
					}
				}

				if(k == pivot) {
					for(k = 0; k < pivot2; k++) {
						if(str2[k] != str2[len2-k-1]) {
							break;
						}
					}

					if(k == pivot2) {
						count++;
					}
				}
			}
		}

		printf("Case #%d: %d\n", (i+1), count);
	}

	return 0;
}