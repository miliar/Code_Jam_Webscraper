// TTTT.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

ifstream input;
ofstream output;
string data;
int T; // number of test cases
//int result; // 0; Game has not completed; 1; X won; 2: O won; 3: Draw;
int matrix1[4][4]; // to store data in one test case: set "T" to 1: suggest X won
int matrix2[4][4]; // set "T" to -1: suggest O won
char c;

void loop_process();
bool X_win();
bool O_win();

int _tmain(int argc, _TCHAR* argv[])
{
	input.open(argv[1]);
	output.open("output.txt");

	if(input.is_open())
	{
		// get the number of test cases
		getline(input, data);
		T = atoi(data.c_str());

		// loop
		for(int i=0; i<T; i++)
		//for(int i=0; i<2; i++)
		{
			cout << "Case #" << i+1 << ": ";
			output << "Case #" << i+1 << ": ";
			loop_process();
		}
	}
	
	input.close();
	output.close();
	
	return 0;
}

// process
void loop_process()
{
	bool draw = true; // false if "." is found

	for(int i=0; i < 4; i++) {
		for(int j=0; j<4; j++)
		{
			c = input.get();
			switch (c)
			{
			case 'X':
				matrix1[i][j] = 1;
				matrix2[i][j] = 1;
				break;
			case 'O':
				matrix1[i][j] = -1;
				matrix2[i][j] = -1;
				break;
			case 'T':
				matrix1[i][j] = 1;
				matrix2[i][j] = -1;
				break;
			case '.':
				matrix1[i][j] = 0;
				matrix2[i][j] = 0;
				draw = false;
				break;
			}
		}
		getline(input, data);
	}

	// to go to a new case
	getline(input, data);
			
	if(X_win())
	{
		cout << "X won" << endl;
		output << "X won" << endl;
	}
	else if(O_win())
	{
		cout << "O won" << endl;
		output << "O won" << endl;
	}
	else if(draw)
	{
		cout << "Draw" << endl;
		output << "Draw" << endl;
	}
	else
	{
		cout << "Game has not completed" << endl;
		output << "Game has not completed" << endl;
	}
}

// check if X won
bool X_win()
{
	for(int i=0; i<4; i++)
	{
		int sum = 0;
		for(int j=0; j<4; j++)
		{	
			sum += matrix1[i][j];
		}
		if (sum == 4)
			return true;
	}

	for(int j=0; j<4; j++)
	{
		int sum = 0;
		for(int i=0; i<4; i++)
		{	
			sum += matrix1[i][j];
		}
		if (sum == 4)
			return true;
	}

	{
		if(matrix1[0][0]+matrix1[1][1]+matrix1[2][2]+matrix1[3][3] == 4 ||
			matrix1[0][3]+matrix1[1][2]+matrix1[2][1]+matrix1[3][0] == 4)
			return true;
	}
	
	return false;
}

// Check if O won
bool O_win()
{
	for(int i=0; i<4; i++)
	{
		int sum = 0;
		for(int j=0; j<4; j++)
		{	
			sum += matrix2[i][j];
		}
		if (sum == -4)
			return true;
	}

	for(int j=0; j<4; j++)
	{
		int sum = 0;
		for(int i=0; i<4; i++)
		{	
			sum += matrix2[i][j];
		}
		if (sum == -4)
			return true;
	}

	{
		if(matrix2[0][0]+matrix2[1][1]+matrix2[2][2]+matrix2[3][3] == -4 ||
			matrix2[0][3]+matrix2[1][2]+matrix2[2][1]+matrix2[3][0] == -4)
			return true;
	}
	
	return false;
}
