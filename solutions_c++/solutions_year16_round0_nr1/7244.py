#include <stdio.h>

typedef long long ll;

ll num[10];

void renew(ll n){
	while (n > 0){
		num[n % 10]++;
		n /= 10;
	}
}

ll check(ll n){
	for (int i = 0; i < 10; ++i)num[i] = 0;
	for (ll i = 1;; ++i){
		ll acc = n*i;
		renew(acc);
		ll pro = 1;
		for (int i = 0; i < 10; ++i){
			pro *= num[i];
		}
		if (pro != 0)return acc;
	}
}

int main(){

	FILE *fi;
	FILE *fo;
	ll t;
	fi = fopen("A-large.in", "r");
	fo = fopen("A-large.out", "w");

	fscanf(fi, "%lld", &t);
	for (int i = 1; i <= t; ++i){
		ll n;
		fscanf(fi, "%lld", &n);
		if (n == 0)
			fprintf(fo, "Case #%d: INSOMNIA\n", i);
		else
			fprintf(fo, "Case #%d: %lld\n", i, check(n));
	}
	return 0;
}