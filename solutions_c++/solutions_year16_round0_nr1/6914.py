#include <stdio.h>
int digit[10];
int main(void) {
	FILE *f;
	f=fopen("pa.txt", "w+");
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		for (int j = 0; j < 10; j++)
			digit[j] = 0;
		unsigned long long n;
		scanf("%llu", &n);
		if (n == 0) {
			fprintf(f,"Case #%d: INSOMNIA\n", i);
			continue;
		}
		int check = 0;
		int cnt = 0;
		while (check!=10) {
			cnt++;
			unsigned long long temp = n*cnt;
			int temp1;
			do {
				temp1 = temp % 10;
				if (digit[temp1] == 0) {
					digit[temp1] = 1;
					check++;
				}
				temp = temp / 10;
			} while (temp!= 0);
		}
		fprintf(f,"Case #%d: %llu\n",i,n*cnt);
	}
	fclose(f);
	return 0;
}
