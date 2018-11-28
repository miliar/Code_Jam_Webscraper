#include <bits/stdc++.h>

using namespace std;

#define ll long long

int t;


void solve();

int main() {
	ios::sync_with_stdio(0);

	bool file = true;
	if (file) {
		freopen("A-large.in","r", stdin);
		freopen("output.out", "w", stdout);
	}

	cin >> t;
	for (int z = 1; z<= t; z++) {
		cout << "Case #" << z << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

void solve() {
	ll num;
	cin >> num;
	if (num <= 0)  { cout << "INSOMNIA"; return; }
	bool found[10];
	for (int i = 0; i < 10; i++) found[i] = false;
	ll n = 1;
	while(true) {
		ll cur = num * n++;
		ll soln = cur;
		while(cur) {
			found[cur%10] = true;
			cur/=10;
		}
		bool solved = true;
		for (int i = 0; i < 10; i++)
			if (!found[i])
				solved = false;
		if (solved) {
			cout << soln; return;
		}
	}
}
