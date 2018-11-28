#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool check_o(string& str) {
	static string o_winstr[] = {
		"OOOO",
		"OOOT",
		"OOTO",
		"OTOO",
		"TOOO"	
	};

	for(int k = 0; k < 5; ++k) {
		if(str == o_winstr[k])
			return true;
	}

	return false;
}

bool check_x(string& str) {
	static string x_winstr[] = {
		"XXXX",
		"XXXT",
		"XXTX",
		"XTXX",
		"TXXX"
	};

	for(int k = 0; k < 5; ++k) {
		if(str == x_winstr[k])
			return true;
	}

	return false;
}

int main(int argc, char *argv[]) {
	if(argc < 2)
		return -1;

	ifstream dataset(argv[1]);

	int cases = 0;
	dataset >> cases;

	for(int i = 0; i < cases; ++i) {
		bool has_empty = false;
		int result = 0;
		string board[4];

		for(int j = 0; j < 4; ++j) {
			dataset >> board[j];

			if(check_x(board[j]))
				result = 1;
			else if(check_o(board[j]))
				result = 2;

			if(board[j].find('.') != string::npos)
				has_empty = true;
		}

		if(!result) {
			string diag1;
			diag1 += board[0][0];
			diag1 += board[1][1];
			diag1 += board[2][2];
			diag1 += board[3][3];

			string diag2;
			diag2 += board[0][3];
			diag2 += board[1][2];
			diag2 += board[2][1];
			diag2 += board[3][0];

			if(check_x(diag1) || check_x(diag2))
				result = 1;
			else if(check_o(diag1) || check_o(diag2))
				result = 2;
		}

		if(!result) {
			for(int i = 0; i < 4; ++i) {
				string vert;

				vert += board[0][i];
				vert += board[1][i];
				vert += board[2][i];
				vert += board[3][i];

				if(check_x(vert)) {
					result = 1;
					break;
				} else if(check_o(vert)) {
					result = 2;
					break;
				}
			}
		}


		cout << "Case #" << i+1 << ": ";

		switch(result) {
		case 0:
			cout << (has_empty ? "Game has not completed" : "Draw") << endl;
			break;
		case 1:
			cout << "X won" << endl;
			break;
		case 2:
			cout << "O won" << endl;
			break;
		}
	}

	return 0;
}