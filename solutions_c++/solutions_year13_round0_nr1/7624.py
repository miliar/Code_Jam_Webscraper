#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <map>

using namespace std;
int main(int argc, char *argv[]) {
	ifstream indata ("A-small-attempt0.in");
	ofstream outdata ("A-small-attempt0.out");
	string line;
	int t;
	
	const string x_won = "X won";
	const string o_won = "O won";
	
	if (indata.is_open()) {
		getline (indata, line);
		istringstream(line) >> t;
			
		for (int i=0; i<t; i++) {
			if (i > 0) {
				getline (indata, line);
			}
			string outcome;
			int board[4][4];
			bool full = true;
			bool won = false;
			int who = 0;
			
			for (int j=0; j<4; j++) {
				getline (indata, line);
				
				if (won) continue;
				
				map<int, int> this_line;
									
				this_line[-1] = 0;
				this_line[0] = 0;
				this_line[1] = 0;	
				
				for (int k=0; k<4; k++) {
					switch (line[k]) {
						case 'O':
							board[j][k] = -1;
							this_line[board[j][k]]++;
							break;
						case 'X':
							board[j][k] = 1;
							this_line[board[j][k]]++;
							break;
						case 'T':
							board[j][k] = 0;
							this_line[board[j][k]]++;
							break;
						case '.':
							board[j][k] = 1000;
							this_line[board[j][k]]++;
							full = false;
							break;
					}
				}
				
				cout << this_line[0] << this_line[1] << this_line[2] << endl;
				
				if ((this_line[0]+this_line[-1]) == 4) {
					won = true;
					who = -1;
					full = false;
					cout << "Single line win" << endl;
				} else if ((this_line[0]+this_line[1]) == 4) {
					won = true;
					who = 1;
					full = false;
					cout << "Single line win" << endl;
				}
			}
			
			if (full) {
				outcome = "Draw";
			} else if (won) {
				if (who == -1) {
					outcome = o_won;
				} else {
					outcome = x_won;
				}
			} else {
				// Down
				for (int j=0; j<4; j++) {
					map<int, int> this_line;
					
					this_line[-1] = 0;
					this_line[0] = 0;
					this_line[1] = 0;					
					for (int k=0; k<4; k++) {
						this_line[board[k][j]]++;
					}
					
					if ((this_line[0]+this_line[-1]) == 4) {
						won = true;
						who = -1;
						full = false;
						cout << "Single down win" << endl;
						break;
					} else if ((this_line[0]+this_line[1]) == 4) {
						won = true;
						who = 1;
						full = false;
						cout << "Single down win" << endl;
						break;
					}
				}
				// Diagonal
				if (!won) {
					map<int, int> d1, d2;
					for (int j=0; j<4; j++) {
						d1[board[j][j]]++;
						d2[board[j][abs(3-j)]]++;
					}
					
					if ((d1[0]+d1[-1]) == 4 || (d2[0]+d2[-1]) == 4) {
						won = true;
						who = -1;
						full = false;
						cout << "Single diagonal win" << endl;
					} else if ((d1[0]+d1[1]) == 4 || (d2[0]+d2[1]) == 4) {
						won = true;
						who = 1;
						full = false;
						cout << "Single diagonal win" << endl;					}
				}
				
				if (who == -1) {
					outcome = o_won;
				} else if (who == 1) {
					outcome = x_won;
				} else {
					outcome = "Game has not completed";
				}
			}
			
			outdata << "Case #" << i+1 << ": " << outcome << endl;
			cout << "Case #" << i+1 << ": " << outcome << endl;
		}
		
		outdata.close();
		indata.close();
	} else {
		cout << "File not found :( " << endl;
	}
}