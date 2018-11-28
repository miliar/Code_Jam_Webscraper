#include <bits/stdc++.h>
using namespace std;
#define ll long long 

int main()
{
	ll t; scanf("%lld", &t);
	for (ll test = 1; test <= t; test++){
		ll n; scanf("%lld", &n);
		set<ll> s;
		for (ll i = 1; i < 100; i++){
			ll temp = i * n;
			while (temp > 0){
				s.insert(temp % 10);
				temp /= 10;
			}
			if (s.size() == 10){
				printf("Case #%lld: %lld\n", test, i * n);
				break;
			}	
		}
		if (s.size() != 10){
			printf("Case #%lld: INSOMNIA\n", test);
		}
	}
	return 0;
}
