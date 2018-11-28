#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool oWin, xWin, notFinished;

void check(string s) {
	char ch = s[0] != 'T' ? s[0] : s[1];
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] != ch && s[i] != 'T')
			return;
	}
	if (ch == 'O') oWin = true;
	if (ch == 'X') xWin = true;
}

int main() {
	int N;
	cin >> N;
	for (int t = 0; t < N; ++t) {
		oWin = xWin = notFinished = false;
		vector<string> a;
		a.resize(4);
		cin >> a[0] >> a[1] >> a[2] >> a[3];
		string d1 = "", d2 = "";
		for (int i = 0; i < 4; ++i) d1 += a[i][i], d2 += a[i][3-i];
		check(d1);
		check(d2);
		for (int i = 0; i < 4; ++i) {
			check(a[i]);
			string s = "";
			for (int j = 0; j < 4; ++j) {
				s += a[j][i];
				if (a[j][i] == '.') {
					notFinished = true;
				}
			}
			check(s);
		}
		cout << "Case #" << t+1 << ": ";
		if (xWin && !oWin) {
			cout << "X won" << endl;
		} else if (oWin && !xWin) {
			cout << "O won" << endl;
		} else if (oWin && xWin) {
			cout << "Draw" << endl;
		} else if (notFinished) {
			cout << "Game has not completed" << endl;
		} else {
			cout << "Draw" << endl;
		}
	}
	return 0;
}