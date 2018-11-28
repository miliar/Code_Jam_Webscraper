#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int N;
		scanf("%d", &N);
		double p1[1050], p2[1050];
		for (int i = 0; i < N; i++) scanf("%lf", &p1[i]);
		for (int i = 0; i < N; i++) scanf("%lf", &p2[i]);

		sort(p1, p1+N);
		sort(p2, p2+N);

		//for (int i = 0; i < N; i++) printf("%lf ", p1[i]);
		//puts("");
		//for (int i = 0; i < N; i++) printf("%lf ", p2[i]);

		//puts("");

		int l1 = 0, r1 = N-1, l2 = 0, r2 = N - 1;
		int c1 = 0, c2 = 0;
		for (int num = 0; num < N; num++) {
			if (p1[l1] < p2[l2]) {
				l1++;
				r2--;
			}
			else {
				l1++;
				l2++;
				c1++;
			}
		}
		l1 = l2 = 0;
		r1 = r2 = N-1;
		bool removed2[1050];
		for (int i = 0; i < N; i++) removed2[i] = false;
		for (int i = 0; i < N; i++) {
			if (p1[i] > p2[r2]) {
				removed2[l2] = true;
				l2++;
				c2++;

			}
			else {
				int find = -100;
				for (int j = 0; j <= r2; j++) if (p2[j] > p1[i] && !removed2[j]) {
					find = j;
					removed2[j] = true;
					break;
				}
				if (find == r2) r2--;
				else if (find == -100) c2++;
			}
		}
		printf("Case #%d: %d %d\n", t+1, c1, c2);
	}
}
