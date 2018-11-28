#include <iostream>

using namespace std;

int main() {
	int T;
	int cards[4][4];
	int mask;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int s1, s2;
		mask = 0;
		cin >> s1;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
			cin >> cards[i][j];
		for (int i = 0; i < 4; i++)
			mask |= 1 << cards[s1-1][i];
		cin >> s2;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++)
			cin >> cards[i][j];
		int occ = 0;
		int num;
		for (int i = 0; i < 4; i++)
			if (mask & (1<<cards[s2-1][i])) {
				occ++;
				num = cards[s2-1][i];
			}
		if (occ == 0)
			cout << "Case #" << t << ": Volunteer cheated!" << endl;
		else if (occ == 1)
			cout << "Case #" << t << ": " << num << endl;
		else
			cout << "Case #" << t << ": Bad magician!" << endl;
	}
	return 0;
}
