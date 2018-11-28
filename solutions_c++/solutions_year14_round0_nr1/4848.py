#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>

#define LL long long

using namespace std;

LL T, temp, ans, s1, s2, count[20];

int main() {
	freopen("ex.in", "r", stdin);
	freopen("ex.out", "w", stdout);

	cin >> T;
	for (int it = 0; it < T; it++) {
        ans = -1;
		cin >> s1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> temp;
				if (i + 1 == s1) count[temp] = it + 1;
			}
		}
		cin >> s2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> temp;
				if ((i + 1 == s2) && (count[temp] == it + 1)) {
					if (ans == -1) ans = temp;
					else ans = -2;
				}
			}
		}
		cout << "Case #" << it + 1 << ": ";
		if (ans == -1) cout << "Volunteer cheated!" << endl;
		else if (ans == -2) cout << "Bad magician!" << endl;
		else cout << ans << endl;
	}
	return 0;
}
