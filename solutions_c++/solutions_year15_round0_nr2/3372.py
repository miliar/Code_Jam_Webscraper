#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDEGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int t = 0;
	cin >> t;
	for (int k = 0; k < t; ++k) {
		int d;
		cin >> d;
//		cout << d << endl;
		vector<int> v(d);
		for (int i = 0; i < d; ++i) {
			cin >> v[i];
//			cout << v[i]<<" ";
		}
//		cout << endl;
		sort(v.rbegin(),v.rend());

		int m = v[0];
		int res = v[0];

		for (int r = 1; r < m+1; ++r) {
			int move = 0;
			for (int j = 0; j < v.size(); ++j) {
				if(v[j]<=r)
					break;
				 move += ceil(float(v[j]) / float(r)) - 1;
			}
			if( move + r < res)
				res = move+r;
		}

		cout << "Case #" << k + 1 << ": " << res << endl;
	}
	return 0;
}
