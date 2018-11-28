#include <stdio.h>
#include <math.h>
#include <string.h>

bool isFair(long n)
{
	char str[128];

	sprintf(str, "%ld", n);

	int l=0, r = strlen(str)-1;

	while(l < r) {
		if (str[l++] != str[r--]) return false; 
	}

	return true;
}

bool isSquare(int n)
{
	long ln = n;
	long sn = sqrt(ln);

	if ((int)(sn*sn) == n && isFair(sn)) {
		return true;
	}

	return false;
}

int main()
{
	int t;

	scanf("%d", &t);

	for(int i = 1; i <= t; i++) {
		int from, to;
		int count = 0;

		scanf("%d %d", &from, &to);

		for(int j=from; j<=to; j++) {
			if (isFair(j) && isSquare(j)) {
				count++;
			}
		}

		printf("Case #%d: %d\n", i, count);
	}

	return 0;
}

