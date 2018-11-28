#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long ll;

ll solve(ll N) {
	ll ans = 1;
	ll count[10] = {0};
	bool notDone = true;
	while (true) {
		ll temp = ans * N;
		while(temp) {
			++count[temp % 10];
			temp /= 10;
		}
		
		// printf("%lld %lld\n", ans, N);
		int test_count = 0;
		for (int i = 0; i < 10; ++i) test_count += (count[i] != 0);
		if (test_count == 10) return ans * N;
		++ans;
		// printf("test_count = %lld\n");
	}
	// return ans * N;
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	ll N;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		scanf("%lld", &N);
		printf("Case #%d: ", i + 1);
		if (N == 0) printf("INSOMNIA\n");
		else printf("%lld\n", solve(N));
	}
	return 0;
}

