#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, TC;
	scanf("%d", &T);
	TC = T;
	while (TC--) {
		int N;
		scanf("%d", &N);
		double naomi[1000], ken[1000];
		for (int i = 0; i < N; i++)
			scanf("%lf", naomi + i);
		for (int i = 0; i < N; i++)
			scanf("%lf", ken + i);
		sort(naomi, naomi + N);
		sort(ken, ken + N);

		printf("Case #%d: ", T - TC);
		if (naomi[0] > ken[N - 1])
			printf("%d ", N);
		else if (naomi[N - 1] < ken[0])
			printf("%d ", 0);
		else {
			double *pnhead = naomi, *pntail = naomi + N - 1, *pkhead = ken,
					*pktail = ken + N - 1;
			int ans = 0;
			for (int i = 0; i < N; i++) {
				if (*pnhead < *pkhead) {
					pnhead++;
					pktail--;
				} else {
					ans++;
					pnhead++;
					pkhead++;
				}
			}
			printf("%d ", ans);
		}

		{
			int ans = 0;
			double *pnhead = naomi, *pntail = naomi + N - 1, *pkhead = ken,
					*pktail = ken + N - 1;
			for (int i = 0; i < N; i++) {
				while (*pkhead < *pnhead)
					if (pkhead == pktail)
						break;
					else {
						pkhead++;
						ans++;
					}
				if (*pkhead > *pnhead) {
					pnhead++;
					if (pkhead == pktail)
						break;
					else
						pkhead++;
				}
			}
			printf("%d\n", pntail - pnhead + 1);
		}
	}
}
