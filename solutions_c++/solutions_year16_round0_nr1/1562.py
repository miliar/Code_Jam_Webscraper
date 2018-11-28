#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n, coef;
ll A[10];

void refresh() {
	coef = 0;
	for (ll i = 0; i < 10; i++) {
		A[i] = 0;
	}
}
string reverseString(string thestring) {
	string ans = "";
	for (ll i = thestring.size() - 1; i >= 0; i--) {
		ans += thestring[i];
	}
	return ans;
}
string toString(ll num) {
	string ans = "";
	ll temp2 = num;
	while (temp2) {
		ll dif = temp2 - temp2 / 10 * 10;
		temp2 /= 10;
		ans += ('0' + dif);
	}
	ans = reverseString(ans);
	return ans;
}
void count(ll num) {
	string newstring = toString(num);
	for (ll i = 0; i < newstring.size(); i++) {
		A[newstring[i] - '0'] = 1;
	}
}

void handle() {
	ll flag = 0;
	for (ll i = 0; i < 10; i++) {
		if (A[i] == 0) {
			flag = 1;
		}
	}
	if (!flag) {
		return;
	}
	coef++;
	count(n * coef);
	handle();
}

int main() {
	ll t; cin >> t;
	ll numoftest = 1;
	while (t--) {
		refresh();
		cin >> n;
		cout << "Case #" << numoftest << ": ";
		if (n != 0) {
			handle();
			cout << coef * n << endl;
		}
		else {
			cout << "INSOMNIA" << endl;
		}
		numoftest++;
	}
}
