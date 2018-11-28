#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <list>
#include <map>
#include <math.h>

using namespace std;

int
outcome (char *board, int *Dot)
{
	int X=0;
	int O=0;
	int T=0;
	int dot=0;

	for (int i = 0 ; i < 4; i++) {
		if (board[i] == 'X') {
		    X++;
		} else if (board[i] == 'O') {
		    O++;
		} else if (board[i] == 'T') {
		    T++;
		} else {
		   dot++;
		}
	}

	*Dot = dot;

	if (X >= 3 && O <= 0 && dot <= 0) {
		//return "X won";
		return 1;
	} else if (O >= 3 && X <= 0 && dot <= 0) {
		//return "O won";
		return 2;
	} else if (dot == 0) {
		//return "Draw";
		return 3;
	} else {
		//return "Game has not completed";
		return 4;
	}
	
}

const char *
tic_tac_toe_tomek (char **board)
{
	char array[4];
	int res = 0;
	int dot=0,d;

	/* horizontal */
	for (int i = 0; i < 4; i++) {
	     memcpy(array, board[i], 4);
		res = outcome(array, &d);
		if (res == 1) {
		    return "X won";
		} else if (res == 2) {
		    return "O won";
		}
		dot += d;
	}

	/* vertical */
	for (int i = 0; i < 4; i++) {
	     array[0] = board[0][i];
	     array[1] = board[1][i];
	     array[2] = board[2][i];
	     array[3] = board[3][i];

		res = outcome(array, &d);
		if (res == 1) {
		    return "X won";
		} else if (res == 2) {
		    return "O won";
		}
		dot += d;
	}

	/* diagonals */
     for (int i = 0; i < 4; i++) {
	     array[i] = board[i][i];
		res = outcome(array, &d);
		if (res == 1) {
		    return "X won";
		} else if (res == 2) {
		    return "O won";
		}
		dot += d;
	}

     for (int i = 0; i < 4; i++) {
	     array[i] = board[3-i][i];
		res = outcome(array, &d);
		if (res == 1) {
		    return "X won";
		} else if (res == 2) {
		    return "O won";
		}
		dot += d;
	}


	if (dot == 0) {
	    return "Draw";
	}
	return "Game has not completed";
}

int main(int argc, char **argv) {
	int case_num = 1;
	string str;
	bool first = 0;
	int total_cases;
	unsigned int TC_num = 0;
	unsigned int line = 0;
	char a,b,c,d;
	int row = 0;
	char **board;
	
	board = (char **)malloc(4*sizeof(int *));
	for (int i = 0; i < 4; i++) {
		board[i] = (char *)malloc(sizeof(char)*4);
	}
	
	ifstream read_file (argv[1]);

	if (read_file.is_open()) {
	    while (getline(read_file, str)) {
			 if (!first) {
				 total_cases = atoi(str.c_str());
				 first = 1;
			 } else {
		           line++;
				 if (line % 5 == 0) {
					row = 0;
				     cout << "Case #" << ++TC_num <<": "<< tic_tac_toe_tomek (board) << endl;
					continue;
				 }
				 stringstream ss(str);
				 ss >> a >> b >> c >> d;
				 //cout << "line: " << line << " " << a << " " << b << " " << c << " " << d << endl;
				 board[row][0] = a;
				 board[row][1] = b;
				 board[row][2] = c;
				 board[row][3] = d;

				 if (line == total_cases*5-1) {
				     cout << "Case #" << ++TC_num <<": "<< tic_tac_toe_tomek (board) << endl;
				 }
				 row++;
			 }
	    }
	    read_file.close();
	}

     for (int i = 0; i < 4; i++) {
		free(board[i]);
	}
	free(board);
}
