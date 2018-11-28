#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>

using namespace std;

const int N = 1000 + 5;

int main() {
#ifdef _DEBUG
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		
		string s;
		int k;

		cin >> s >> k;
		int n = s.length();
		bool a[N];
		for (int i = 0; i < n; i++) {
			a[i] = (s[i] == '+');
		}
		
		int d = 0;
		for (int i = 0; i + k <= n; i++) {
			if (!a[i]) {
				d++;
				for (int j = 0; j < k; j++) {
					a[i + j] = !a[i + j];
				}
			}
		}

		bool impossible = false;
		for (int i = 0; i < n && !impossible; i++) {
			impossible = !a[i];
		}

		if (impossible) {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << d;
		}
		cout << endl;
	}

	return 0;
}