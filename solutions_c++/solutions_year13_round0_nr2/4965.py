//
//  main.cpp
//  Lawn
//
//  Created by Patrick Burns on 4/12/13.
//  Copyright (c) 2013 Bl4ckSun Developement. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <unistd.h>
#include <math.h>
#include <algorithm>
using namespace std;


#if 0
string filename = "sample.txt";
string resultsFile = "codeJameResults-Sample.txt";
#elif 0
string filename = "small.txt";
string resultsFile = "codeJameResults-Small.txt";
#elif 1
string filename = "large.txt";
string resultsFile = "codeJameResults-Big.txt";
#endif


int numberOfTest;
int testN, testM;

int lawn[100][100];
int rowHeight[100];
int colHeight[100];

std::ifstream inFile;
std::ofstream outFile;

char * evalLawn(int inRows, int inCols);

int main(int argc, const char * argv[])
{
	
	inFile.open(filename);
	outFile.open(resultsFile);
	
	inFile >> numberOfTest;
//	std::cout << "Number of Test:" << numberOfTest << std::endl;
	for (int i = 1; i <= numberOfTest; i++)
	{
		inFile >> testN >> testM;
//		cout << "Test:" << i << "N: "<< testN << " by M:" << testM << std::endl;
		outFile << "Case #" << i << ": " << evalLawn(testN,testM) << std::endl;
	}
	
    return 0;
}


char * evalLawn(int inRows, int inCols)
{
 	int height;
	memset(rowHeight, 0, sizeof(int)*100);
	memset(colHeight, 0, sizeof(int)*100);
	memset(lawn,      0,  sizeof(int)*100*100);
	
	for(int i = 0; i < inRows; i++)
	{
		for(int j = 0; j < inCols; j++)
		{
			inFile >> height;
			rowHeight[i] = max(rowHeight[i], height);
			colHeight[j] = max(colHeight[j], height);
			lawn[i][j] = height;
		}
	}
	
	
	for(int i = 0; i < inRows; i++)
	{
		for(int j = 0; j < inCols; j++)
		{
			if(lawn[i][j] < rowHeight[i] &&  lawn[i][j] < colHeight[j])
				return "NO";
			
		}
	}
	
	return "YES";
}

//char * evalGame()
//{
//	
//	completeGame = true;							// Disable at first '.'
//	memset(&rowVictory, 0, sizeof(short)*4);			// Count the number of X and O (-X is negative)
//	memset(&colVictory, 0, sizeof(short)*4);
//	diagVictoryOne = 0;
//	diagVictoryTwo = 0;
//	int value = 0;
//	char space;
//	
//	for (int row = 0; row < 4; row++)
//	{
//		for (int col = 0; col < 4; col++)
//		{
//			inFile >> space;
//			value = 0;
//			switch (space) {
//				case 'X': value = X_TIC; break;
//				case 'O': value = O_Tac; break;
//				case 'T': value = TOMEK; break;
//				case '.': completeGame = false;  break;
//				default: cerr << "Error" << endl;
//					break;
//			}
//			rowVictory[row] += value;
//			colVictory[col] += value;
//			if((row == 0 && col == 0) ||
//			   (row == 1 && col == 1) ||
//			   (row == 2 && col == 2) ||
//			   (row == 3 && col == 3) )
//				diagVictoryOne += value;
//			
//			if((row == 3 && col == 0) ||
//			   (row == 2 && col == 1) ||
//			   (row == 1 && col == 2) ||
//			   (row == 0 && col == 3) )
//				diagVictoryTwo += value;
//		}
//	}
//	
//	cout << "Dia1 " << endl;
//	if(winCondition(diagVictoryOne))
//		return winValue(diagVictoryOne);
//	
//	cout << "Dia2 " << endl;
//	if(winCondition(diagVictoryTwo))
//		return winValue(diagVictoryTwo);
//	
//	cout << "row " << endl;
//	for(int i = 0; i < 4; i++)
//		if(winCondition(rowVictory[i]))
//			return winValue(rowVictory[i]);
//	
//	cout << "col " << endl;
//	for(int i = 0; i < 4; i++)
//		if(winCondition(colVictory[i]))
//			return winValue(colVictory[i]);
//	
//	cout << "Ohter" << endl;
//	if(completeGame)
//		return "Draw";
//	else
//		return "Game has not completed";
//}
//
//char *winValue(short inValue)
//{
//	switch (inValue) {
//		case X_WIN:
//		case X_WIN_T:
//			return "X won";
//			break;
//			
//		case O_WINS:
//		case O_WIN_T:
//			return "O won";
//			break;
//		default:
//			return "ERROR";
//			break;
//	}
//	
//	return "ERROR";
//}
//
//bool winCondition(short inValue)
//{
//	cout << "Win Con: " << inValue << endl;
//	switch (inValue) {
//		case X_WIN:
//		case O_WINS:
//		case X_WIN_T:
//		case O_WIN_T:
//			return true;
//			break;
//		default:
//			return false;
//			break;
//	}
//}

