#include <iostream>
#include <fstream>
#include <string>
#include <map>

enum DOMINANCE{EMTPY,FULL_X,FULL_O,NEUTRAL};
enum STATUS{X_WON,O_WON,DRAW,NOT_OVER};
std::map<STATUS,std::string> outputStrings;
DOMINANCE gHorizontalDominance[4];
DOMINANCE gVerticalDominance[4];
DOMINANCE gTopLeft2BottomRight;
DOMINANCE gBottomLeft2TopRight;

struct GameState{
char board[4][4];
};

inline void clearStateArrays()
{
	gTopLeft2BottomRight = EMTPY;
	gBottomLeft2TopRight = EMTPY;
	for(int it=0;it<4;++it)
		gHorizontalDominance[it]=gVerticalDominance[it]=EMTPY;
}

inline void incrementCounter(char fValue, int* fCounter)
{
	switch(fValue)
	{
		case 'X':
			fCounter[0]++;
			break;
		case 'O':
			fCounter[1]++;
			break;
		case 'T':
			fCounter[2]++;
			break;
		case '.':
			fCounter[3]++;
			break;
		default:
			break;
	}
}

int main(int argc, char** argv)
{
	// BEGIN - Initialize constants
	outputStrings[X_WON]="X won";
	outputStrings[O_WON]="O won";
	outputStrings[DRAW]="Draw";
	outputStrings[NOT_OVER]="Game has not completed";
	clearStateArrays();
	// END - Initialize constants

	GameState* inputs;
	int numInputs;
	// BEGIN - Read file
	std::ifstream inputFile;
	inputFile.open("C:\\Users\\prady\\Downloads\\A-large.in");
	if(inputFile.good())
	{
		std::string currentLine;
		std::getline(inputFile,currentLine);
		numInputs	= atoi(currentLine.c_str());
		inputs		= new GameState[numInputs];
		currentLine.clear();

		for(int inp=0;inp<numInputs; ++inp) {
			for(int row=0; row<4; ++row) {
				std::getline(inputFile,currentLine);
				inputs[inp].board[row][0] = currentLine[0];
				inputs[inp].board[row][1] = currentLine[1];
				inputs[inp].board[row][2] = currentLine[2];
				inputs[inp].board[row][3] = currentLine[3];
				currentLine.clear();
			}
			std::getline(inputFile,currentLine);
			currentLine.clear();
		}

		if(inputFile.eof())
			std::cout<<"Reached end of file."<<std::endl;
		else
			std::cout<<"Not reached end of file, some extra lines at the end!"<<std::endl;
	}
	inputFile.close();
	// END - Read file

	/*for(int inp=0;inp<numInputs; ++inp) {
			for(int row=0; row<4; ++row)
				std::cout<<inputs[inp].board[row][0]<<inputs[inp].board[row][1]<<inputs[inp].board[row][2]<<inputs[inp].board[row][3]<<std::endl;
			std::cout<<std::endl<<std::endl;
	}*/

	STATUS* output = new STATUS[numInputs];
	// BEGIN - Processing inputs
	for(int inp=0;inp<numInputs; ++inp)
	{
		// Horizontal dominace array
		for(int row=0;row<4;++row) {
			// Array indices for below array: 0 - X; 1 - O; 2 - T; 3 - .
			int pawnCounter[4]={0};
			incrementCounter(inputs[inp].board[row][0],pawnCounter);
			incrementCounter(inputs[inp].board[row][1],pawnCounter);
			incrementCounter(inputs[inp].board[row][2],pawnCounter);
			incrementCounter(inputs[inp].board[row][3],pawnCounter);
			if(pawnCounter[3]>0)
				gHorizontalDominance[row] = EMTPY;
			else if(pawnCounter[0]==4 || (pawnCounter[0]==3 && pawnCounter[2]==1))
				gHorizontalDominance[row] = FULL_X;
			else if(pawnCounter[1]==4 || (pawnCounter[1]==3 && pawnCounter[2]==1))
				gHorizontalDominance[row] = FULL_O;
			else
				gHorizontalDominance[row] = NEUTRAL;
		}
		// Vertical dominance array
		for(int col=0;col<4;++col) {
			// Array indices for below array: 0 - X; 1 - O; 2 - T; 3 - .
			int pawnCounter[4]={0};
			incrementCounter(inputs[inp].board[0][col],pawnCounter);
			incrementCounter(inputs[inp].board[1][col],pawnCounter);
			incrementCounter(inputs[inp].board[2][col],pawnCounter);
			incrementCounter(inputs[inp].board[3][col],pawnCounter);
			if(pawnCounter[3]>0)
				gVerticalDominance[col] = EMTPY;
			else if(pawnCounter[0]==4 || (pawnCounter[0]==3 && pawnCounter[2]==1))
				gVerticalDominance[col] = FULL_X;
			else if(pawnCounter[1]==4 || (pawnCounter[1]==3 && pawnCounter[2]==1))
				gVerticalDominance[col] = FULL_O;
			else
				gVerticalDominance[col] = NEUTRAL;
		}
		// Top to bottom diagonal
		{
			// Array indices for below array: 0 - X; 1 - O; 2 - T; 3 - .
			int pawnCounter[4]={0};
			incrementCounter(inputs[inp].board[0][0],pawnCounter);
			incrementCounter(inputs[inp].board[1][1],pawnCounter);
			incrementCounter(inputs[inp].board[2][2],pawnCounter);
			incrementCounter(inputs[inp].board[3][3],pawnCounter);
			if(pawnCounter[3]>0)
				gTopLeft2BottomRight = EMTPY;
			else if(pawnCounter[0]==4 || (pawnCounter[0]==3 && pawnCounter[2]==1))
				gTopLeft2BottomRight = FULL_X;
			else if(pawnCounter[1]==4 || (pawnCounter[1]==3 && pawnCounter[2]==1))
				gTopLeft2BottomRight = FULL_O;
			else
				gTopLeft2BottomRight = NEUTRAL;
		}
		// Bottom to top diagonal
		{
			// Array indices for below array: 0 - X; 1 - O; 2 - T; 3 - .
			int pawnCounter[4]={0};
			incrementCounter(inputs[inp].board[3][0],pawnCounter);
			incrementCounter(inputs[inp].board[2][1],pawnCounter);
			incrementCounter(inputs[inp].board[1][2],pawnCounter);
			incrementCounter(inputs[inp].board[0][3],pawnCounter);
			if(pawnCounter[3]>0)
				gBottomLeft2TopRight = EMTPY;
			else if(pawnCounter[0]==4 || (pawnCounter[0]==3 && pawnCounter[2]==1))
				gBottomLeft2TopRight = FULL_X;
			else if(pawnCounter[1]==4 || (pawnCounter[1]==3 && pawnCounter[2]==1))
				gBottomLeft2TopRight = FULL_O;
			else
				gBottomLeft2TopRight = NEUTRAL;
		}
		// compute game state based on dominance values
		if(gHorizontalDominance[0]==FULL_X || gHorizontalDominance[1]==FULL_X
			|| gHorizontalDominance[2]==FULL_X || gHorizontalDominance[3]==FULL_X
			|| gVerticalDominance[0]==FULL_X || gVerticalDominance[1]==FULL_X
			|| gVerticalDominance[2]==FULL_X || gVerticalDominance[3]==FULL_X
			|| gTopLeft2BottomRight==FULL_X || gBottomLeft2TopRight==FULL_X)
			output[inp] = X_WON;
		else if(gHorizontalDominance[0]==FULL_O || gHorizontalDominance[1]==FULL_O
			|| gHorizontalDominance[2]==FULL_O || gHorizontalDominance[3]==FULL_O
			|| gVerticalDominance[0]==FULL_O || gVerticalDominance[1]==FULL_O
			|| gVerticalDominance[2]==FULL_O || gVerticalDominance[3]==FULL_O
			|| gTopLeft2BottomRight==FULL_O || gBottomLeft2TopRight==FULL_O)
			output[inp] = O_WON;
		else if(gHorizontalDominance[0]==NEUTRAL && gHorizontalDominance[1]==NEUTRAL
			&& gHorizontalDominance[2]==NEUTRAL && gHorizontalDominance[3]==NEUTRAL
			&& gVerticalDominance[0]==NEUTRAL && gVerticalDominance[1]==NEUTRAL
			&& gVerticalDominance[2]==NEUTRAL && gVerticalDominance[3]==NEUTRAL
			&& gTopLeft2BottomRight==NEUTRAL && gBottomLeft2TopRight==NEUTRAL)
			output[inp] = DRAW;
		else
			output[inp] = NOT_OVER;
		// clear state arrays
		clearStateArrays();
	}
	// END - Processing inputs

	//BEGIN - Write to file
	std::ofstream outputFile;
	outputFile.open("output_largeInput.txt");
	if(outputFile.good()) {
		for(int inp=0;inp<numInputs; ++inp) {
			outputFile<<"Case #"<<inp+1<<": "<<outputStrings[output[inp]]<<std::endl;
		}
	}
	outputFile.close();
	//END - Write to file
	return 0;
}
