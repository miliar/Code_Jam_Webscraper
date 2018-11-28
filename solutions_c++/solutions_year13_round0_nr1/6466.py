#include <cstdio>
#include <iostream>

using namespace std;

char board[4][4];

bool checkHorizontal( char player )
{
	for( int i=0; i<4; i++ )
	{
		bool isT = false;
		int counter = 0;

		for( int j=0; j<4; j++ )
		{
			if( board[j][i]=='T')
				isT = true;
			else if( board[j][i]==player)
				counter++;
		}

		if( counter==4 || (counter==3 && isT==true) )
			return true;
	}

	return false;
}

bool checkVertical( char player )
{
	for( int i=0; i<4; i++ )
	{
		bool isT = false;
		int counter = 0;

		for( int j=0; j<4; j++ )
		{
			if( board[i][j]=='T')
				isT = true;
			else if( board[i][j]==player)
				counter++;
		}

		if( counter==4 || (counter==3 && isT==true) )
			return true;
	}

	return false;
}

bool checkRDiagonal( char player )
{
	bool isT = false;
	int counter = 0;

	for( int i=0; i<4; i++ )
	{
		if( board[i][i]=='T')
			isT = true;
		else if( board[i][i]==player)
			counter++;	
	}

	if( counter==4 || (counter==3 && isT==true) )
			return true;
	else
		return false;
}

bool checkLDiagonal( char player )
{
	bool isT = false;
	int counter = 0;

	for( int i=0; i<4; i++ )
	{
		if( board[3-i][i]=='T')
			isT = true;
		else if( board[3-i][i]==player)
			counter++;	
	}

	if( counter==4 || (counter==3 && isT==true) )
			return true;
	else
		return false;
}

int main()
{
	int t,i=1;
	cin >> t;

	while( t-- )
	{
		int emptiesCount = 0;

		for( int r=0; r<4; r++ )
		{
			for( int c=0; c<4; c++ )
			{
				cin >> board[r][c];

				if( board[r][c]== '.' )
					emptiesCount++;
			}
		}

		cout << "Case #" << i << ": ";
		i++;
		if( checkVertical('X') || checkHorizontal('X') || checkLDiagonal('X') || checkRDiagonal('X'))
			cout << "X won";
		else if( checkVertical('O') || checkHorizontal('O') || checkLDiagonal('O') || checkRDiagonal('O'))
			cout << "O won";
		else if( emptiesCount == 0 )
			cout << "Draw";
		else
			cout << "Game has not completed";
		cout << endl;
	}

	return 0;
}