#include <iostream>
using namespace std;

int pos(int x) {
	return x<0?0:x;
}

int main() {
	int t, l;
	cin >> t;
	string s;
	for(int tt = 1; tt <= t; tt++) {
		cin >> l >> s;
		int count = 0, ans = 0;
		for(int i = 0; i < l+1; i++) {
			int x = s[i] - '0';
			if (count < i) 
				ans += (i - count);
			count += pos(i - count) + x;
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}