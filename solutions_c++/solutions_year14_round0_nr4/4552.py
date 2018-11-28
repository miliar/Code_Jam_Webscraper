#include <stdio.h>
#include <algorithm>

#define MAX 1001

using namespace std;

int main(void)
{
	int T, N;
	int x = 0, y, z;
	double naomi[MAX], ken[MAX];

	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &T);
	x = 0;
	while (x < T) {
		int i, j;
		int naomi_lose;
		scanf("%d", &N);
        for (i = 0; i < N; i++)
			scanf("%lf", &naomi[i]);
		naomi[i] = '\0';

		for (i = 0; i < N; i++)
			scanf("%lf", &ken[i]);
		ken[i] = '\0';

        sort(naomi, naomi+N);
		sort(ken, ken+N);

        i = 0;
        j = 0;
        while (i < N && j < N) {
            while (naomi[i] > ken[j]) {
                i++;
                j++;
                if (i == N)
                    break;
            }
            i++;
            if (i == N)
                break;
        }
        y = j;

        i = 0;
        j = 0;
        while (i < N && j < N) {
            while (naomi[i] < ken[j]) {
                i++;
                j++;
                if (j == N)
                    break;
            }
            j++;
            if (j == N)
                break;
        }
        z = N - i;

		x++;
		printf("Case #%d: %d %d\n", x, y, z);
	}
	return 0;
}
