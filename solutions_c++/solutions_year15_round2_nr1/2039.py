#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef long long ll;


vector<ll> mas;
ll mas_size = 1e6 + 5;

ll rev(ll n) {
	ll res = 0;
	while(n > 0) {
		res = res * 10 + n % 10;
		n /= 10;
	}
	return res;
}

ll count_n(ll x) {
	for(ll n = 1; n < x; n++) {
		mas[n + 1] = min(mas[n] + 1, mas[n + 1]);
		ll revn = rev(n);
		if(revn > n && revn < mas_size) {
			mas[revn] = min(mas[revn], mas[n] + 1);
		}
	}
	return mas[x];
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	ll n;
	ll d;
	ll res;
	int it;
	cin >> t;
	for(int o = 0; o < t; o++) {
		cin >> n;
		mas.clear();
		mas.resize(mas_size);
		for(int i = 0; i < mas_size; i++) {
			mas[i] = i;
		}
		cout << "Case #" << (o + 1) << ": " << count_n(n) << endl;
	}
	return 0;
}


/*		cin >> n;
		d = 10;
		res = 0;
		it = 0;
		
		if(n < 91) {
			cout << n << endl;
			//cerr << n << endl;			
			continue;
		}
		
		res = (ll)19;
		while(mas[1] * d + mas[0] <= n) {
			if(n < mas[1] * d * ((ll)10) + mas[0]) {
				res += (n - mas[1] * d - mas[0] + 1);
			}
			else {
				res += mas[0] * d + mas[1];
			}
			//cerr << "res: " << res << endl;
			d *= (ll)10;
		}
		
		//cerr << (mas[1] * d + mas[0]) << endl;
		cout << res << endl;
		//cerr << res << endl;
*/
