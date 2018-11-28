#include <bits/stdc++.h>	

using namespace std;

const int M = 1000;

int main (void) {
	int T;
	cin >> T;
	for (int c = 1; c <= T; ++c) {
		cout << "Case #" <<  c << ": ";
		
		int D, md = 0;
		cin >> D;

		vector <int> v(D);
		priority_queue<int> q;
		for (int i = 0; i < D; ++i) {
			cin >> v[i];
			md = max(md, v[i]);
		}
	
		int res = M;
		for (int i = 1; i <= md; ++i) {
			int curr = 0;
			for (int j = 0; j < D; ++j) {
				if (v[j] == i) continue;
				curr += (v[j] + i - 1)/i - 1;
			}
			res = min(res, curr + i);
		}

		cout << res << endl;
	}
	return 0;
}