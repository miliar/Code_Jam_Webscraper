#include <bits/stdc++.h>

using namespace std;

int main() {
	int _T;
	cin >> _T;
	for(int _t = 1; _t <= _T; _t++) {
		cout << "Case #" << _t << ": ";
		string s;
		int k;
		cin >> s >> k;
		int res = 0;
		for(int i=0; i + k - 1 < s.size(); i++) {
			if (s[i] == '-') {
				res++;
				for(int j=i; j<i+k; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		bool flag = 1;
		for(int i=0; i<s.size(); i++)
		if (s[i] == '-')
			flag = 0;
		if (flag)
			cout << res << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}