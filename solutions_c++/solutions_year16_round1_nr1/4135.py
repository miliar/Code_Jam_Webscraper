#include <bits/stdc++.h>

using namespace std;

int TC;
string s, s1;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> TC;
	for (int i = 1; i <= TC; ++i) {
		cin >> s;
		s1 = s[0];
		for (int i = 1; i < s.size(); ++i) 
			if (s[i] >= s1[0])
				s1 = s[i]+s1;
			else
				s1 += s[i];
		cout << "Case #" << i << ": " << s1 << "\n";
	}
	return 0;
}