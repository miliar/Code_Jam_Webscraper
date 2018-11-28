//============================================================================
// Name        : Problem.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

#define FORS(i,s,e) for(int i = int(s); i < int(e); i++)
#define FOR(i,e) FORS(i,0,e)

typedef vector<char> vc;
typedef vector<vc> vvc;

int main() {
	int c;
	cin >> c;
	vvc T(4,vc(4,'.'));

	FOR(i,c){
		FOR(j,4){
			FOR(k,4){
				cin >> T[j][k];
			}
		}

		bool complete = false;
		int cdot = false;

		//along the row
		FOR(m,4){
			int rowX = 0;
			int rowO = 0;
			int cT = 0;
			FOR(n,4){
				if(T[m][n] == '.'){
					cdot++;
					break;
				}
				else if(T[m][n] == 'T'){
					cT++;
				}
				else if((T[m][0] == 'X') && T[m][n] == T[m][0]){
					rowX++;
				}else if((T[m][0] == 'O') && T[m][n] == T[m][0]){
					rowO++;
				}else{
					break;
				}

			}
			if(rowX == 4){
				cout << "Case #"<< i + 1 << ": X won" << endl;
				complete = true;
			}else if(rowO == 4){
				cout << "Case #"<< i + 1 << ": O won" << endl;
				complete = true;
			}
			else if(rowX == 3 && cT == 1){
				cout << "Case #"<< i + 1 << ": X won" << endl;
				complete = true;
			}else if(rowO == 3 && cT == 1){
				cout << "Case #"<< i + 1 << ": O won" << endl;
				complete = true;
			}else{

			}

		}

		if(complete){
			if(i != c - 1)
				continue;
			else
				break;
		}

		//along the column
		FOR(n,4){
			int colX = 0;
			int colO = 0;
			int cT = 0;
			FOR(m,4){
				if(T[m][n] =='.'){
					break;
				}
				else if(T[m][n] == 'T'){
					cT++;
				}
				else if((T[0][n] == 'X') && T[m][n] == T[0][n]){
					colX++;
				}
				else if((T[0][n] == 'O') && T[m][n] == T[0][n]){
					colO++;
				}
				else{
					break;
				}

			}

			if(colX == 4){
				cout << "Case #"<< i + 1 << ": X won" << endl;
				complete = true;
			}else if(colO == 4){
				cout << "Case #"<< i + 1 << ": O won" << endl;
				complete = true;
			}
			else if(colX == 3 && cT == 1){
				cout << "Case #"<< i + 1 << ": X won" << endl;
				complete = true;
			}else if(colO == 3 && cT == 1){
				cout << "Case #"<< i + 1 << ": O won" << endl;
				complete = true;
			}else{
			}
		}

		if(complete){
			if(i != c - 1)
				continue;
			else
				break;
		}

		//along the first diagonals
		int diagX = 0;
		int diagO = 0;
		int cT = 0;
		FOR(m,4){
			if(T[m][m] == '.')
				break;
			else if(T[m][m] == 'T')
				cT++;
			else if(T[0][0] == 'X' && T[m][m] == T[0][0]){
				diagX++;
			}else if(T[0][0] == 'O' && T[m][m] == T[0][0]){
				diagO++;
			}else{
				break;
			}
		}

		if(diagX == 4){
			cout << "Case #"<< i + 1 << ": X won" << endl;
			complete = true;
		}
		else if(diagO == 4){
			cout << "Case #"<< i + 1 << ": O won" << endl;
			complete = true;
		}else if(diagX == 3 && cT == 1){
			cout << "Case #"<< i + 1 << ": X won"<< endl;
			complete = true;
		}else if(diagO == 3 && cT == 1){
			cout << "Case #"<< i + 1 << ": O won"<< endl;
			complete = true;
		}else{
		}

		if(complete){
			if(i != c - 1)
				continue;
			else
				break;
		}

		//along the second diagonal
		diagX = 0;
		diagO = 0;
		cT = 0;
		FOR(m,4){
			if(T[m][3-m] == '.')
				break;
			else if(T[m][3-m] == 'T')
				cT++;
			else if(T[0][3] == 'X' && T[m][3-m] == T[0][3]){
				diagX++;
			}else if(T[0][3] == 'O' && T[m][3-m] == T[0][3]){
				diagO++;
			}else{
				break;
			}
		}

		if(diagX == 4){
			cout << "Case #"<< i + 1 << ": X won" << endl;
			complete = true;
		}
		else if(diagO == 4){
			cout << "Case #"<< i + 1 << ": O won" << endl;
			complete = true;
		}else if(diagX == 3 && cT == 1){
			cout << "Case #"<< i + 1 << ": X won"<< endl;
			complete = true;
		}else if(diagO == 3 && cT == 1){
			cout << "Case #"<< i + 1 << ": O won"<< endl;
			complete = true;
		}else{
		}

		if(complete){
			if(i != c - 1)
				continue;
			else
				break;
		}

		if(cdot > 0){
			cout << "Case #"<< i + 1 << ": Game has not completed" << endl;
		}else{
			cout << "Case #"<< i + 1 << ": Draw" << endl;
		}

	}

	return 0;
}
