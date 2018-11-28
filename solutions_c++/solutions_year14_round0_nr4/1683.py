#include <cstdio>
#include <cstdlib>
#include <ctime>
using namespace std;
#define MAXN 1000
int N;
double A[MAXN], B[MAXN];
void qs(double* arr, int l, int r) {
	int t = rand() % (r-l+1) + l;
	double x = arr[t];
	arr[t] = arr[l];
	int i = l, j = r;
	while (i < j) {
		while (i < j && x <= arr[j]) j--;
		if (i < j) arr[i++] = arr[j];
		while (i < j && arr[i] <= x) i++;
		if (i < j) arr[j--] = arr[i];
	}
	arr[i] = x;
	if (l < i-1) qs(arr, l, i-1);
	if (i+1 < r) qs(arr, i+1, r);
}
int main() {
	srand(time(0));
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%lf", &A[i]);
		for (int i = 0; i < N; i++)
			scanf("%lf", &B[i]);
		qs(A, 0, N-1);
		qs(B, 0, N-1);
		int ans0 = 0, ans1 = 0;
		int ah = 0, at = N-1, bh = 0, bt = N-1;
		while (ah <= at) {
			if (A[ah] < B[bh]) {
				ah++;
				bt--;
			} else {
				ah++;
				bh++;
				ans0++;
			}
		}
		ah = bh = 0;
		at = bt = N-1;
		while (ah <= at) {
			if (A[at] > B[bt]) {
				at--;
				bh++;
				ans1++;
			} else {
				at--;
				bt--;
			}
		}
		printf("Case #%d: %d %d\n", t, ans0, ans1);
	}
	return 0;
}

