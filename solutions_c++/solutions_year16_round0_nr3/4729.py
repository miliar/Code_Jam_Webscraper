#include <bits/stdc++.h>
using namespace std;

#define INF 0x3F3F3F3F
#define INFL 0x3F3F3F3F3F3F3F3FLL
#define sz(X) int((X).size())
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define ll long long

ll ntobase(char *str, int b) {
	ll ans = 0;
	for (int i = 0; str[i]; ++i)
		ans = ans*b + str[i]-'0';
	return ans;
}

int isPrime(ll x, ll *vet, int b) {
	if (x == 2) return 1;
	if (x&1 == 0) {
		vet[b] = 2;
		return 0;
	}
	for (ll p = 3; p*p <= x; p += 2) {
		if (x % p == 0) {
			vet[b] = p;
			return 0;
		}
	}
	return 1;
}

int main(int argc, char const *argv[]) {
	int n, j, x, cnt = 0;
	char str[64]; 
	scanf("%*d %d %d", &n, &j);
	x = (1<<(n-1))+1;
	puts("Case #1:");
	for (int i = 0; i < (1<<(n-2))-1; i++) {
		if (cnt == j) break;
		int y = x + (i<<1);
		str[n] = '\0';
		for (int j = n-1; j >= 0; --j) {
			str[j] = (y&1) + '0';
			y >>= 1;
		}
		//puts(str);
		int ok = 1;
		ll vet[11];
		for (int b = 2; b <= 10; b++) {
			ll z = ntobase(str, b);
			if (isPrime(z, vet, b))
				ok = 0;
		}
		if (ok) {
			cnt++;
			printf("%s", str);
			for (int b = 2; b <= 10; b++)
				printf(" %lld", vet[b]);
			puts("");
		}
	}
	return 0;
}