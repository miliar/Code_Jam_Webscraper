#include "board.h"
#include <string> 
#include <iostream>
#include <fstream> 
using namespace std; 

Board::Board(void){
	for (int i = 0; i < 4; i++) { 
		for( int j = 0; j < 4; j++) {
			lattice[i][j] = 0; 
		}
	}
}

void Board::fillRow(int rowInd, string con) {
	for (int i = 0; i < 4; i++) { 
		lattice[rowInd][i] = convert_string(i,con);
	}
}

void Board::print(void) { 
	for (int i = 0; i < 4; i++) { 
		for (int j = 0; j < 4; j++) { 
			cout << lattice[i][j] << '\t';
		}
		cout << endl; 
	}
}

int Board::considerRow(int index) {
	int xscore = 0; 
	int oscore = 0;
	int value = 0; 
	for(int i = 0; i < 4; i++) { 
		switch (lattice[index][i]) { 
		case 0:
			break;
		case 1:
			xscore++;
			break;
		case 2: 
			oscore++;
			break;
		case 3:
			xscore++; 
			oscore++;
			break;
		default: 
			cout << "WTF CONSIDERROW" << endl; 
			break;
		}
	}
	if(xscore == 4) { 
		value = 1; 
	}
	else if(oscore == 4) { 
		value = 2; 
	}
	return value; 
}

int Board::considerColumn(int index){
	int xscore = 0; 
	int oscore = 0;
	int value = 0; 
	for(int i = 0; i < 4; i++) { 
		switch (lattice[i][index]) { 
		case 0:
			break;
		case 1:
			xscore++;
			break;
		case 2: 
			oscore++;
			break;
		case 3:
			xscore++; 
			oscore++;
			break;
		default: 
			cout << "WTF CONSIDERCOL" << endl; 
			break;
		}
	}
	if(xscore == 4) { 
		value = 1; 
	}
	else if(oscore == 4) { 
		value = 2; 
	}
	return value; 
}

int Board::considerDiagonalA(void){
	int xscore = 0; 
	int oscore = 0;
	int value = 0; 
	for(int i = 0; i < 4; i++) { 
		switch (lattice[i][i]) { 
		case 0:
			break;
		case 1:
			xscore++;
			break;
		case 2: 
			oscore++;
			break;
		case 3:
			xscore++; 
			oscore++;
			break;
		default: 
			cout << "WTF CONSIDERA" << endl; 
			break;
		}
	}
	if(xscore == 4) { 
		value = 1; 
	}
	else if(oscore == 4) { 
		value = 2; 
	}
	return value; 
}
int Board::considerDiagonalB(void){
	int xscore = 0; 
	int oscore = 0;
	int value = 0; 
	for(int i = 0; i < 4; i++) { 
		switch (lattice[i][3-i]) { 
		case 0:
			break;
		case 1:
			xscore++;
			break;
		case 2: 
			oscore++;
			break;
		case 3:
			xscore++; 
			oscore++;
			break;
		default: 
			cout << "WTF CONSIDERB" << endl; 
			break;
		}
	}
	if(xscore == 4) { 
		value = 1; 
	}
	else if(oscore == 4) { 
		value = 2; 
	}
	return value; 
}

int Board::consider(void) { 
	for(int i = 0; i < 4; i++) { 
		if(considerRow(i) == 1) { 
			return 1; 
		}
		if(considerRow(i) == 2) {
			return 2;
		}
		if(considerColumn(i) == 1) { 
			return 1; 
		}
		if(considerColumn(i) == 2) {
			return 2; 
		}
	}
	if(considerDiagonalA() == 1) {
		return 1; 
	}
	if(considerDiagonalA() == 2) { 
		return 2; 
	}
	if(considerDiagonalB() == 1) { 
		return 1; 
	}
	if(considerDiagonalB() == 2) { 
		return 2; 
	}
	int noDot = 0;
	for(int i = 0; i < 4; i++) { 
		for(int j = 0; j < 4; j++) { 
			if(lattice[i][j] == 0) { 
				noDot++; 
			}
		}
	}
	if(noDot == 0) { 
		return 3; 
	}
	return 4;
}
string Board::printstate(void) { 
	string value = ""; 
	switch(consider()) { 
	case 1: 
		value = "X won"; 
		break;
	case 2:
		value = "O won";
		break; 
	case 3: 
		value = "Draw";
		break;
	case 4:
		value = "Game has not completed";
		break; 
	default:
		cout << "WTF PRINT STATE" << endl; 
		break; 
	}
	return value;
}

int convert_string(int index, string con) { 
	char x = con.at(index);
	int value; 
	switch (x) {
	case '.':
		value = 0; 
		break; 
	case 'X': 
		value = 1; 
		break; 
	case 'O': 
		value = 2; 
		break; 
	case 'T':
		value = 3;
		break; 
	default: 
		cout << "WTF ERROR IN STRING CONVERSION" << endl; 
		value = 999; 
		break;
	}
	return value; 
}
