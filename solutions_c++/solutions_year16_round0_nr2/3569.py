#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int main() {
#ifdef _DEBUG
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		
		string s;
		cin >> s;
		int n = s.length();
		bool b[100];
		for (int i = 0; i < n; i++) {
			b[i] = (s[i] == '+');
		}

		int k = 0;

		while (find(b, b + n, false) - b < n) {
			int j = 0;
			while (b[j] && j < n) {
				b[j] = false;
				j++;
			}
			if (j != 0) {
				k++;
			}

			int f = -2;
			for (int i = 0; i < n; i++) {
				if (!b[i]) {
					f = i;
				}
			}
			f++;
			
			if (f > 0) {
				for (int i = 0; i < f; i++) {
					b[i] = !b[i];
				}
				reverse(b, b + f);

				k++;
			}
		}

		cout << "Case #" << t << ": " << k << endl;
		
	}
	return 0;
}