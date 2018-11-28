#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

bool IsPalindrome(long long number)
{
	int i = 0, l;
	char str[18];
	itoa(number, str , 10);
	l = strlen(str);
	while (i <= l/2) {
		if (str[i] != str[l - 1 - i])
			return false;
		i++;
	}

	return true;
}

int main()
{
	int i, T, result = 0;
	long long first, last, k;
	long long A, B;
	FILE *ffile1, *ffile2;

	ffile1 = fopen("C-small-attempt0.in", "r");
	ffile2 = fopen("C-small-attempt0.out", "w");

	fscanf(ffile1, "%d", &T);
	for (i = 1; i <= T; i++) {
		result = 0;
		fscanf(ffile1, "%lld%lld", &A, &B);
		first = ceil(sqrt(A - 0.000000001));
		last = floor(sqrt(B + 0.000000001));
		
		for (k = first; k <= last; k++) {
			if (IsPalindrome(k) && (k*k <= B))
				if (IsPalindrome(k*k))
					result++;
		}
		fprintf(ffile2, "Case #%d: ", i);
		fprintf(ffile2, "%d\n", result);
	}
	fclose(ffile1);
	fclose(ffile2);
	return 0;
}

