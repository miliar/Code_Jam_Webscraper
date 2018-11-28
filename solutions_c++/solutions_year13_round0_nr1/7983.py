#include <iostream>
#include <fstream>
#include <string>

#define SMALLIN		"A-small-attempt0.in"
#define SMALLOUT	"A-small-attempt0.out"
#define LARGEIN		""
#define LARGEOUT	""

#define X		"X won"
#define O		"O won"
#define DRAW	"Draw"
#define GOON	"Game has not completed"


using namespace std;

string judge( char data[4][4] , bool flag )
{
	// decide if who has won the game
	// all rows
	for( int i = 0 ; i < 4 ; i ++ )
	{
		char curPlayer = data[ i ][ 0 ];
		if( curPlayer == 'X' )
		{
			if( data[i][1] != '.' && data[i][1] != 'O' )
			{
				if( data[i][2] != '.' && data[i][2] != 'O' )
				{
					if( data[i][3] != '.' && data[i][3] != 'O' )
					{
						return X;
					}// end of if-3
				}// end of if-2
			}//end of if-1
		}
		else if ( curPlayer == 'O' )
		{
			if( data[i][1] != '.' && data[i][1] != 'X' )
			{
				if( data[i][2] != '.' && data[i][2] != 'X' )
				{
					if( data[i][3] != '.' && data[i][3] != 'X' )
					{
						return O;
					}// end of if-3
				}// end of if-2
			}//end of if-1
		}
		else if( curPlayer == 'T' )
		{
			if(  data[i][1] != '.' &&data[i][1] == data[i][2] && data[i][2] == data[i][3])
			{
				if( data[i][1] == 'O' )
				{
					return O;
				}
				else
				{
					return X;
				}
			}
		}
		else
		{
			continue;
		}
	}


	// all rows
	for( int i = 0 ; i < 4 ; i ++ )
	{
		char curPlayer = data[ 0 ][ i ];
		if( curPlayer == 'X' )
		{
			if( data[1][i] != '.' && data[1][i] != 'O' )
			{
				if( data[2][i] != '.' && data[2][i] != 'O' )
				{
					if( data[3][i] != '.' && data[3][i] != 'O' )
					{
						return X;
					}// end of if-3
				}// end of if-2
			}//end of if-1
		}
		else if ( curPlayer == 'O' )
		{
			if( data[1][i] != '.' && data[1][i] != 'X' )
			{
				if( data[2][i] != '.' && data[2][i] != 'X' )
				{
					if( data[3][i] != '.' && data[3][i] != 'X' )
					{
						return O;
					}// end of if-3
				}// end of if-2
			}//end of if-1
		}
		else if( curPlayer == 'T' )
		{
			if(  data[1][i] != '.' &&data[2][i] == data[2][i] && data[2][i] == data[3][i])
			{
				if( data[1][i] == 'O' )
				{
					return O;
				}
				else
				{
					return X;
				}
			}
		}
		else
		{
			continue;
		}
	}

	// diagonal 1
 	if( data[0][0] != '.' && data[0][0] == data[1][1] && data[2][2] == data[1][1] && data[3][3] == data[1][1] )
	{
		if ( data[0][0] == 'X' )
		{
			return X;
		}
		else
		{
			return O;
		}
	}

	if( data[0][0] == 'T' )
	{
		if( data[1][1] == 'X' && data[2][2] == 'X' && data[3][3] == 'X' )
		{
			return X;
		}
		if( data[1][1] == 'O' && data[2][2] == 'O' && data[3][3] == 'O' )
		{
			return O;
		}
	}

	if( data[1][1] == 'T' )
	{
		if( data[0][0] == 'X' && data[2][2] == 'X' && data[3][3] == 'X' )
		{
			return X;
		}
		if( data[0][0] == 'O' && data[2][2] == 'O' && data[3][3] == 'O' )
		{
			return O;
		}
	}

	if( data[2][2] == 'T' )
	{
		if( data[1][1] == 'X' && data[0][0] == 'X' && data[3][3] == 'X' )
		{
			return X;
		}
		if( data[1][1] == 'O' && data[0][0] == 'O' && data[3][3] == 'O' )
		{
			return O;
		}
	}

	if( data[3][3] == 'T' )
	{
		if( data[1][1] == 'X' && data[2][2] == 'X' && data[0][0] == 'X' )
		{
			return X;
		}
		if( data[1][1] == 'O' && data[2][2] == 'O' && data[0][0] == 'O' )
		{
			return O;
		}
	}

	// diagonal 2
	if( data[3][0] != '.' && data[3][0] == data[2][1] && data[3][0] == data[1][2] && data[3][0] == data[0][3] )
	{
		if ( data[3][0] == 'X' )
		{
			return X;
		}
		else
		{
			return O;
		}
	}

	if( data[3][0] == 'T' )
	{
		if( data[2][1] == 'X' && data[1][2] == 'X' && data[0][3] == 'X' )
		{
			return X;
		}
		if( data[2][1] == 'O' && data[1][2] == 'O' && data[0][3] == 'O' )
		{
			return O;
		}
	}

	if( data[2][1] == 'T' )
	{
		if( data[3][0] == 'X' && data[1][2] == 'X' && data[0][3] == 'X' )
		{
			return X;
		}
		if( data[3][0] == 'O' && data[1][2] == 'O' && data[0][3] == 'O' )
		{
			return O;
		}
	}

	if( data[1][2] == 'T' )
	{
		if( data[3][0] == 'X' && data[2][1] == 'X' && data[0][3] == 'X' )
		{
			return X;
		}
		if( data[3][0] == 'O' && data[2][1] == 'O' && data[0][3] == 'O' )
		{
			return O;
		}
	}

	if( data[2][1] == 'T' )
	{
		if( data[3][0] == 'X' && data[1][2] == 'X' && data[0][3] == 'X' )
		{
			return X;
		}
		if( data[3][0] == 'O' && data[1][2] == 'O' && data[0][3] == 'O' )
		{
			return O;
		}
	}

	if( flag == true )
	{
		return GOON;
	}
	return DRAW;
}

int main()
{
	ifstream infile( SMALLIN );
	ofstream outfile( SMALLOUT );
	int totalRecords ;
	infile >> totalRecords;
	char data[4][4];
	char ch;
	bool isBlank = false;
	for( int round = 0 ; round < totalRecords ; round ++ )
	{
		isBlank = false;
		for( int i = 0 ; i < 4 ; i ++ )
		{
			for( int j = 0 ; j < 4 ; j ++ )
			{
				infile >> ch ;
				while ( ch == '\n' && ch == ' ')
				{
					infile >> ch ;
				}
				if( ch == '.' )
				{
					isBlank = true;
				}
				data[ i ][ j ] = ch;
			}
		}
		outfile << "Case #" << round + 1 << ": " << judge( data , isBlank ) << endl;
	}
	infile.close();
	outfile.close();
}