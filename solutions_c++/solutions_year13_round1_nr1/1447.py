#include<cstdio>
using namespace std;

int main() {
    int n; scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		long long r, t;
		scanf("%lld %lld", &r, &t);
		long long u = 0;
		long long a = 0;
		while (u <= t) {
			long long c = 2 * r + 1;
			if (u + c > t) break;
			a++;
			r += 2;
			u += c;
		}
		printf("Case #%d: %lld\n", i, a);
	}
	return 0;
}