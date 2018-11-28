#include<stdio.h>
#define decimal 10
#define maxTSize 100

int T;
int N;
int total;
int input[decimal];
int result[maxTSize];

int isAllSelected();
void checkInput(int remainder);

int main() {
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);

		if (N == 0) {
			result[tc] = 0;
		}
		else {
			for (int i = 0; i < decimal; i++) {
				input[i] = 0;
			}

			total = 0;

			while (!isAllSelected()) {
				total += N;

				int current = total;
				int remainder = 0;

				while (true) {
					if (current < 10) {
						checkInput(current);
						break;
					}
					else {
						remainder = current % 10;
						current /= 10;

						checkInput(remainder);
					}
				}

				/*
				for (int i = 0; i < decimal; i++) {
					printf("%d ", input[i]);
				}
				printf("\n");
				*/
			}

			result[tc] = total;
		}
	}

	for (int tc = 0; tc < T; tc++) {
		if (result[tc] == 0) {
			printf("Case #%d: INSOMNIA\n", (tc+1));
		}
		else {
			printf("Case #%d: %d\n", (tc+1), result[tc]);
		}
	}
}

int isAllSelected() {
	bool allChecked = true;

	for (int i = 0; i < decimal; i++) {
		if (input[i] == 0) {
			allChecked = false;
			break;
		}
	}

	return allChecked;
}

void checkInput(int remainder) {
	input[remainder] = 1;
}