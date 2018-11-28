#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long i64;

int T;
int N;

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T; ) {
		scanf("%d", &N);
		printf("Case #%d:", t);
		if (N == 0) {
			puts(" INSOMNIA");
			continue;
		}
		int mask = 0;
		for (int m = N; ; m += N) {
			int t = m;
			while (t) {
				mask |= 1 << (t % 10);
				t /= 10;
			}
			if (mask == 1023) {
				printf(" %d\n", m);
				break;
			}
		}
	}
	return 0;
}
