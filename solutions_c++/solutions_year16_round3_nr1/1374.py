#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	int t, tc = 1;
	int n, a;
	cin >> t;
	while (t--) {
		cin >> n;
		string s = "";
		for (int i = 0; i < n; i++) {
			cin >> a;
			for (int j = 0; j < a; j++) {
				s += (char)'A' + (char)i;
			}
		}
		cout << "Case #" << tc++ << ": ";
		int l, r;
		int sl = s.length();
		if (sl % 2 == 0) {
			l = sl/2-1;
			r = sl/2;
		} else {
			l = r = sl/2;
		}
		while (l >= 0) {
			if (l == r) cout << s[l] << ' ';
			else cout << s[l] << s[r] << ' ';
			l--; r++;
		}
		cout << endl;
	}
	return 0;
}