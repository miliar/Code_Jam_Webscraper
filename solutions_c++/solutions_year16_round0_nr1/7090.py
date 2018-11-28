// Counting sheep

#include <cstdio>

void calc() {
	int in;
	int temp;
	int sum = 0;
	int checker[10] = {};
	int check = 0;
	int i;

	scanf("%d", &in);
	if (in == 0) {
		printf("INSOMNIA\n");
		return;
	}

	do {
		sum += in;
		temp = sum;
		while (temp > 0) {
			if (checker[temp % 10] == 0) {
				check++;
				checker[temp % 10] = 1;
			}
			temp /= 10;
		}
	} while(check != 10);

	printf("%d\n", sum);
}

int main() {
	int t, tc;

	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		printf("Case #%d: ", t);
		calc();
	}
	return 0;
}