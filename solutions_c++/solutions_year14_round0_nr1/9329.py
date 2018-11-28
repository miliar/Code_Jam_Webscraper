#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <vector>

using namespace std;

string solve(int &first, int &second, int rowsfirst[4][4], int rowsecond[4][4]){
	int amt = 0;
	map<int, int> pairs;
	first -= 1;
	second -= 1;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (rowsecond[second][i] == rowsfirst[first][j])
				pairs[amt++] = rowsfirst[first][j];
		}
	}

	return (amt > 0) ? ((amt != 1) ? "Bad magician!" : to_string(pairs[0])) : "Volunteer cheated!";
}

int main() {
	int N;
	scanf_s("%d", &N);
	const int n = N;
	vector<string> answ;
	for (int i = 0; i < N; i++) {
		int first;
		int rows[4][4];
		scanf_s("%d", &first);
		for (int i = 0; i < 4; i++) {
			cin >> rows[i][0] >> rows[i][1] >> rows[i][2] >> rows[i][3];
		}
		int second;
		int rows2[4][4];
		scanf_s("%d", &second);
		for (int i = 0; i < 4; i++) {
			cin >> rows2[i][0] >> rows2[i][1]>>  rows2[i][2] >> rows2[i][3];
		}

		string ans = "Case #" + to_string(i+1) + ":";
		ans += " " +solve(first, second, rows, rows2);
		answ.push_back(ans);
	}
	for (int i = 0; i < N; i++) cout << answ[i] << endl;
	return 0;
}