#include <bits/stdc++.h>
using namespace std;

int main () {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int S;
		cin >> S;
		string s;
		cin >> s;
		int count = 0;
		int res = 0;
		for(int i = 0; i < S+1; i++) {
			if(count < i && s[i] > '0') {
				res += i - count;
				count = i;
			}
			count += int(s[i]-'0');
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}
