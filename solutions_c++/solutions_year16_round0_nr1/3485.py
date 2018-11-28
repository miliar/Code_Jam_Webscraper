#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T, d, e=(1<<10)-1;
ll N, n, c;

int main() {
	int t = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%lld", &N);
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", t++);
			continue;
		}
		d = 0;
		c = 1;
		while (1) {
			n = c * N;
			while (n) {
				d |= (1 << (n % 10));
				n /= 10;
			}
			if (d == e) break;
			c++;
		}
		printf("Case #%d: %lld\n", t++, c*N);
	}
	return 0;
}