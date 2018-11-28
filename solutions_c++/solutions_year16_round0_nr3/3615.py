#include <stdio.h>
#define ll long long

bool isPrime(ll v) {
	if (v == 2)return true;
	else if (v % 2 == 0 || v < 2)return false;
	else {

		for (ll i = 3; i*i <= v; i += 2) {
			if (v%i)continue;
			return false;
		}

		return true;
	}
}

void func(ll v) {

	int a[17];
	int top = 0;
	while (v) {
		a[top++] = v & 1;
		v /= 2;
	}

	for (int i = top - 1; i >= 0; i--)printf("%d", a[i]);

}

int main() {

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int t;
	scanf("%d", &t);

	int tc = 0;

	while (t--) {

		ll n, a;
		scanf("%lld %lld", &n, &a);

		printf("Case #%d:\n", ++tc);

		for (ll i = (1 << (n - 1)) + 1; i < (1 << n) && a; i++) {

			if (i & 1) {

				ll x[10] = { 0 };

				bool flag = false;

				for (ll j = 2; j <= 10; j++) {

					ll k = i;
					ll l = 1;
					ll m = 0;

					while (k) {
						m += (k & 1) * l;
						l *= j;
						k /= 2;
					}

					if (!isPrime(m)) {
						x[j - 2] = m;
					}
					else {
						flag = true;
						break;
					}
				}

				if (flag)continue;
				
				a--;
				func(i);

				for (int j = 0; j < 9; j++) {

					flag = false;
					for (ll k = 2; k*k <= x[j]; k++) {
						if (x[j] % k)continue;
						printf(" %lld", k);
						flag = true;
						break;
					}

					if (!flag)printf(" %lld", x[j]);

				}

				printf("\n");

			}

		}

	}


}