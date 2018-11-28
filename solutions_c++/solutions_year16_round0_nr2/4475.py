#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
	ll t; scanf("%lld", &t);
	for (ll test = 1; test <= t; test++){
		char s[110]; scanf("%s", s);
		ll p = 1, n = 1;
		ll l = strlen(s);
		for (int i = 0; i < l; i++){
			if (s[i] == '-') p = 0;
			if (s[i] == '+') n = 0;
		}
		if (p) printf("Case #%lld: %lld\n", test, 0LL);
		else if (n) printf("Case #%lld: %lld\n", test, 1LL);
		if (p == 0 && n == 0){
			ll cnt = 0, i = 0, f = 0;
			while (s[i] == '-'){
				i++;
				f = 1;
			}
			if (f) cnt++;
			while (i < l - 1){
				if (s[i] == '+' && s[i + 1] == '-') cnt += 2;
				i++;
			}
			printf("Case #%lld: %lld\n", test, cnt);
		}
	}
	return 0;
}
