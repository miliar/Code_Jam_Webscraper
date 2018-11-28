//Akshay Vats
//quasar

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
	cin.tie(0);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	int cs = 1;
	while (t--) {
		string s;
		cin >> s;
		int st = s[0] == '+' ? 0 : 1;
		int len = 0;
		char l = 0;
		for (char c : s) {
			if (c != l)len++;
			l = c;
		}

		int ans;
		if (st == len % 2) ans = len;
		else ans = len - 1;
		cout << "Case #"<<cs++<<": "<<ans<<"\n";
	}
	return 0;
}