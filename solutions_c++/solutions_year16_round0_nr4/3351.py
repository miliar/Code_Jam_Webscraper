#include <bits/stdc++.h>
using namespace std;

#define ll long long
int main(){
	ll t; scanf("%lld", &t);
	for (ll test = 1; test <= t; test++){
		ll k, c, s; scanf("%lld %lld %lld", &k, &c, &s);
		printf("Case #%lld: ", test);
		for (ll i = 1; i <= s; i++) printf("%lld ", i);
		printf("\n");
	}
	return 0;
}
