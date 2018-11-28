#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int r1;
		cin >> r1;
		vector<vector<int>> d1(4, vector<int>(4, 0));
		for (int r = 0; r < 4; r++) for (int c = 0; c < 4; c++) cin >> d1[r][c];
		int r2;
		cin >> r2;
		vector<vector<int>> d2(4, vector<int>(4, 0));
		for (int r = 0; r < 4; r++) for (int c = 0; c < 4; c++) cin >> d2[r][c];

		vector<int> res;
		r1--;
		r2--;
		for (int c1 = 0; c1 < 4; c1++) for (int c2 = 0; c2 < 4; c2++) if (d1[r1][c1] == d2[r2][c2]) res.push_back(d1[r1][c1]);

		if (res.size() == 1) 
			cout << "Case #" << i << ": " << res[0] << endl;
		else if (res.size() == 0)
			cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
		else
			cout << "Case #" << i << ": " << "Bad magician!" << endl;

	}

	return 0;
}