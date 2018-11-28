#include<iostream>
#include<fstream>
#include<string>

using namespace std;

bool symOrT (char player_symbol, char board_symbol) {
	return board_symbol == player_symbol || board_symbol == 'T';
}

int main() {
	ifstream input_file;
	ofstream output_file;
	//string file_name;
	int cases = 0;
	char board[16];
	bool found_winner = false;
	bool completed = true;

	//cout << "Input file location:" << endl;
	//getline(cin, file_name);

	//input_file.open(file_name);
	input_file.open("D:\\Lysander\\input.txt");
	output_file.open("out.txt");

	if (input_file.is_open()) {
		input_file >> cases;
		for (int i = 1; i <= cases; ++i) {
			found_winner = false;
			completed = true;

			for (int j = 0; j < 16; ++j)
				input_file >> board[j];

			for (int j = 0; j < 16; ++j) {
				if (board[j] == '.') {
					completed = false;
					break;
				}
			}

			for (int j = 0; j < 10; ++j) {
				if (
					(symOrT('X', board[0]) && symOrT('X', board[1]) && symOrT('X', board[2]) && symOrT('X', board[3])) ||
					(symOrT('X', board[4]) && symOrT('X', board[5]) && symOrT('X', board[6]) && symOrT('X', board[7])) ||
					(symOrT('X', board[8]) && symOrT('X', board[9]) && symOrT('X', board[10]) && symOrT('X', board[11])) ||
					(symOrT('X', board[12]) && symOrT('X', board[13]) && symOrT('X', board[14]) && symOrT('X', board[15])) ||
					(symOrT('X', board[0]) && symOrT('X', board[4]) && symOrT('X', board[8]) && symOrT('X', board[12])) ||
					(symOrT('X', board[1]) && symOrT('X', board[5]) && symOrT('X', board[9]) && symOrT('X', board[13])) ||
					(symOrT('X', board[2]) && symOrT('X', board[6]) && symOrT('X', board[10]) && symOrT('X', board[14])) ||
					(symOrT('X', board[3]) && symOrT('X', board[7]) && symOrT('X', board[11]) && symOrT('X', board[15])) ||
					(symOrT('X', board[0]) && symOrT('X', board[5]) && symOrT('X', board[10]) && symOrT('X', board[15])) ||
					(symOrT('X', board[3]) && symOrT('X', board[6]) && symOrT('X', board[9]) && symOrT('X', board[12]))
					) {
						output_file << "Case #" << i << ": X won" << endl;
						found_winner = true;
						break;
				}

				if (
					(symOrT('O', board[0]) && symOrT('O', board[1]) && symOrT('O', board[2]) && symOrT('O', board[3])) ||
					(symOrT('O', board[4]) && symOrT('O', board[5]) && symOrT('O', board[6]) && symOrT('O', board[7])) ||
					(symOrT('O', board[8]) && symOrT('O', board[9]) && symOrT('O', board[10]) && symOrT('O', board[11])) ||
					(symOrT('O', board[12]) && symOrT('O', board[13]) && symOrT('O', board[14]) && symOrT('O', board[15])) ||
					(symOrT('O', board[0]) && symOrT('O', board[4]) && symOrT('O', board[8]) && symOrT('O', board[12])) ||
					(symOrT('O', board[1]) && symOrT('O', board[5]) && symOrT('O', board[9]) && symOrT('O', board[13])) ||
					(symOrT('O', board[2]) && symOrT('O', board[6]) && symOrT('O', board[10]) && symOrT('O', board[14])) ||
					(symOrT('O', board[3]) && symOrT('O', board[7]) && symOrT('O', board[11]) && symOrT('O', board[15])) ||
					(symOrT('O', board[0]) && symOrT('O', board[5]) && symOrT('O', board[10]) && symOrT('O', board[15])) ||
					(symOrT('O', board[3]) && symOrT('O', board[6]) && symOrT('O', board[9]) && symOrT('O', board[12]))
					) {
						output_file << "Case #" << i << ": O won" << endl;
						found_winner = true;
						break;
				}
			}

			if (found_winner) continue;

			if (!completed) {
				output_file << "Case #" << i << ": Game has not completed" << endl;
			} else {
				output_file << "Case #" << i << ": Draw" << endl;
			}
		}
	}

	input_file.close();
	output_file.close();
	return 0;
}