#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int t;
ll n;
int v[12];

void parse(ll x){
	ll y = x;
	while(y/10 > 0){
		v[y%10]++;
		y/=10;
	}
	v[y]++;
}

int main () {

	scanf("%d", &t);
	int caso = 1;

	while(t--){
		
		scanf("%lld", &n);
		ll ans = 0;
		bool ok = false;

		memset(v,0,sizeof v);

		for(ll i = 1; i <= 1e5; i++){
			parse(n*i);
			bool all = true;
			ans++;

			for(int j = 0; j <= 9; j++){
				if(v[j] == 0){
					all = false;
					break;
				}
			}
			if(all){
				ok = true;
				break;
			}
		}
		printf("Case #%d: ",caso++);
		if(ok)
			printf("%lld\n", n*ans);
		else
			printf("INSOMNIA\n");
	}

	return 0;
}