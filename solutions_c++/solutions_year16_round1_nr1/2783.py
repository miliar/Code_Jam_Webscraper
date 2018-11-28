#include <bits/stdc++.h>
using namespace std;

int Main () {
	string s;
	cin >> s;
	
	bool left[s.length()];
	memset (left, 0, sizeof left);
	
	int n = s.length();
	while (n > 1) {
		int idx = 0;
		for (int i=1; i<n; i++) {
			if (s[i] >= s[idx]) idx = i;
		}
		
		left[idx] = 1;
		n = idx;
	}
	
	string ans;
	for (int i=0; i<s.length(); i++) {
		if ( left[i] ) ans = s[i] + ans;
		else ans = ans + s[i];
	}
	
	cout << ans << endl;
	return 0;
}

int main () {
	freopen ("A-large (1).in", "r", stdin);
	freopen ("A-large (1).out", "w", stdout);

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int t;
	cin >> t;
	for (int tc=0; tc<t; tc++) {
		cout << "Case #" << tc + 1 << ": ";
		Main();
	}
	return 0;
}