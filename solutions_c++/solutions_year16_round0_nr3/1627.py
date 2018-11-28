#include <bits/stdc++.h>
// https://gmplib.org/
#include "gmpxx.h"
typedef mpz_class big;
#define N 10000000
using namespace std;
typedef long long int LL;
LL prime[N + 10], lp[N + 10];
big p[N + 10];
int sz = 0;
void sievelp() {
    for(LL i=2 ; i<N ; i++) {
        if( lp[i] == 0 ) {
            lp[i] = i;
            prime[sz++] = i;
            p[sz - 1] = (int)i;
        }
        for(LL k=0 ; k < sz && prime[k] <= lp[i] && i * prime[k] < N ; k++)
            lp[i * prime[k]] = prime[k];
    }
}
big bigPow(big a, int b) {
	big ans = 1;
	for(int i=0 ; i<b ; i++) ans *= a;
	return ans;
}
int main() {
	sievelp();
	int T, bits, n;
	scanf("%d", &T);
	for(int caso=1 ; caso<=T ; caso++) {
		scanf("%d %d", &bits, &n);
		printf("Case #%d:\n", caso);
		int limit = 1 << (bits - 2);
		for(int mask=0 ; mask<limit && n; mask++) {
			vector<LL> v;
			for(int base=2 ; base<=10 ; base++) {
				big data = 1 + bigPow(base, 31);
				big pot = base;
				big baseTmp = base;
				for(int i=0 ; i<(bits-2) ; i++, pot *= baseTmp )
					if( mask & (1<<i) ) data += pot;
				for(int i=0 ; i<sz ; i++) {
					if( data % p[i] == 0 ) {
						v.push_back(prime[i]);
						break;
					}
				}
			}
			if( v.size() == 9 ) {
				n--;
				printf("1");
				for(int i=bits-3 ; i>=0 ; i--)
					if( mask & (1<<i) ) printf("1");
					else printf("0");
				printf("1");
				for(int i=0 ; i<v.size() ; i++) printf(" %lld", v[i]);
				printf("\n");
			}
		}
	}
	return 0;
}