#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int tc;
	bool check[11];
	scanf("%d\n", &tc);
	for (int testcase = 1; testcase <= tc; testcase++) {
		int n = 0, cnt = 0;
		long long now = 0, it = 0;
		scanf("%d", &n);
		printf("Case #%d: ", testcase);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		for (int i = 0; i < 10; i++) {
			check[i] = false;
		}
		while (cnt < 10) {
			it++;
			now = (long long)n * it;
			while (now > 0) {
				if (!check[now % 10]) {
					check[now % 10] = true;
					cnt++;
				}
				now /= 10;
			}
		}
		printf("%lld\n", (long long)n*it);
	}
}