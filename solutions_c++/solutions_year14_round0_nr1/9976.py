#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

int a[5][5], b[5][5];
map <int, int> m;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int a1, a2;
		cin >> a1; a1--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> a2; a2--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> b[i][j];
		m.clear();
		for (int i = 0; i < 4; i++)
			m[a[a1][i]] ++;
		for (int i = 0; i < 4; i++)
			m[b[a2][i]] ++;
		int k = 0, res = 0;
		for (int i = 1; i <= 16; i++)
			if (m[i] == 2) {
				k++;
				res = i;
			}
		printf("Case #%d: ", t);
		if (k == 1)
			cout << res;
		else if (k > 1)
			cout << "Bad magician!";
		else cout << "Volunteer cheated!";
		cout << endl;
	}
	return 0;
}