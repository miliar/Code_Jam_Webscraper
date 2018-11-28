#include<iostream>
#define NUMCOLS 4
#define NUMROWS 4

using namespace std;

char curr[4];
char board[NUMROWS][NUMCOLS];

// Returns:
// 0 if O won with this quartet
// 1 if X won with this quartet
// 2 if neither did
int checkCurr() {
	for (int i = 0; i < 4; i++) {
		//cerr<<curr[i];
		if (curr[i] == '.') {
			//cerr<<endl;
			return 2;
		}
		//cerr<<endl;
	}
	char last = 'T';
	for (int i = 0; i < 4; i++) {
		//cerr<<"curr[i]="<<curr[i]<<" ";
		//cerr<<"last="<<last<<" ";
		if (curr[i] == 'T') {
			//cerr<<"T\n";
			continue;
		}
		if (curr[i] == last || last == 'T') {
			last = curr[i];
			//cerr<<"cont with last="<<last<<endl;
		}
		else {
			//cerr<<"conflict\n";
			return 2;
		}
	}
	if (last == 'O') {
		//cerr<<"O won!\n";
		return 0;
	}
	//cerr<<"X won!\n";
	return 1;
}

// Returns:
// 0 if O won
// 1 if X won
// 2 if neither won with these lines
int checkCols() {
	int temp;
	for (int c = 0; c < NUMCOLS; c++) {
		for (int r = 0; r < NUMROWS; r++) {
			curr[r] = board[r][c];
		}
		//cerr<<"Checking col "<<c<<" "<<curr[0]<<curr[1]<<curr[2]<<curr[3]<<":\n";
		temp = checkCurr();
		//cerr<<endl;
		if (temp != 2)
			return temp;
	}
	return 2;
}

int checkRows() {
	int temp;
	for (int r = 0; r < NUMROWS; r++) {
		for (int c = 0; c < NUMCOLS; c++) {
			curr[c] = board[r][c];
		}
		//cerr<<"Checking row "<<r<<" "<<curr[0]<<curr[1]<<curr[2]<<curr[3]<<":\n";
		temp = checkCurr();
		//cerr<<endl;
		if (temp != 2)
			return temp;
	}
	return 2;
}

int checkDiags() {
	int temp;
	for (int i = 0; i < NUMROWS; i++)
		curr[i] = board[i][i];
	//cerr<<"Checking diag 1 "<<curr[0]<<curr[1]<<curr[2]<<curr[3]<<":\n";
	temp = checkCurr();
	//cerr<<endl;
	if (temp != 2)
		return temp;
	for (int i = 0; i < NUMCOLS; i++)
		curr[i] = board[i][NUMCOLS - 1 - i];
	//cerr<<"Checking diag 2 "<<curr[0]<<curr[1]<<curr[2]<<curr[3]<<":\n";
	temp = checkCurr();
	//cerr<<endl;
	if (temp != 2)
		return temp;
	return 2;
}

int checkAll() {
	int temp;
	for (int i = 0; i < 3; i++) {
		switch (i) {
			case 0:
				temp = checkCols();
				break;
			case 1:
				temp = checkRows();
				break;
			case 2:
				temp = checkDiags();
				break;
			default:
				break;
				//cerr<<"Shit, there's  problem here";
		}
		if (temp != 2)
			return temp;
	}
	return 2;
}

bool isBoardFull() {
	for (int r = 0; r < NUMROWS; r++) {
		for (int c = 0; c < NUMCOLS; c++) {
			if (board[r][c] == '.')
				return false;
		}
	}
	return true;
}

void getBoard() {
	char temp;
	for (int r = 0; r < NUMROWS; r++) {
		for (int c = 0; c < NUMCOLS; c++) {
			cin>>temp;
			board[r][c] = temp;
			//cerr<<"Got "<<temp<<endl;
		}
	}
}

void printBoard() {
	for (int r = 0; r < NUMROWS; r++) {
		for (int c = 0; c < NUMCOLS; c++) {
			cout<<board[r][c];
		}
		cout<<endl;
	}
	cout<<endl;
}

int main() {
	int n, temp, ntot;
	cin>>ntot;
	n = ntot;
	while (n--) {
		getBoard();
		//printBoard();
		temp = checkAll();
		cout << "Case #" << ntot - n << ": ";
		switch (temp) {
			case 0:
				cout << "O won\n";
				break;
			case 1:
				cout << "X won\n";
				break;
			case 2:
				if (isBoardFull())
					cout<<"Draw\n";
				else
					cout<<"Game has not completed\n";
				break;
			default:
				break;
				//cerr<<"Shit just hit the fan!";
		}
	}
	return 0;
}
