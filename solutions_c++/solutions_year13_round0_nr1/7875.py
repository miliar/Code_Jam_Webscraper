//============================================================================
// Name        : Tic-Tac-Toe-Tomek.cpp
// Author      : pulkjam
// Version     :
// Copyright   : pulkjam
// Description : Tik-Tac-Toe-Tomek
//============================================================================

#include <iostream>
#include <fstream>
#include <stack>
#include <streambuf>
using namespace std;

int main() {
	//Variables
	ifstream fin;
	ofstream fout;

	int numOfCases;
	char grid[4][4];

	bool xWon = false;
	bool oWon = false;
	bool gameFinished = true;


	//Input Stream
	fin.open("A-large.in");
	fout.open("A-large.out");

	if(fin.is_open()){
		//Reading inputs
		if(!fin.eof()){
			fin >> numOfCases;

			//cout << "Num Of Cases: " << numOfCases << endl;

			fin.ignore(1); //Take out '\n' of first line

			for(int i=0; i < numOfCases; i++){
				xWon = false;
				oWon = false;
				gameFinished = true;


				for(int a=0; a < 4; a++){
					for(int b=0; b < 4; b++){

						grid[a][b] =  (char)fin.get();

						if(grid[a][b] == '.'){
							gameFinished = false;
						}

						//cout << grid[a][b];
					}

					//cout << endl;
					fin.ignore(1);	//Ignore \n

				}



				int xHorizontalCount = 0;
				int xVerticalCount = 0;
				int xDLRCount = 0;
				int xDRLCount = 0;

				int oHorizontalCount = 0;
				int oVerticalCount = 0;
				int oDLRCount = 0;
				int oDRLCount = 0;

				//Check horizontal
				for(int l=0; l < 4; l++){
					xHorizontalCount = 0;
					xVerticalCount = 0;
					oHorizontalCount = 0;
					oVerticalCount = 0;

					for(int m=0; m < 4; m++){

						//Horizontal
						if(grid[l][m] == 'X'){
							xHorizontalCount++;
						}
						else if(grid[l][m] == 'O'){
							oHorizontalCount++;
						}
						else if(grid[l][m] == 'T'){
							xHorizontalCount++;
							oHorizontalCount++;
						}

						//Vertical
						if(grid[m][l] == 'X'){
							xVerticalCount++;
						}
						else if(grid[m][l] == 'O'){
							oVerticalCount++;
						}
						else if(grid[m][l] == 'T'){
							xVerticalCount++;
							oVerticalCount++;
						}

						//Diagonal Left-Right
						if(m-l == 0){
							if(grid[l][m] == 'X'){
								xDLRCount++;
							}
							else if(grid[l][m] == 'O'){
								oDLRCount++;
							}
							else if(grid[l][m] == 'T'){
								xDLRCount++;
								oDLRCount++;
							}
						}

						//Diagonal Right-Left
						if(m+l == 3){
							if(grid[l][m] == 'X'){
								xDRLCount++;
							}
							else if(grid[l][m] == 'O'){
								oDRLCount++;
							}
							else if(grid[l][m] == 'T'){
								xDRLCount++;
								oDRLCount++;
							}
						}

					}

					//Check if anyone on horizontals won
					if((xHorizontalCount == 4) || (xVerticalCount == 4)){
						xWon = true;
					}

					if((oHorizontalCount == 4) || (oVerticalCount == 4)){
						oWon = true;
					}

				}

				//Check diagonals
				if((xDLRCount == 4) || (xDRLCount == 4)){
					xWon = true;
				}

				if((oDLRCount == 4) || (oDRLCount == 4)){
					oWon = true;
				}


				//Print out results
				fout << "Case #" << i + 1 << ": ";

				if(xWon){
					fout << "X won" << endl;
				}
				else if(oWon){
					fout << "O won" << endl;
				}
				else{
					if(gameFinished){
						fout << "Draw" << endl;
					}
					else {
						fout << "Game has not completed" << endl;
					}
				}

				//Pop last end of line
				fin.ignore(1);

				//cout << endl;


			}
		}
	}
	else{
		cout << "Could not open input file" << endl;
	}

	return 0;
}
