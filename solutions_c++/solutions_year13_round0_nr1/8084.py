//============================================================================
// Name        : Problem1_2013.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
bool checkRow(char array[4][4], char check);
bool checkCol(char array[4][4], char check);
bool checkDiagonal(char array[4][4], char check);

int main() {
	int DataSet;
	char breakLine[10];
	char status[4][4];
	bool player1, player2, complete;

	cin >> DataSet;

	for(int i = 0; i < DataSet; i++) {
		complete = true;
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++)
			{
				cin >> status[j][k];
				if(status[j][k] == '.')
					complete = false;
			}
		}

		player1 = player2 = false;
		if((checkRow(status, 'X')) || (checkCol(status, 'X')) ||(checkDiagonal(status, 'X')))
			player1 = true;

		if((checkRow(status, 'O')) || (checkCol(status, 'O')) ||(checkDiagonal(status, 'O')))
			player2 = true;

		cout << "Case #" << (i + 1) << ": ";
		if(player1 == true)
			cout << "X won\n";
		else if(player2 == true)
			cout << "O won\n";
		else if(complete == true)
			cout << "Draw\n";
		else
			cout << "Game has not completed\n";

//		if(i < (DataSet - 1))
//			cin >> breakLine;
	}
	return 0;
}

bool checkRow(char array[4][4], char check){
	int count;
	bool checkSepecial = false;
	for(int i = 0; i < 4; i++) {
		count = 0;
		checkSepecial = false;
		for(int j = 0; j < 4; j++) {
			if(array[i][j] == check)
				count++;
			else if(array[i][j] == 'T')
				checkSepecial = true;
		}

		if((count == 4) || ((count == 3) && (checkSepecial == true)))
			return true;
	}
	return false;
}

bool checkCol(char array[4][4], char check){
	int count;
	bool checkSepecial = false;
	for(int i = 0; i < 4; i++) {
		count = 0;
		checkSepecial = false;
		for(int j = 0; j < 4; j++) {
			if(array[j][i] == check)
				count++;
			else if(array[j][i] == 'T')
				checkSepecial = true;
		}

		if((count == 4) || ((count == 3) && (checkSepecial == true)))
			return true;
	}
	return false;
}

bool checkDiagonal(char array[4][4], char check){
	int count = 0;
	bool checkSepecial = false;
	for(int i = 0; i < 4; i++) {
		checkSepecial = false;
		if(array[i][i] == check)
			count++;
		else if(array[i][i] == 'T')
			checkSepecial = true;
	}
	if((count == 4) || ((count == 3) && (checkSepecial == true)))
		return true;

	count = 0;
	for(int i = 0; i < 4; i++) {
		checkSepecial = false;
		if(array[i][3 - i] == check)
			count++;
		else if(array[i][3 - i] == 'T')
			checkSepecial = true;
	}
	if((count == 4) || ((count == 3) && (checkSepecial == true)))
		return true;

	return false;
}

