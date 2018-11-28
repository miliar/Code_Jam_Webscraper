#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDEGE
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
#endif
	int t = 0;
	cin >> t;
	for (int k = 0; k < t; ++k) {
		long long standed = 0, ans = 0;
		string str;
		int Smax;
		cin >> Smax >> str;
		for (int i = 0; i < str.size(); ++i) {
			//cout << i << " " << standed << endl;
			if (standed < i) {
				int d = i - standed;
				ans += d;
				standed += d;
			}
			standed += str[i] - '0';

		}
		cout << "Case #" << k + 1 << ": " << ans << endl;
	}
	return 0;
}
