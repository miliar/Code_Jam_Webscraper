#include <cstdio>
#include <algorithm>
using namespace std;

int T, D, P[1010];

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T;) {
		scanf("%d", &D);
		for (int i = 0; i < D; ++i) scanf("%d", P + i);

		int ret = 101010;
		for (int i = 1; i <= 1000; ++i) {
			int tmp = i;
			for (int j = 0; j < D; ++j) {
				tmp += (P[j] - 1) / i;
			}
			ret = min(ret, tmp);
		}

		printf("Case #%d: %d\n", t, ret);
	}
	return 0;
}
