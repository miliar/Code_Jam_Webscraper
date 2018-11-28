#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <(b); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
const int maxn = 32;
int n = 16;
int J = 50;

typedef long long ll;

ll pows[16][32];
ll prime[50485760];
int np = 0;
int div[16];
int is_prime(ll x, int& d) {
	if(x%2==0) {
		if(x == 2) return 1;
		else {
			d = 2;
			return 0;
		}
	}
	FOR(i,1,np) {
		if(x%prime[i]==0) {
			d = prime[i];
			return 0;
		}
		if(prime[i]*prime[i] > x) return 1;
	}
	return 1;
}
void find_prime() {
	prime[np++] = 2;
	prime[np++] = 3;
	prime[np++] = 5;
	prime[np++] = 7;
	for(ll x = 11; np < 200000; x+=2) {
		for(int i = 1; i < np;++i) {
			if(x % prime[i] == 0) break;
			if(prime[i]*prime[i] > x) {
				prime[np++] = x;
				break;
			}
		}
	}
//	printf("np = %d, last prime = %lld\n", np, prime[np-1]);
}
int main() {
	int ans = 0;
	printf("Case #1:\n");
	find_prime();
	FOR(b,2,11) {
		ll B = b;
		pows[b][0] = 1;
		FOR(j,1,20)
			pows[b][j] = pows[b][j-1] * B;
	}
	ll nn = 1<<n;
	for(ll x = 0; x < nn; ++x) {
		if((x&1)==1 && (x&(1<<(n-1)))==(1<<(n-1)));
		else continue;
		/*
		{
			printf("trying x = %lld: ", x);
			for(int i = n-1; i>=0;--i) {
				if(x & (1<<i)) printf("1");
				else printf("0");
			}
			printf("\n");
		}
		*/
		int flag = 0;
		FOR(b,2,11) { // base
			ll num_b = 0;
			FOR(i,0,n) {
				if(x&(1<<i)) {
					num_b += pows[b][i];
				}
			}
			//printf("\tin base %d, num = %lld\n", b, num_b);
			if(is_prime(num_b, div[b])) {
				flag = 1;
				break;
			}
		}
		if(!flag) {
			for(int i = n-1; i>=0;--i) {
				if(x & (1<<i)) printf("1");
				else printf("0");
			}
			FOR(b,2,11) {
				printf(" %d", div[b]);
			}
			printf("\n");

			ans++;
			if(ans >= J) break;
			/*
			FOR(b,2,11) { // base
				ll num_b = 0;
				FOR(i,0,n) {
					if(x&(1<<i)) {
						num_b += pows[b][i];
					}
				}
				printf("\tin base %d, num = %lld\n", b, num_b);
			}
			*/
		}
	}
	return 0;
}
