#include<bits/stdc++.h>
using namespace std;

bool isCompleted(long long n) {
	//cout << n << endl;
	for(int i=0;i<10;i++) {
		if(!(1<<i & n)) {
			return false;
		}
	}
	return true;
}

typedef long long ll;

ll process(ll p) {
	ll b = 0;
	//cout << "lll" << endl;
	while(p) {
		b |= 1<<(p%10);
		p /= 10;
	}
	return b;
}

ll fun(ll k) {
	ll p = 0, s;
	s = k;
	while(!isCompleted(p)) {
		p |= process(s);
		s += k;
	}
	return s-k;
}

int main() {
	ll n, ip;
	cin >> n;
	for(ll i=1;i<=n;i++) {
		cin >> ip;
		if(ip  == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i << ": " << fun(ip) << endl;
		}
	}
	return 0;
}