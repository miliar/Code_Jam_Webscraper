#include <bits/stdc++.h>
using namespace std;


int main () {
	int t;
	long long k, c, s;
	cin >> t;
	for (int x=1; x<=t; x++) {
		cin >> k >> c >> s;
		cout << "Case #" << x << ": ";
		if (k==s) {
		for (int i=1; i<=k; i++) cout << i << " ";
		cout << "\n";
		}
		else cout << "IMPOSSIBLE\n";
	}
}