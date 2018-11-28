#include <algorithm>
#include <cmath>
#include <cstdio>
#include <memory.h>

using namespace std;

int N;

bool Chk[1111];

double A[1111], B[1111];

int main(void)
{
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tt = 1; tt <= TC; tt++) {
		scanf("%d", &N);
		for (int i = 1; i <= N; i++) scanf("%lf", &A[i]);
		for (int i = 1; i <= N; i++) scanf("%lf", &B[i]);
		printf("Case #%d: ", tt);
		int Ans1 = 0;
		memset(Chk, false, sizeof (Chk));
		for (int i = 1; i <= N; i++) {
			double Min = 999999999.;
			int Minj = -1;
			for (int j = 1; j <= N; j++) {
				if (A[i] < B[j] && B[j] - A[i] < Min && !Chk[j]) {
					Min = B[j] - A[i];
					Minj = j;
				}
			}
			if (Minj == -1) {
				Min = 999999999.;
				Ans1++;
				for (int j = 1; j <= N; j++) {
					if (!Chk[j] && Min > B[j]) {
						Min = B[j];
						Minj = j;
					}
				}
				Chk[Minj] = true;
			} else {
				Chk[Minj] = true;
			}
		}
		memset(Chk, false, sizeof (Chk));
		stable_sort(B + 1, B + N + 1);
		int Ans2 = 0;
		for (int i = 1; i <= N; i++) {
			double Min = 999999999.;
			int Minj = -1;
			for (int j = 1; j <= N; j++) {
				if (!Chk[j] && A[j] > B[i] && Min > A[j]) {
					Min = A[j];
					Minj = j;
				}
			}
			if (Minj != -1) {
				Chk[Minj] = true;
				Ans2++;
			}
		}
		printf("%d %d\n", Ans2, Ans1);
	}

	return 0;
}
