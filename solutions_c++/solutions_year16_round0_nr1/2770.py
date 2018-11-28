#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;
int v[10];

int main() {
	int o, cas = 0;
	scanf("%d", &o);
	//for (int p = 0; p <= 1000000; p++) {
	while (o--) {
		ll n, m;
		cin>>n;
		//n = p;
		m = n;
		printf("Case #%d: ", ++cas);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		memset(v, 0, sizeof(v));
		int res = 0;
		while (1) {
			ll x = n;
			while (x) {
				int t = x % 10;
				if (v[t] == 0) {
					v[t] = 1;
					res++;
				}
				x/=10;
			}
			if (res == 10) break;
			n += m;
		}
		printf("%lld\n", n);
	}
}