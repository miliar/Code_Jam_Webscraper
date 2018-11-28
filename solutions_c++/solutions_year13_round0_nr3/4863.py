#include <stdio.h>
#include <math.h>

int checkPalindrome(int num);

int main() {

	int t, a, b, A, B;
	int i, j, count;
	;
	FILE *fin, *fout;

	fin = fopen("C-small-attempt0.in", "r");
	fout = fopen("C-small-attempt0.out", "w");

	fscanf(fin, "%d", &t);

	for (i = 1; i <= t; i++) {
		fscanf(fin, "%d %d", &A, &B);
		count = 0;
		a = ceil((double) sqrt((double) A));
		b = sqrt((double) B);
		for (j = a; j <= b; j++) {
			if (checkPalindrome(j)) {
				if (checkPalindrome(j * j)) {
					count++;
				}
			}
		}
		fprintf(fout, "Case #%d: %d\n", i, count);
	}
	return 0;
}

int checkPalindrome(int num) {
	int temp, revNum = 0;
	temp  = num;
	while (num > 0) {
		revNum = (revNum * 10) + (num % 10);
		num = num / 10;
	}
	if (temp == revNum) {
		return 1;
	}
	return 0;
}

