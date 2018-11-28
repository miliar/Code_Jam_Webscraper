#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		string l; cin >> l;
		char curr = l[0];
		int cnt = 0;
		for (int i = 1; i < l.size(); ++i) if (l[i] != curr) {
			curr = l[i];
			++cnt;
		}
		if (curr == '-')
			++cnt;
		cout << "Case #" << (t+1) << ": " << cnt << endl;
	}
}