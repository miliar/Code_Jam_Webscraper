#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

// The game board
char board[4][4];

// Checking the result
char check();

int main()
{
	ios_base::sync_with_stdio(false);
	
	int games;
	
	cin >> games;
	
	for (int game=0; game < games; game++)
	{
		// Read the board
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin >> board[i][j];
		
		// Check the board
		char result = check();
		
		// Display the result
		cout << "Case #" << game + 1 << ": ";
		
		switch (result)
		{
			case 'X':
			case 'O':
				cout << result << " won\n";
				break;
			case '.':
				cout << "Game has not completed\n";
				break;
			case 'D':
				cout << "Draw\n";
				break;
			default:
				;
		}
	}
	
	exit(EXIT_SUCCESS);
}

char check()
{
	bool haveEmptyCell = false;
	char lastHorizontal;
	char lastVertical;
	bool continueH = true;
	bool continueV = true;
	
	for (int i=0; i<4; i++)
	{
		continueH = true;
		continueV = true;
		lastHorizontal = board[i][0];
		lastVertical = board[0][i];
		
		// Handling with T
		if (lastHorizontal == 'T')
			lastHorizontal = board[i][1];
		if (lastVertical == 'T')
			lastVertical = board[1][i];
		
		for (int j=0; j<4; j++)
		{
			// Horizontal Checking
			if (((lastHorizontal == board[i][j]) || (board[i][j] == 'T')) && (continueH))
				continueH = true;
			else
				continueH = false;
			
			// Vertical Checking
			if (((lastVertical == board[j][i]) || (board[j][i] == 'T')) && (continueV))
				continueV = true;
			else
				continueV = false;
				
			// Empty Cells Checking
			if (board[i][j] == '.')
				haveEmptyCell = true;
		}
		
		// Full row
		if (continueH && (lastHorizontal != '.'))
			return lastHorizontal;
		
		// Full column
		if (continueV && (lastVertical != '.'))
			return lastVertical;
	}
	
	// ULBR Diagonal Checking
	char lastULBR = board[0][0];
	bool continueULBR = true;
	if (lastULBR == 'T') lastULBR = board[1][1];
	for (int i=0; i<4; i++)
	{
		if (((lastULBR == board[i][i]) || (board[i][i] == 'T')) && (continueULBR))
			continueULBR = true;
		else
			continueULBR = false;
	}
	
	// BLUR Diagonal Checking
	char lastBLUR = board[3][0];
	bool continueBLUR = true;
	if (lastBLUR == 'T') lastBLUR = board[2][1];
	for (int i=0; i<4; i++)
	{
		if (((lastBLUR == board[3 - i][i]) || (board[3 - i][i] == 'T')) && (continueBLUR))
			continueBLUR = true;
		else
			continueBLUR = false;
	}
	
	if (continueULBR)
		return lastULBR;
	if (continueBLUR)
		return lastBLUR;
	
	// Board isn't completed
	if (haveEmptyCell)
		return '.';
	
	// Draw
	else
		return 'D';
}
