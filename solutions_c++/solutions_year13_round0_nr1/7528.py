#include <iostream>
#include <string>
#include <algorithm>
#include <stdexcept>
using namespace std;

inline void check(const char c, int &O, int &X, int &T, int &dots)
{
	switch (c) {
		case 'O': O++; break;
		case 'X': X++; break;
		case 'T': T++; break;
		case '.': dots++; break;
		default: throw std::runtime_error("incorrect character");
	}
}

inline string check2(int O, int X, int T)
{
	if ((O == 3 && T == 1) || O == 4)
		return "O won";
	if ((X == 3 && T == 1) || X == 4)
		return "X won";
	
	return "";
}

int main()
{
	int T;

	cin >> T;

	for (int case_nr=1; case_nr <= T; case_nr++) {
		string board[4];

		for (int i=0; i<4; i++)
			cin >> board[i];

		cout << "Case #" << case_nr << ": ";

		string result;

		int dots = 0;
		for (int i=0; i<4; i++) {
			int O = 0, X = 0, T = 0;
			for (int j=0; j<4; j++) {
				check(board[i][j], O, X, T, dots);
			}

			if (result.empty()) result = check2(O, X, T);
		}

		for (int j=0; j<4; j++) {
			int O = 0, X = 0, T = 0;
			for (int i=0; i<4; i++) {
				check(board[i][j], O, X, T, dots);
			}

			if (result.empty()) result = check2(O, X, T);
		}

		{
			int O = 0, X = 0, T = 0;
			for (int i=0; i<4; i++) {
				check(board[i][i], O, X, T, dots);
			}

			if (result.empty()) result = check2(O, X, T);
		}

		{
			int O = 0, X = 0, T = 0;
			for (int i=0; i<4; i++) {
				check(board[i][3-i], O, X, T, dots);
			}

			if (result.empty()) result = check2(O, X, T);
		}


		if (result.empty()) {
			if (dots == 0)
				result = "Draw";
			else
				result = "Game has not completed";
		}

		cout << result << endl;
	}
}
