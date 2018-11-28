#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas = 1, t;
	cin >> t;
	string s;
	while (t--) {
		cin >> s;
		cout<<"Case #"<<cas++<<": ";
		int c = 0;
		bool m = 0, pl = 0;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] == '-')
				m = 1;
			else
				pl = 1;
		}
		if (m == 0) {
			cout << 0 << endl;
			continue;
		}
		if (pl == 0) {
			cout << 1 << endl;
			continue;
		}

		for (int i = 1; i < s.size(); ++i) {
			if (s[i] == '-' && s[i - 1] == '+')
				c++;
		}
		if(s[0]=='-')
		{
			c++;
			cout<<2*c-1<<endl;
		}
		else
		{
			cout<<2*c<<endl;
		}

	}
}
