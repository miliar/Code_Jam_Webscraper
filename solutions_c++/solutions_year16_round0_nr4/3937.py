#include <bits/stdc++.h>

using namespace std;

#define ll				long long int
#define vi				vector<int>
#define vl				vector<ll>
#define pii				pair<int,int>
#define pil				pair<int, ll>
#define pll				pair<ll, ll>
#define pli				pair<ll, int>
#define pb				push_back
#define mp				make_pair
#define MOD				1000000007
#define F				first
#define S				second

ll pow_mod(ll a, ll b) {
	ll res = 1;
	while(b) {
		if(b & 1)
			res = (res * a);
		a = (a * a);
		b >>= 1;
	}
	return res;
}

int main(){

	int t;
	scanf("%d", &t);

	for(int i=1;i<=t;i++){

		ll k,c,s;
		scanf("%lld %lld %lld", &k, &c, &s);

		ll len = pow_mod(k,c);
		ll skip = pow_mod(k,c-1);

		printf("Case #%d: ", i);

		ll res = 1;
		for(int j = 1;j<=s;j++){

			printf("%lld ", res);
			res += skip;

		}
		printf("\n");

	}

	return 0;
}
