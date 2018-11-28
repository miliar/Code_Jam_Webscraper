#include <cstdio>

using namespace std;

typedef long long ll;
const ll MAXN = 10000;

ll rev(ll N) {
	ll ret = 0;
	while (N) {
		ret *= 10;
		ret += N % 10;
		N /= 10;
	}
	return ret;
}

bool ispal(ll k) {
	return k == rev(k);
}

ll p1(ll N) {
	ll fac = 1;
	ll k = N;
	ll ret = 0;
	while (k) {
		ret *= 10;
		ret += k % 10;
		k /= 10;
		fac *= 10;
	}
	return N * fac + ret;
}

ll p2(ll N) {
	ll fac = 1;
	ll k = N;
	ll ret = 0;
	while (k) {
		ret *= 10;
		ret += k % 10;
		k /= 10;
		fac *= 10;
	}
	return (N / 10) * fac + ret;
}

int Q, A, B;
int main() {
	scanf("%d", &Q);
	for(int q = 1; q <= Q; ++q) {
		printf("Case #%d: ", q);
		scanf("%d %d", &A, &B);
		int ans = 0;

		for(int i = 1; i < MAXN; ++i) {
			ll pal1 = p1(i);
			ll pal2 = p2(i);
			ll sq1 = pal1 * pal1;
			ll sq2 = pal2 * pal2;
			if (ispal(sq1) && sq1 >= A && sq1 <= B) ++ans;
			if (ispal(sq2) && sq2 >= A && sq2 <= B) ++ans;
		}
		printf("%d\n", ans);
	}

	return 0;
}
