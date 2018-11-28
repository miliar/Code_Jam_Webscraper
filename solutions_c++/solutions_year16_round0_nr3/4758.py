#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, j, ja;

ll checkDiv(ll num) {
	for (int i = 2; i <= sqrt(num); i++) {
		if (num%i == 0) return i;
	}

	return num;
}

bool solve(string s) {
	ll v[11];
	vector<int> ans;

	for (int i = 2; i <= 10; i++) {
		ll aux = 1, num = 0;
		for (int j = s.size()-1; j >= 0; j--) {
			num += (s[j]-'0') * aux;
			aux *= i;
		}	
		v[i] = num;
	}

	for (int i = 2; i <= 10; i++) {
		ll cd = checkDiv(v[i]);
		if (cd == v[i]) return false;
		else ans.push_back(cd);
	}

	cout << s << " ";
	for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
	cout << endl;

	return true;
}

void go (string s) {
	if (s.size() == n-1) {
		if (ja == j) exit(0);

		if (solve(s+'1')) ja++;

		return;
	}

	go(s+'1');
	go(s+'0');
}

int main(void) {
	cin >> n >> n >> j;

	cout << "Case #1:" << endl;
	go("1");

	return 0;
}
