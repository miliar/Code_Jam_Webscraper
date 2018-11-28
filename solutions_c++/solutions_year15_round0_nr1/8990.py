#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll t, smax;

char ar[10000];

int main(){

	scanf("%lld", &t);

	for(ll it=1; it<=t; it++){

		scanf("%lld %s", &smax, &ar);

		ll r = 0;
		ll act = ar[0] - '0';

		for(ll i=1; i <= smax; i++){
			if(i > act){
				r += i - act;
				act += (i-act);
			}
			act += (ar[i] - '0');
			if(act >= smax) break;
		}

		printf("Case #%lld: %lld\n", it, r);

	}

}