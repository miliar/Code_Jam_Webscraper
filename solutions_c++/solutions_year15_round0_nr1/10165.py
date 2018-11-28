#include <bits/stdc++.h>

using namespace std;

int main ()
{
	freopen ("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int t, n; cin >> t;
	string s; int c = 1;
	
	while (t--) {
		cin >> n; cin >> s;
		int count = 0, sum = s[0]-'0';
		for (int i = 1; i < s.length(); i++) {
			if (s[i] != '0') {
				if (sum < i) {
					count += (i - sum);
					sum += count;
				}
				sum += s[i] - '0';
			}
		}
		cout << "Case #" << c++ << ": " << count << endl;
	}
	return 0;
}
