#include <bits/stdc++.h>
using namespace std;

set <int> s;
bool check(int a) {
	while (a) {
		s.insert(a%10);
		a/=10;
	}
	return s.size()==10;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
	int x, ans;
	for (int T=1; T<=t; T++) {
		cout << "Case #" << T << ": ";
		cin >> x;
		ans=x;
		if (ans==0) {
			cout << "INSOMNIA\n";
			continue;
		}
		while (1) {
			if (check(ans)) {
				cout << ans << "\n";
				s.clear();
				break;
			}
			else ans+=x;
		}
	}
	return 0;
}
