#include <bits/stdc++.h>
#define pb push_back
#define popb pop_back
#define mkp make_pair
#define par pair<ll, ll>
#define N 200010

typedef long long ll;

using namespace std;

ll quickExpo(ll x, ll n){
	if(n == 1)
		return x;
	if(n == 0)
		return 1;
	if(n % 2 == 0){
		ll aux = pow(x, n/2);
		return aux * aux;
	}else
		return x * pow(x, n-1);
}

int main(){

	ll n, m, i, k, j;

	scanf("%lld\n", &n);

	for(k = 1; k <= n; k++){
		string s;
		getline(cin, s);

		printf("Case #%lld: ", k);

		string f = "";
		f += s[0];

		for(i = 1; i < s.length(); i++){
			if(s[i] >= f[0])
				f = s[i] + f;
			else
				f += s[i];
		}

		cout << f << endl;
	}
	return 0;
}
