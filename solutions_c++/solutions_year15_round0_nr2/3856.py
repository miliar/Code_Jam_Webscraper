#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
using namespace std;

int T;
int count;
int num[10];
int D, P;
int res;

int getMax(int m, int* a) {
	int Max = 0;
	for (int i = m; i > 0; i--) {
		if (a[i] > 0) {
			Max = i;
			break;
		}
	}
	return Max;
}

void dfs(int m, int* a, int add) {
	if (m == 0)
		return;
	int A[10];
	int B[10];
	memset(A, 0, sizeof(int)* 10);
	memset(B, 0, sizeof(int)* 10);
	for (int i = 1; i <= m; i++) {
		A[i] = a[i];
	}
	for (int i = 1; i <= m - 1; i++) {
		B[i] = a[i + 1];
	}
	int temp;
	for (int i = 1; i <= m / 2; i++) {
		for (int j = 1; j <= m; j++) {
			A[j] = a[j];
		}
		A[i] += A[m];
		A[m - i] += A[m];
		temp = add + A[m] + getMax(m - 1, A);
		if (temp < res)
			res = temp;
		dfs(getMax(m - 1, A), A, add + A[m]);
	}
	temp = add + 1 + m - 1;
	if (temp < res)
		res = temp;
	dfs(m - 1, B, add + 1);
}

int main() {
	freopen("C:\\Users\\wzh22014\\Downloads\\B-small-attempt2.in", "r", stdin);
	freopen("B.out", "w", stdout);
	count = 0;
	scanf("%d", &T);
	while (T--) {
		count++;
		memset(num, 0, sizeof(int)* 10);
		scanf("%d", &D);
		for (int i = 0; i < D; i++) {
			scanf("%d", &P);
			num[P]++;
		}
		res = getMax(9, num);
		dfs(res, num, 0);
		printf("Case #%d: %d\n", count, res);
	}
}