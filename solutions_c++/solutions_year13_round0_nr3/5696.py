#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int testcase, caseno;
int m[100];
int s[200];

int check(int n) {
	int count = 0, i = 0, j;
	while (n) {
		s[count++] = n % 10;
		n /= 10;
	}
	j = count - 1;
	while (i < j) {
		if (s[i] != s[j]) break;
		i++, j--;
	}
	if (i < j) return 0;
	return 1;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("E:\\C-small-attempt0.in", "r", stdin);
	freopen("E:\\test.out", "w", stdout);
#endif

	int i, j;
	int A, B, num;
	int count;
	scanf("%d", &testcase);
	for (caseno = 1; caseno <= testcase; ++caseno) {
		count = 0;
		scanf("%d%d", &A, &B);
		num = sqrt((double)A) - 1;
		while (num * num < A) num += 1;
		for (; num * num <= B; ++num) {
			if (check(num) && check(num * num)) {
				//printf("	%d	%d\n", num, num*num);
				count++;
			}
		}
		printf("Case #%d: %d\n", caseno, count);
	}
	return 0;
}