#include <bits/stdc++.h>
using namespace std;
int mat[2][4][4], row[2], tests;
int main() {
	freopen("Ulaz.txt","r",stdin);
	cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		for (int i = 0; i < 2; ++i) {
			cin >> row[i]; row[i]--;
			for (int dx = 0; dx < 16; ++dx) cin >> mat[i][dx/4][dx%4];
		}
		vector<int> w;
		multiset<int> cnt;
		for (int i = 0; i < 4; ++i) cnt.insert(mat[0][row[0]][i]), cnt.insert(mat[1][row[1]][i]);
		for (int i = 1; i <= 16; ++i) if (cnt.count(i) > 1) w.push_back(i);
		cout << "Case #" << t << ": ";
		if (w.size() == 0) cout << "Volunteer cheated!" << endl;
		else if (w.size() > 1) cout << "Bad magician!" << endl;
		else cout << w[0] << endl;
	}
}
