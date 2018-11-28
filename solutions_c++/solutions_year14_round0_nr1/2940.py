#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void solve(int N)
{
	int r1;
	cin >> r1;
	r1--;
	vector<vector<int>> d1(4, vector<int>(4, 0));
	for (int y = 0; y < 4; y++) {
		for (int x = 0; x < 4; x++) {
			cin >> d1[y][x];
		}
	}
	int r2;
	cin >> r2;
	r2--;
	vector<vector<int>> d2(4, vector<int>(4, 0));
	for (int y = 0; y < 4; y++) {
		for (int x = 0; x < 4; x++) {
			cin >> d2[y][x];
		}
	}
	vector<int> answers;
	for (int x1 = 0; x1 < 4; x1++) {
		for (int x2 = 0; x2 < 4; x2++) {
			if (d1[r1][x1] == d2[r2][x2]) {
				answers.push_back(d1[r1][x1]);
				break;
			}
		}
	}

	if (answers.size() == 0) {
		cout << "Volunteer cheated!";
	} else if (answers.size() > 1) {
		cout << "Bad magician!";
	} else {
		cout << answers[0];
	}
}

int main(int argc, char* argv[])
{
	if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
		cout << endl;
	}

	return 0;
}