// Q1.cpp : 定義主控台應用程式的進入點。
//

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char solve_case(ifstream &ifile, ofstream &ofile) {
	char arr[4*3][4];
	string str;
	char winner = 'N';

	getline(ifile, str);
	for(int i=0;i<4;++i) {
		getline(ifile, str);
		for(int j=0;j<4;++j) {
			if(str[j] == 'T') {
				arr[i][j] = 'X';
				arr[i+4][j] = 'O';
				arr[i+8][j] = 'T';
			} else {
				arr[i][j] = str[j];
				arr[i+4][j] = str[j];
				arr[i+8][j] = '.';
			}
		}
	}
	//for(int qq=0;qq<3;++qq) {
	//	for(int i=0;i<4;++i) {
	//		for(int j=0;j<4;++j) {
	//			if(qq==0) {
	//				cout << arr[i][j];
	//			} else if(qq==1){
	//				cout << arr[i+4][j];
	//			} else {
	//				cout << arr[i+8][j];
	//			}
	//		}
	//		cout << endl;
	//	}
	//	cout << endl;
	//}

	// row X
	for(int i=0;i<4;++i) {
		if((arr[i+8][0] & arr[i+8][1] & arr[i+8][2] & arr[i+8][3]) == 'T') {
			continue;
		}
		if((arr[i][0] & arr[i][1] & arr[i][2] & arr[i][3]) == 'X') {
			winner = 'X';
			break;
		}
	}
	// row O
	for(int i=0;i<4;++i) {
		if((arr[i+8][0] & arr[i+8][1] & arr[i+8][2] & arr[i+8][3]) == 'T') {
			continue;
		}
		if((arr[i+4][0] & arr[i+4][1] & arr[i+4][2] & arr[i+4][3]) == 'O') {
			if(winner == 'X') {
				winner = 'D';
				break;
			}
			winner = 'O';
		}
	}

	if(winner == 'D') {
		return winner;
	}

	// col X
	for(int i=0;i<4;++i) {
		if((arr[8][i] & arr[8][i] & arr[8][i] & arr[8][i]) == 'T') {
			continue;
		}
		if((arr[0][i] & arr[1][i] & arr[2][i] & arr[3][i]) == 'X') {
			if(winner == 'O') {
				winner = 'D';
				break;
			}
			winner = 'X';
		}
	}

	if(winner == 'D') {
		return winner;
	}

	// col O
	for(int i=0;i<4;++i) {
		if((arr[8][i] & arr[8][i] & arr[8][i] & arr[8][i]) == 'T') {
			continue;
		}
		if((arr[4][i] & arr[5][i] & arr[6][i] & arr[7][i]) == 'O') {
			if(winner == 'X') {
				winner = 'D';
				break;
			}
			winner = 'O';
		}
	}

	if(winner == 'D') {
		return winner;
	}

	// cross X
	if((arr[8][0] & arr[9][1] & arr[10][2] & arr[11][3]) != 'T') {
		if((arr[0][0] & arr[1][1] & arr[2][2] & arr[3][3]) == 'X') {
			if(winner == 'O') {
				winner = 'D';
			} else {
				winner = 'X';
			}
		}
	}

	if(winner == 'D') {
		return winner;
	}

	if((arr[11][0] & arr[10][1] & arr[9][2] & arr[8][3]) != 'T') {
		if((arr[3][0] & arr[2][1] & arr[1][2] & arr[0][3]) == 'X') {
			if(winner == 'O') {
				winner = 'D';
			} else {
				winner = 'X';
			}
		}
	}

	if(winner == 'D') {
		return winner;
	}

	// cross O
	if((arr[8][0] & arr[9][1] & arr[10][2] & arr[11][3]) != 'T') {
		if((arr[4][0] & arr[5][1] & arr[6][2] & arr[7][3]) == 'O') {
			if(winner == 'X') {
				winner = 'D';
			} else {
				winner = 'O';
			}
		}
	}

	if(winner == 'D') {
		return winner;
	}

	if((arr[11][0] & arr[10][1] & arr[9][2] & arr[8][3]) != 'T') {
		if((arr[7][0] & arr[6][1] & arr[5][2] & arr[4][3]) == 'O') {
			if(winner == 'X') {
				winner = 'D';
			} else {
				winner = 'O';
			}
		}
	}


	if(winner == 'D') {
		return winner;
	}

	if(winner == 'N') {
		winner = 'D';
		for(int i=0;i<4;++i) {
			for(int j=0;j<4;++j) {
				if(arr[i][j] == '.') {
					winner = 'N';
					goto FINISH;
				}
			}
		}
		FINISH:;
	}
	return winner;
}

int main(int argc, char* argv[])
{
	ifstream ifile("a_in.txt");
	ofstream ofile("a_out.txt");

	int case_num = 0;
	ifile >> case_num;

	for(int i=0;i<case_num;++i) {
		char winner = solve_case(ifile, ofile);
		string winnerStr;
		if(winner == 'X') {
			winnerStr = "X won";
		} else if(winner == 'O') {
			winnerStr = "O won";
		} else if(winner == 'D') {
			winnerStr = "Draw";
		} else {
			winnerStr = "Game has not completed";
		}

		char res[1024] = "";
		sprintf(res, "Case #%d: %s", i+1, winnerStr.c_str());

		cout << res << endl;
		ofile << res << endl;
	}

	system("PAUSE");
	return 0;
}

