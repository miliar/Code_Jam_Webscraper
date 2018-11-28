//Akshay Vats
//quasar

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool check(string s) {


	for (int i = 2; i <= 10; i++) {
		ll n = 0;
		ll b = 1;
		for (int j = 0; j < s.size(); j++) {
			n = b*(s[s.size() - j - 1] - '0') + n;
			b *= i;
		}
		bool pr = true;
		ll sq = sqrt(n);
		for (ll j = 2; j < sq; j++) {
			if (n%j == 0) {
				pr = false;
				break;
			}
		}
		if (pr) return false;
	}
	return true;
}
vector<ll> find(string s) {
	vector<ll> v;
	for (int i = 2; i <= 10; i++) {
		ll n = 0;
		ll b = 1;
		for (int j = 0; j < s.size(); j++) {
			n = b*(s[s.size() - j - 1] - '0') + n;
			b *= i;
		}

		ll sq = sqrt(n);
		for (ll j = 2; j < sq; j++) {
			if (n%j == 0) {
				v.push_back(j);
				break;
			}
		}

	}
	return v;
}

vector<string> ans;
vector<vector<ll>> aa;
ll ctr = 0;

void solve(string s, int i) {
	if (ans.size() > 500)
		return;
	if (i == s.size() - 1) {
		//ctr++;
		if (check(s)) {
			ans.push_back(s);
			aa.push_back(find(s));
		}
		return;

	}
	solve(s, i + 1);
	s[i] = '1';
	solve(s, i + 1);
	s[i] = '0';
}

int main()
{
	cin.tie(0);
	ios::sync_with_stdio(false);

	solve("1000000000000001", 1);
	cout << "Case #1:\n";
	for (int i = 0; i < 500; i++) {
		cout << ans[i] <<ans[i]<< " ";
		for (ll j : aa[i])cout << j << " ";
		cout << "\n";
	}
}