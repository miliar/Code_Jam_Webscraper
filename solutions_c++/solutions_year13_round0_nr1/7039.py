// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <math.h>

bool StillHasDots( int inBoard[4][4]  ){
	for ( int m = 0; m < 4; m++ )
		for ( int n = 0; n < 4; n++ )
			if ( inBoard[m][n] == 0 )
				return true;
	return false;
}

int checkHorizontal( int inBoard[4][4], int Hori, int Vert, int checkNo ){
	// Check horizontal.
	int OneCount = 0;
	int TwoCount = 0;
	for ( int i = 0; i < 4; i++ ){
		if ( inBoard[Hori][i] == 1 )
			OneCount = OneCount + 1;
		if ( inBoard[Hori][i] == 2 )
			TwoCount = TwoCount + 1;
		if ( inBoard[Hori][i] == 3 ) {
			OneCount = OneCount + 1;
			TwoCount = TwoCount + 1;
		}
	}
	if ( OneCount == 4 )
		return 1;
	if ( TwoCount == 4 )
		return 2;
	OneCount = 0;
	TwoCount = 0;
	// Check Vertical.
	for ( int i = 0; i < 4; i++ ){
		if ( inBoard[i][Vert] == 1 )
			OneCount = OneCount + 1;
		if ( inBoard[i][Vert] == 2 )
			TwoCount = TwoCount + 1;
		if ( inBoard[i][Vert] == 3 ) {
			OneCount = OneCount + 1;
			TwoCount = TwoCount + 1;
		}
	}
	if ( OneCount == 4 )
		return 1;
	if ( TwoCount == 4 )
		return 2;
	// Check Diagonal.
	if ( Hori == 0 || Hori == 3 ){
		if ( Vert == 1 || Vert == 2 )
			return 0;
	}
	if ( Hori == 1 || Hori == 2 ){
		if ( Vert == 0 || Vert == 3 )
			return 0;
	}
	if ( Hori == Vert ) {
		OneCount = 0;
		TwoCount = 0;
		for ( int i = 0; i < 4; i++ ) {
			if ( inBoard[i][i] == 1 )
				OneCount = OneCount + 1;
			if ( inBoard[i][i] == 2 )
				TwoCount = TwoCount + 1;
			if ( inBoard[i][i] == 3 ) {
				OneCount = OneCount + 1;
				TwoCount = TwoCount + 1;
			}
		}
		if ( OneCount == 4 )
			return 1;
		if ( TwoCount == 4 )
			return 2;
	}
	if ( Hori != Vert ) {
		OneCount = 0;
		TwoCount = 0;
		for ( int i = 0; i < 4; i++ ) {
			if ( inBoard[i][abs(i-3)] == 1 )
				OneCount = OneCount + 1;
			if ( inBoard[i][abs(i-3)] == 2 )
				TwoCount = TwoCount + 1;
			if ( inBoard[i][abs(i-3)] == 3 ) {
				OneCount = OneCount + 1;
				TwoCount = TwoCount + 1;
			}
		}
		if ( OneCount == 4 )
			return 1;
		if ( TwoCount == 4 )
			return 2;
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::cout << "Starting of File." << std::endl;
	std::string aLine;

	std::ofstream outputFile;
	outputFile.open( "TomekOutput.txt" );

	std::ifstream myfile("A-large.in");
	bool readFirst = false;
	int NoLine = 1;

	if ( myfile.is_open() ){
		while( myfile.good() ){
			getline( myfile, aLine );
			std::cout << "At top the loop aLine is " << aLine << std::endl;
			if ( readFirst == false ){
				readFirst = true;
				continue;
			}
			std::string aResult = "";
			int board[4][4] = { { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 }  };
			for ( int i = 0; i < 4; i++ ){
				for ( int j = 0; j < 4; j++ ){
					if ( aLine[j] == 'X' )
						board[i][j] = 1;
					if ( aLine[j] == 'O' )
						board[i][j] = 2;
					if ( aLine[j] == 'T' )
						board[i][j] = 3;
				}
				if ( i != 3 )
					getline( myfile, aLine );
				std::cout << "In the loop aLine is " << aLine << std::endl;
			}
			// We have the board here.
			int Winner = 0;
			for ( int m = 0; m < 4; m++ ){
				for ( int n = 0; n < 4; n++ ){
					if ( checkHorizontal ( board, m, n, 1  ) != 0  )
					Winner = checkHorizontal ( board, m, n, 1  );
				}
			}
		
			if ( Winner == 0 ){
				if (  StillHasDots( board ) == true )
					aResult = "Game has not completed";
				else
					aResult = "Draw";
			} else {
				if ( Winner == 1 )
					aResult = "X won";
				else
					aResult = "O won";

			}
			outputFile << "Case #" << NoLine << ": " << aResult << std::endl;

			getline( myfile, aLine ); // Remove new line.
			std::cout << "At the end aLine is " << aLine << std::endl;


			NoLine = NoLine + 1;
		}
	}

	outputFile.close();

	std::string endLine;
	// std::cin >> endLine;

	return 0;
}

