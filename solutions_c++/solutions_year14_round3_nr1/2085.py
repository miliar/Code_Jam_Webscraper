#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		char str[10], delimeter[2];
		char *temp;
		int num1, num2;
		double num;
		delimeter[0] = '/';
		delimeter[1] = NULL;
		scanf("%s", &str);
		temp = strtok(str, delimeter);
		num1 = atoi(temp);
		temp = strtok(NULL, delimeter);
		num2 = atoi(temp);

		if (num2 % 2 != 0) {
			printf("Case #%d: impossible\n", i);
			continue;
		}

	//	num = (double)num1 / (double)num2;
		
		int j = 0;
		for (j = 0; j <= 40; j++) {
			if (num2 > 1 && num2 % 2 != 0) {
				j = 41;
				break;
			}

			if (num1 >= num2){//num >= 1.0) {
				int re = num1 - num2;
				int k = 0;
				for (k = 0; k < 40; k++) {
					int remain = re%num2;
					if (remain == 0) {
						break;
					}

					re = remain * 10;
				}
				if (k < 40)
					printf("Case #%d: %d\n", i, j);
				else
					j = 41;
				break;
			}
			num2 /= 2;
			//num *= 2.0;
		}

		if (j == 41) {
			printf("Case #%d: impossible\n", i);
		}
	}
	return 0;
}