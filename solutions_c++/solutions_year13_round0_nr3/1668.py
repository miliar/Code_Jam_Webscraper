#include <iostream>
#include <sstream>
#include <map>

using namespace std;

typedef long long ll;

string tostr(ll x) {
	stringstream ss;
	ss << x;
	return ss.str();
}

bool palin(ll x) {
	string str = tostr(x);
	//cout << "length = " << str.length() << endl;
	//cout << "str = " << str << endl;
	//cout << "num = " << x << endl;
	for (int i = 0; i < str.length(); i++) {
		if (str[i] != str[str.length()-1-i]) {
			return false;
		}
	}
	//cout << "palin " << str << endl;
	return true;
}


int main() {
	ll a, b;
	map<ll,int> m;
	int t;
	int ctr = 0;
	for (ll i = 1LL; i <= 10000000LL; i++) {
		if (palin(i) && palin(i*i)) {
			m[i*i] = ctr++;
			//cout << i << " " << i*i << endl;
		}
	}
	m[10000000000000000LL] = ctr++;
	cin >> t;
	for (int kei = 1; kei <= t; kei++) {
		cin >> a >> b;
		cout << "Case #" << kei << ": ";
		cout << m.upper_bound(b)->second - m.lower_bound(a)->second << endl;
	}
	return 0;
}