#include <iostream>
using namespace std;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	for (int t = 0; t < n; ++t) {
		int s1;
		cin >> s1;
		int a[4][4];
		int b[4][4];
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> a[i][j];
		int s2;
		cin >> s2;
		--s1;
		--s2;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> b[i][j];
		int cnt = 0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a[s1][i] == b[s2][j])
					++cnt;
		cout << "Case #" << t + 1 << ':' << ' ';
		if (cnt > 1) {
			cout << "Bad magician!" << '\n';
			continue;
		}
		if (cnt == 0) {
			cout << "Volunteer cheated!\n";
			continue;
		}
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a[s1][i] == b[s2][j]) {
					cout << a[s1][i] << '\n';
				}
	}
}