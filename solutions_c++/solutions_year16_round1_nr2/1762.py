#include <bits/stdc++.h>

using namespace std;
int v[3000];
int main() {
	int t; cin >> t;

	for(int c = 1; c <= t; c++) {
		memset(v, 0, sizeof(v));
		set<int> s;
		int n; cin >> n;

		for (int i = 0; i < 2*n-1; i++) {
			for (int j = 0; j < n; j++ ) {
				int x; cin >> x;
				v[x]++;
			}
		}

		for (int i = 1; i <= 2500; i++) {
			if (v[i] % 2 != 0) {
				s.insert(i);
			}
		}

		printf("Case #%d: ", c);
		for (auto it = s.begin(); it != s.end(); it++) {
			cout << *it << " ";
		}
		cout << endl;
	}
}
