#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int main() {
#ifdef _DEBUG
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << t << ":";
		for (int i = 1; i <= k; i++) {
			cout << ' ' << i;
		}
		cout << endl;
	}
	return 0;
}