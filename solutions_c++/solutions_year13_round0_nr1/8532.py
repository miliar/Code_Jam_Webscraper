#include <string>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <sstream>

#include "TicTacToeBoard.h"

using namespace std;

int main(int argc, const char *argv[]) 
{
	if (argc < 2) {
		return 1;
	}
	int result = 0;
	string line;
	ifstream inputfile(argv[1], ifstream::in);
	ofstream outputFile;
	outputFile.open("c:\\TEMP\\TicTacTomek\\output.txt");
	int numCases = 0;
	int currentCase = 0;
	int currentLine = 0;
	TicTacToeBoard myBoard;	
	if (inputfile.is_open())
	{
		while (inputfile.good())
		{			
			getline(inputfile, line);
			if (currentLine == 0) {
				numCases = atoi(line.c_str());
			} else if (currentLine % 5 != 0) {				
				int row = currentLine - (5 * currentCase) - 1;
				// Start of game				
				myBoard.setElement(row, 0, line.c_str()[0]);
				myBoard.setElement(row, 1, line.c_str()[1]);
				myBoard.setElement(row, 2, line.c_str()[2]);
				myBoard.setElement(row, 3, line.c_str()[3]);
				if (row == TicTacToeBoard::BOARD_SIZE-1) {
					++currentCase;					
					switch (myBoard.getResult()) {
						case TicTacToeBoard::DRAW:
							outputFile << "Case #" << currentCase << ": Draw" << endl;
							break;						
						case TicTacToeBoard::X_WON:
							outputFile << "Case #" << currentCase << ": X won" << endl;
							break;
						case TicTacToeBoard::O_WON:
							outputFile << "Case #" << currentCase << ": O won" << endl;
							break;
						default:
						case TicTacToeBoard::NOT_COMPLETED:
							outputFile << "Case #" << currentCase << ": Game has not completed" << endl;
							break;
					}
					myBoard.reset();
				}				
			}
			++currentLine;
		}
		inputfile.close();
		outputFile.close();		
	}	
    return 0;
}