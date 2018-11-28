#include <iostream>
#include <cstring>

using namespace std;

bool mark[20];
int a[4][4], b[4][4];

int main() {
	int t;
	cin >> t;
	for (int o = 0; o < t; o++) {
		int r1, r2;
		cin >> r1; r1--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> a[i][j];
		cin >> r2; r2--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> b[i][j];
		memset(mark, 0, sizeof mark);
		for (int i = 0; i < 4; i++)
			mark[a[r1][i]] = true;
		int cnt = 0, ans = -1;
		for (int i = 0; i < 4; i++)
			if (mark[b[r2][i]])
				cnt++, ans = b[r2][i];
		cout << "Case #" << o + 1 << ": ";
		if (cnt == 1)
			cout << ans << endl;
		else if (cnt > 1)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}
	return 0;
}
