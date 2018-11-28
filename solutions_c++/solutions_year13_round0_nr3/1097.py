
#include <iostream>
#include <sstream>
using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;

string toStr(ll n) {
	ostringstream ss;
	ss << n;
	return ss.str();
}

ll pal1(ll n) {
	string const& s = toStr(n);
	rep (i,s.size()) {
		n *= 10;
		n += s[s.size()-1-i]-'0';
	}
	return n;
}

ll pal2(ll n) {
	string const& s = toStr(n);
	rep (i,s.size()-1) {
		n *= 10;
		n += s[s.size()-2-i]-'0';
	}
	return n;
}

bool isPal(ll n) {
	string const& s = toStr(n);
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] != s[s.size()-1-i]) {
			return false;
		}
	}
	return true;
}

ll number(ll N) {
	if (N == 0) return 0;
	ll count = 0;
	for (ll i = 1; ; ++i) {
		ll p = pal1(i);
		p *= p;
		if (p > N) break;
		if (isPal(p)) ++count;
	}
	for (ll i = 1; ; ++i) {
		ll p = pal2(i);
		p *= p;
		if (p > N) break;
		if (isPal(p)) ++count;
	}
	return count;
}

void solve() {
	ll A, B;
	cin >> A >> B;
	cout << number(B)-number(A-1) << endl;
}

int main() {
	int T;
	cin >> T;
	rep (i,T) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
