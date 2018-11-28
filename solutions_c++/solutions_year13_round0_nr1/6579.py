#include <iostream>
#include <vector>
#include <fstream>

void setBoard (std::vector<std::string>& board) {
	for (int i = 0; i < board.size(); i++) {
		std::string tmp;
		std::cin >> tmp;
		board[i] = tmp;
	}
}

bool draw (const std::vector<std::string>& board) {
	bool flag = true;

	for (int i = 0; i < board.size(); i++) {
	int countX = 0;
	int countO = 0;
		for (int j = 0; j < board[i].size(); j++) {
			if (board[i][j] == 'X' || board[i][j] == 'T') countX++;
			if (board[i][j] == 'O' || board[i][j] == 'T') countO++;
		}
		if (countX == 4 || countO == 4) flag = false;
 
	}

	for (int i = 0; i < board.size(); i++) {
	int countX = 0;
	int countO = 0;
		for (int j = 0; j < board[i].size(); j++) {
			if (board[j][i] == 'X' || board[j][i] == 'T') countX++;
			if (board[j][i] == 'O' || board[j][i] == 'T') countO++;
		}
		if (countX == 4 || countO == 4) flag = false;
 
	}

	int countX = 0;
	int countO = 0;
	for (int i = 0,j=0; i < 4 && j < 4; i++,j++) {
		if (board[i][j] == 'X' || board[i][j] == 'T') countX++;
		if (board[i][j] == 'O' || board[i][j] == 'T') countO++;
	}
	if (countX == 4 || countO == 4) flag = false;

	countX = 0;
	countO = 0;
	for (int i = 0,j=3; i < 4 && j >=0; i++,j--) {
		if (board[i][j] == 'X' || board[i][j] == 'T') countX++;
		if (board[i][j] == 'O' || board[i][j] == 'T') countO++;
	}
	if (countX == 4 || countO == 4) flag = false;

	for (int i = 0; i < board.size(); i++) {
		for (int j = 0; j < board[i].size(); j++) {
			if (board[i][j] == '.') flag = false;
		}
	}

	return flag;
}

bool complete (const std::vector<std::string>& board) {
	bool flag = false;
	int count = 0;
	int tmp_count = 0;
	for (int i = 0; i < board.size(); i++) {	
		for (int j = 0; j < board[i].size(); j++) {
			if (board[i][j] != '.') tmp_count++;
		}
		if (count < tmp_count) count = tmp_count;
		tmp_count = 0;
	}
	if (count == 4) flag = true;

	int countX = 0;
	int countO = 0;
	for (int i = 0,j = 0; i < board.size() && j < 4; i++,j++) {
		if (board[i][j] == 'X' || board[i][j] == 'T') { countX++;}
		if (board[i][j] == 'O' || board[i][j] == 'T') { countO++;}
	}
	if (countX < 4 || countO < 4) flag = true;

	countX = 0;
	countO = 0;
	for (int i = 0,j = 3; i < 4 && j >= 0; i++,j--) {
		if (board[i][j] == 'X' || board[i][j] == 'T') { countX++; }
		if (board[i][j] == 'O' || board[i][j] == 'T') { countO++; }
	}
	if (countX < 4 || countO < 4) flag = true;
	return flag;
}

bool doIt (const std::vector<std::string>& board,char var) {
	bool flag = false;
	int countX = 0;
	int countO = 0;
	for (int i = 0; i < board.size(); i++) {
	countX = 0;
	countO = 0;
		for (int j = 0; j < board[i].size(); j++) {
			if (board[i][j] == var || board[i][j] == 'T') { if (var == 'X') countX++; }
			if (board[i][j] == var || board[i][j] == 'T') { if (var == 'O') countO++; }
		}
		if (var == 'X' && countX == 4) flag = true;
		else if (var == 'O' && countO == 4) flag = true;
	}

	countX = 0;
	countO = 0;
	for (int i = 0; i < board.size(); i++) {
	countX = 0;
	countO = 0;
		for (int j = 0; j < board[i].size(); j++) {
			if (board[j][i] == var || board[j][i] == 'T') { if (var == 'X') countX++; }
			if (board[j][i] == var || board[j][i] == 'T') { if (var == 'O') countO++; }
		}
		if (var == 'X' && countX == 4) flag = true;
		else if (var == 'O' && countO == 4) flag = true;
	}

	countX = 0;
	countO = 0;
	for (int i = 0,j = 0; i < board.size() && j < 4; i++,j++) {
		if (board[i][j] == var || board[i][j] == 'T') { if (var == 'X') countX++;}
		if (board[i][j] == var || board[i][j] == 'T') { if (var == 'O') countO++;}
	}
	if (var == 'X' && countX == 4) flag = true;
	else if (var == 'O' && countO == 4) flag = true;

	countX = 0;
	countO = 0;
	for (int i = 0,j = 3; i < 4 && j >= 0; i++,j--) {
		if (board[i][j] == var || board[i][j] == 'T') { if (var == 'X') countX++; }
		if (board[i][j] == var || board[i][j] == 'T') { if (var == 'O') countO++; }
	}
	if (var == 'X' && countX == 4) flag = true;
	else if (var == 'O' && countO == 4) flag = true;
	
	return flag;
}

int main () {
	std::vector<std::string> board(4);
	int T = 0;
	int q = 0;
	std::cin >> T;
	while (q < T) {	
		setBoard(board);
		if (doIt(board,'X')) {
			std::cout << "Case #" << q+1 << ": X won" << std::endl;
		}
		else if (doIt(board,'O')) {
			std::cout << "Case #" << q+1 << ": O won" << std::endl;
		}
		/*else if (complete(board)) {
			std::cout << "Case #" << q+1 << ": Game has not completed" << std::endl;
		}*/
                else if (draw(board)) {
			std::cout << "Case #" << q+1 << ": Draw" << std::endl;
		}
		else {
			std::cout << "Case #" << q+1 << ": Game has not completed" << std::endl;
		}
		q++;
	}
}
