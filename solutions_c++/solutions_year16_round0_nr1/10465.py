#include <cstdio>
#include <vector>
#include <climits>

#define MAXN 1010
char buff[MAXN];

using namespace std;

int main() {
	int N;
	scanf("%d", &N);

	for (int ni = 0; ni < N; ++ni) {
		printf("Case #%d: ", ni+1);

		int a;
		scanf("%d", &a);
		vector<int> occ(10, 0);
		int remain = 10;

		if (a == 0) {
			printf("INSOMNIA\n");
			continue;
		}

		long long j;
		for (j = 0; j < LLONG_MAX / a; ++j) {
			long long aj = a + j*a;

			long long ajj = aj;
			while (ajj) {
				long long aji = ajj % 10;
				if (!occ[aji]) {
					occ[aji] = 1;
					remain--;
				}
				ajj /= 10;
			}
			if (!remain) {
				printf("%lld\n", aj);
				break;
			}
		}
		if (j >= INT_MAX / a) {
			printf("INSOMNIA\n");
		}


		//printf("Case #%d: %s", ni+1, buff);
	}

	return 0;
}