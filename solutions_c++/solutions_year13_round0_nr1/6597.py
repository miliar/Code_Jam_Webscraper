#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void initializeBoard ();
void checkBoard(int i);

char board [4][4];

int main (int argc, char *argv[])
{
	int numCase;
	cin >> numCase;
	for (int i = 0; i < numCase; ++i){
		initializeBoard();
		checkBoard(i);
	}

}

void initializeBoard ()
{
	for (int x = 0; x < 4; ++x){
		for (int y = 0; y < 4; ++y){
			cin >> board [x][y];
		}
	}
}

void checkBoard(int i)
{
	bool winX = false;
  bool winO = false;
  bool completed = true;
	char checker = '.';

	//check for Vertical Win
	for (int y = 0; y < 4; ++y)
	{
		int total = 1;
		checker = '.';
		if (board [0][y] != 'T')
			checker = board [0][y];
		else 
			checker = board [1][y];
		for (int x = 1; x < 4; ++x)
		{
			if (checker != board [x][y] & board [x][y] != 'T')
				break;
			if (x == 3 && checker == 'X')
				winX = true;
			else if (x == 3 && checker == 'O')
				winO = true;
		}
	}


	//check for Horizontal Win
	for (int x = 0; x < 4; ++x)
	{
		int total = 1;
		checker = '.';
		if (board [x][0] != 'T')
			checker = board [x][0];
		else 
			checker = board [x][1];
		for (int y = 1; y < 4; ++y)
		{
			if (checker != board [x][y] & board [x][y] != 'T')
				break;
			if (y == 3 && checker == 'X')
				winX = true;
			else if (y == 3 && checker == 'O')
				winO = true;
		}
	}

	//check for LDiagonal Win
	int lX = 0;
	int lY = 0;
	checker = '.';
	if (board [lX][lY] == 'T')
	{
		++lX;
		++lY;
	}
	checker = board [lX][lY];
	while(lX != 4)
	{
		if (checker != board [lX][lY] & board [lX][lY] != 'T')
			break;
		++lX;
		++lY;
	}
	if (lX == 4 && checker == 'X')
		winX = true;
	else if (lX == 4 && checker == 'O')
		winO = true;



	//check for RDiagonal Win
	int rX = 3;
	int rY = 0;
	checker = '.';
	if (board [rX][rY] == 'T')
	{
		--rX;
		++rY;
	}
	checker = board [rX][rY];
	while(rY != 4)
	{
		if (checker != board [rX][rY] & board [rX][rY] != 'T')
			break;
		--rX;
		++rY;
	}
	if (rY == 4 && checker == 'X')
		winX = true;
	else if (rY == 4 && checker == 'O')
		winO = true;



	//check for completness
	for (int x = 0; x < 4; ++x)
	{
		for (int y = 0; y < 4; ++y)
		{
			if (board [x][y] == '.')
				completed = false;	
		}
	}
	ofstream outputFile;
	outputFile.open("A-large.out", ios::app);
	outputFile << "Case #" << i+1 << ": ";
	if (winX)
		outputFile << "X won" <<endl;
	else if (winO)
		outputFile << "O won" <<endl;
	else if (completed)
		outputFile << "Draw" <<endl;
	else
		outputFile << "Game has not completed" <<endl;
}
