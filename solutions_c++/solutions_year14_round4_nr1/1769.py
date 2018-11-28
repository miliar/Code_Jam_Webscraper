#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int N, X;
int S[10005];
bool mark[10005];

int cmp(const void *a, const void *b)
{
	const int *pa = (const int *)a;
	const int *pb = (const int *)b;
	return *pa - *pb;
}

int calc()
{
	qsort(S, N, sizeof (int), cmp);
	int ret = 0;
	int head = 0, tail = N - 1;
	for (;;) {
		if (head == tail) {
			ret++;
			break;
		}
		else if (head > tail) {
			break;
		}
		int a = S[head];
		int b = S[tail];
		if (a + b <= X) {
			head++;
			tail--;
			ret++;
		}
		else {
			tail--;
			ret++;
		}
	}
	return ret;
}

int main()
{
	int cs, k;
	scanf("%d", &cs);
	for (k = 0; k < cs; k++) {
		scanf("%d%d", &N, &X);
		int i;
		for (i = 0; i < N; i++) {
			scanf("%d", &S[i]);
		}
		printf("Case #%d: %d\n", k + 1, calc());
	}
	return 0;
}