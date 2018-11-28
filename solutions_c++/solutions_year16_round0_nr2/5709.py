#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>

using namespace std;


int main()
{
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		string s;
		int ans = 0;
		cin >> s;
		cout << "Case #" << t << ": ";
		s += '+';
		for (auto i = 0; i < s.length()-1; ++i) {
			if (s[i] == '+' && s[i + 1] == '-') ans += 1;
			if (s[i] == '-' && s[i + 1] == '+') ans += 1;

		}
		cout << ans;

		cout << endl;
	}
	//system("pause");
	return 0;
}