#include <cstdio>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;

ll T, n, f[10];

int jud() {
	for (int i = 0; i <= 9; i++) if (!f[i]) return 0;
	return 1;
}

void work(ll x) {
	while (x) {
		f[x % 10] = 1;
		x /= 10;
	}
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		ll n, t;
		scanf("%lld", &n);
		t = n;
		if (n == 0) printf("Case #%d: INSOMNIA", i);
		else {
			memset(f, 0, sizeof f);
			work(t);
			while (!jud()) {
				t += n;
				work(t);
			}
			printf("Case #%d: %lld", i, t);
		}
		if (i != T) printf("\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}