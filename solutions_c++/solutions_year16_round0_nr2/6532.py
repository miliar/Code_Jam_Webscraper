#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int j = 1; j <= t; j++) {
		string in;
		cin >> in;

		int cnt = 0;
		int r = in.length() - 1;
		while (in[r] == '+') r--;

		while (r >= 0) {
			int l = 0;
			if (in[0] == '+') {
				while (in[l] == '+') {
					in[l] = '-';
					l++;
				}
				cnt++;
			}
			while (in[l] == '-') l++;
			string tmp = in.substr(0, r+1);
			reverse(tmp.begin(), tmp.end());
			for (int i = 0; i < tmp.length(); i++) {
				if (tmp[i] == '+') tmp[i] = '-';
				else tmp[i] = '+';
			}

			in.replace(0, r+1, tmp);
			r -= l;
			cnt++;
		}

		cout << "Case #" << j << ": " << cnt << "\n";
	}
	return 0;
}