/*
ID: ashish1610
PROG:
LANG: C++
*/
#include<bits/stdc++.h>
using namespace std;
#define ll				long long int
#define MOD				1000000007
#define si(a)			scanf("%d", &a)
#define sl(a)			scanf("%lld", &a)
#define pi(a)			printf("%d", a)
#define pl(a)			printf("%lld", a)
#define pn 				printf("\n")
ll pow_mod(ll a, ll b) {
	ll res = 1;
	while(b) {
		if(b & 1) {
			res = (res * a) % MOD;
		}
		a = (a * a) % MOD;
		b >>= 1;
	}
	return res;
}
long double prob[20];
int main() {
	int t;
	cin >> t;
	for(int tcase = 1; tcase <= t; ++tcase) {
		int n, k;
		cin >> n >> k;
		for(int i = 0; i < n; ++i) {
			cin >> prob[i];
		}
		long double res = 0.0;
		for(int i = 0; i < (1 << n); ++i) {
			if(__builtin_popcount(i) == k) {
				vector < long double > v;
				for(int j = 0; j < n; ++j) {
					if(i & (1 << j)) {
						v.push_back(prob[j]);
					}
				}
				long double res1 = 0.0;
				for(int j = 0; j < (1 << k); ++j) {
					if(__builtin_popcount(j) == k / 2) {
						long double tmp = 1.0;
						for(int l = 0; l < k; ++l) {
							if(j & (1 << l)) {
								tmp = tmp * v[l];
							} else {
								tmp = tmp * (1 - v[l]);
							}
						}
						res1 += tmp;
					}
				}
				res = max(res, res1);
			}
		}
		cout << "Case #" << tcase << ": ";
		printf("%0.9Lf\n", res);
	}
	return 0;
}