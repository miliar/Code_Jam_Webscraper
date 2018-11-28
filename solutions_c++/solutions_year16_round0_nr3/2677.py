#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int T, N, J;
int a[11];
int d[33];

int calcPrime(ll n) {
	for (ll i = 2; i * i <= n; i++) 
		if (n % i == 0) return i;
	return 0;
}

int main() {
	scanf("%d",  &T);
	for (int tt = 1; tt <= T; tt++) {
		scanf("%d%d", &N, &J);
		printf("Case #%d:\n", tt);
		memset(d, 0, sizeof(d));
		d[N-1] = d[0] = 1;
		for (int i = 0; i < 1 << (N-2); i++) {
			bool flag = true;
			for (int j = 2; j <= 10; j++) {
				ll x = 0;
				int t;
				for (int k = N - 1; k >= 0; k--)
					x = x * j + d[k];
				if ((t=calcPrime(x))) {
					a[j] = t;
				}
				else {
					flag = false;
					break;
				}
			}
			if (flag) {
				for (int j = N-1; j >= 0; j--) printf("%d", d[j]);
				for (int j = 2; j <= 10; j++) printf(" %d", a[j]);
				puts("");
				J--;
				if (!J) break;
			}
			for (int j = 2; j < N - 1; j++) {
				if (d[j] == 1) 
					d[j] = 0;
				else {
					d[j] = 1;
					break;
				}
			}
		}
	}
	return 0;
}
