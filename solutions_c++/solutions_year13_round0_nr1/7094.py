#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool emptySpaces(int b[4][4]) {
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(b[i][j]==4)
				return true;
	return false;
}

bool xWon(int b[4][4]) {
	//Check Rows
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(!(b[i][j]==1 || b[i][j]==3))
				break;
			if(j==3)
				return true;
		}
	}
	//Check Columns
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(!(b[j][i]==1 || b[j][i]==3))
				break;
			if(j==3)
				return true;
		}
	}
	//Check Diagonals
	for(int i=0; i<4; i++) {
		if(!(b[i][i]==1 || b[i][i]==3))
			break;
		if(i==3)
			return true;
	}
	for(int i=0; i<4; i++) {
		if(!(b[i][3-i]==1 || b[i][3-i]==3))
			break;
		if(i==3)
			return true;
	}
	return false;
}

bool oWon(int b[4][4]) {
	//Check Rows
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(!(b[i][j]==2 || b[i][j]==3))
				break;
			if(j==3)
				return true;
		}
	}
	//Check Columns
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(!(b[j][i]==2 || b[j][i]==3))
				break;
			if(j==3)
				return true;
		}
	}
	//Check Diagonals
	for(int i=0; i<4; i++) {
		if(!(b[i][i]==2 || b[i][i]==3))
			break;
		if(i==3)
			return true;
	}
	for(int i=0; i<4; i++) {
		if(!(b[i][3-i]==2 || b[i][3-i]==3))
			break;
		if(i==3)
			return true;
	}
	return false;
}

int main() {
    ofstream fout ("Tic-Tac-Toe-Tomek.out");
    ifstream fin ("Tic-Tac-Toe-Tomek.in");

    int numCases;
    fin >> numCases;

    for(int i=0; i<numCases; i++) {
    	int board[4][4];
    	char c;
    	for(int j=0; j<4; j++) {
    		for(int k=0; k<4; k++) {
    			fin >> c;
    			int entry;
    			if(c=='X')
    				entry=1;
    			else if(c=='O')
    				entry=2;
    			else if(c=='T')
    				entry=3;
    			else if(c=='.')
    				entry=4;
    			board[j][k]=entry;
    		}
    	}

    	if(xWon(board))
    		fout << "Case #" << i+1 << ": X won\n";
    	else if(oWon(board))
    		fout << "Case #" << i+1 << ": O won\n";
    	else if(emptySpaces(board))
    		fout << "Case #" << i+1 << ": Game has not completed\n";
    	else
    		fout << "Case #" << i+1 << ": Draw\n";

    }

    return 0;
}
