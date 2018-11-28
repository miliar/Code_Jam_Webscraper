#include <cstdio>
#include <algorithm>
using namespace std;

int T, N;
double A[1005], B[1005];

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.in", "w", stdout);

	scanf("%d", &T);

	for (int no = 1; no <= T; no++) {
		printf("Case #%d:", no);
		scanf("%d", &N);
		for (int i = 0; i < N; i++) scanf("%lf", &A[i]);
		sort(A, A + N);
		for (int i = 0; i < N; i++) scanf("%lf", &B[i]);
		sort(B, B + N);
		int ptr1 = 0, ptr2 = 0, cnt1 = 0, cnt2 = 0;
		while (ptr1 < N && ptr2 < N) {
			if (A[ptr1] < B[ptr2]) {
				ptr1++; ptr2++;
			}
			else {
				ptr2++;
				cnt1++;
			}
		}
		ptr1 = ptr2 = N - 1;
		while(ptr1 >= 0 && ptr2 >= 0) {
			if (A[ptr1] > B[ptr2]) {
				ptr1--; ptr2--; cnt2++;
			}
			else {
				ptr2--;
			}
		}
		printf(" %d %d\n", cnt2, cnt1);
	}

	return 0;
}