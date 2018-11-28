#pragma warning(disable:4996)
#include <stdio.h>
#include <math.h>

int bit[33];
int ans_arr[11];
int count;
long long num;
int n, j;
FILE *wfp;

long long toi(int index, int base);
int find(long long num);
void bit_make(int l, int r);

int main() {
	int ts;
	

	wfp = fopen("output.txt", "w");

#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif

	scanf("%d", &ts);

	for (int t = 1; t <= ts; t++) {
		fprintf(wfp, "Case #%d:\n", t);
		count = 0;
		
		scanf("%d %d", &n, &j);

		for (int i = 2; i <= 9; i++)
			ans_arr[i] = 0;

		bit[0] = 1;
		bit[n - 1] = 1;

		for (int i = 1; i <= n - 2; i++)
			bit[i] = 0;

		bit_make(1, n - 2);
	}

	fclose(wfp);

	return 0;
}

long long toi(int index, int base) {
	long long tmp = 0;
	long long k = 1;

	for (int i = 0; i < index; i++) {
		tmp += bit[i] * k;
		k *= base;
	}

	return tmp;
}

int find(long long num) {
	int size;

	if (num > 100000000) {
		if (num < 1000000000)
			size = 32000;
		else if (num < 10000000000)
			size = 100000;
		else if (num < 100000000000)
			size = 320000;
		else if (num < 1000000000000)
			size = 1000000;
		else if (num < 10000000000000)
			size = 3200000;
		else if (num < 100000000000000)
			size = 10000000;
		else if (num < 1000000000000000)
			size = 32000000;
		else
			size = 100000000;
	}
	else
		size = sqrt((double)num);

	if (size == 1)
		return 1;

	if (num % 2 == 0)
		return 2;

	for (int i = 3; i <= size; i += 2)
		if (num % i == 0)
			return i;

	return 1;
}

void bit_make(int l, int r) {
	if (count >= j)
		return;

	int i;

	if (l == r) {
		bit[l] = 0;
		if (count >= j)
			return;

		for (i = 2; i <= 10; i++) {
			num = toi(n, i);
			ans_arr[i] = find(num);
			if (ans_arr[i] == 1)
				break;
		}
		
		if (i == 11) {
			count++;
			for (int i = n - 1; i >= 0; i--)
				fprintf(wfp, "%d", bit[i]);

			for (i = 2; i <= 10; i++)
				fprintf(wfp, " %d", ans_arr[i]);
			fprintf(wfp, "\n");
		}

		if (count >= j)
			return;

		bit[l] = 1;

		for (i = 2; i <= 10; i++) {
			num = toi(n, i);
			ans_arr[i] = find(num);
			if (ans_arr[i] == 1)
				break;
		}

		if (i == 11) {
			count++;
			for (int i = n - 1; i >= 0; i--)
				fprintf(wfp, "%d", bit[i]);

			for (i = 2; i <= 10; i++)
				fprintf(wfp, " %d", ans_arr[i]);
			fprintf(wfp, "\n");
		}
	}
	else {
		bit[r] = 0;
		bit_make(l, r - 1);
		bit[r] = 1;
		bit_make(l, r - 1);
	}

}