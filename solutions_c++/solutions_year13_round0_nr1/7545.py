#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
using namespace std;

char check(vector<string> board) {
	// 行
	for (int i = 0; i < 4; i++) {
		char c = board[i][0] == 'T' ? board[i][0] : board[i][1];
		int flag = 0;

		if (c == '.') continue;
		for (int j = 0; j < 4; j++) {
			if (board[i][j] != 'T' && board[i][j] != c) {
				flag = 1;
				break;
			}
		}
		if (flag == 0) return c;
	}

	// 列
	for (int i = 0; i < 4; i++) {
		char c = board[0][i] == 'T' ? board[0][i] : board[1][i];
		int flag = 0;

		if (c == '.') continue;
		for (int j = 0; j < 4; j++) {
			if (board[j][i] != c) {
				flag = 1;
				break;
			}
		}
		if (flag == 0) return c;
	}


	// 斜め：２か所だけ
	char c = board[0][0] == 'T' ? board[0][0] : board[1][1];
	int flag = 0;

	for (int i = 0; i < 1; i++) {
		if (c == '.') break;
		for (int j = 0; j < 4; j++) {
			if (board[j][j] != 'T' && board[j][j] != c) {
				flag = 1;
				break;
			}
		}
		if (flag == 0) return c;
	}

	c = board[0][3] == 'T' ? board[0][3] : board[1][2];
	flag = 0;

	for (int i = 0; i < 1; i++) {
		if (c == '.') break;
		for (int j = 0; j < 4; j++) {
			if (board[j][3-j] != 'T' && board[j][3-j] != c) {
				flag = 1;
				break;
			}
		}
		if (flag == 0) return c;
	}


	// この時点で勝者無なので、not completedかどうかチェック
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == '.') return 'n';
		}
	}

	return 'd';
}
string IntToString(int number)
{
  stringstream ss;
  ss << number;
  return ss.str();
}
int main(void)
{
	ifstream cin("A-small-attempt0.in");
	ofstream ofs("A-small-attempt0.out");

	int T = 0;
	cin >> T;
	cin.ignore();
	for (int i = 0; i < T; i++) {
		vector<string> board;
		board.clear();

		// 盤面読み込み
		for (int j = 0; j < 4; j++) {
			string buf;
			getline(cin, buf);
			
			board.push_back(buf);
		}

		// 分析
		char r = check(board);
		string out;
		switch (r) {
			case 'X':
				out = "X won";
				break;
			case 'O':
				out = "O won";
				break;
			case 'n':
				out = "Game has not completed";
				break;
			case 'd':
				out = "Draw";
				break;
		}

		//cout << out << endl;
		ofs << "Case #" << i+1 << ": " << out << endl;
		cin.ignore();
	}

	

	return 0;
}