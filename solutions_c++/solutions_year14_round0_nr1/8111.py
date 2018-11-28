#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdio>

using namespace std;


int T;
map <int, int> m;


int main () {
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; t++) {
		m.clear();
		cout << "Case #" << t << ": ";
		int a, b, c;
		cin >> a;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> c;
				if (i == a) {
					m[c]++;
				}
			}
		}
		cin >> b;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> c;
				if (i == b) {
					m[c]++;
				}
			}
		}  
		int ans = -1;
		int cnt = 0;
		for (int i = 1; i <= 16; i++) {
			if (m[i] == 2) {
				cnt++;
				ans = i;
			}	
		}
		if (cnt == 0) {
			cout << "Volunteer cheated!\n";
		}
		if (cnt > 1) {
			cout << "Bad magician!\n";
		}
		if (cnt == 1) {
			cout << ans << "\n";
		}

	}
}