#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

typedef long long ll;

ll n, m, dv[20];

ll f(ll x){
	for (ll i = 2; i * i <= x; i++)
		if (x % i == 0)	return i;
	return	0;
}

ll get(ll ms, ll bs){
	ll x = 0, y = 1;
	while (ms){
		if (ms & 1)	x += y;
		ms >>= 1;
		y *= bs;
	}
	return f(x);
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	ll te;	cin >> te;
	cin >> n >> m;
	cout << "Case #1:\n";
	for (ll i = 0; m && i < (1<<(n - 2)); i++){
		ll ms = (1<<(n-1)) | (i<<1) | 1;
		bool fail = 0;
		for (ll j = 2; j <= 10; j++){
			dv[j] = get(ms, j);
			if (dv[j] == 0){
				fail = 1;
				break;
			}
		}
		if (!fail){
			m--;
			for (ll j = n - 1; j >= 0; j--)
				cout << ((ms>>j)&1);
			for (ll j = 2; j <= 10; j++)
				cout << " " << dv[j];
			cout << "\n";
		}
	}
	return	0;
}
