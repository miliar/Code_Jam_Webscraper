// reading a text file
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

enum results_e
{
	OUTPUT_X_WON		= 0,
	OUTPUT_O_WON		= 1,
	OUTPUT_DRAW			= 2,
	OUTPUT_INCOMPLETE	= 3
};

results_e analyseCaseBlock( char caseBlockPtr[][4] );

int main () {

  string line;
  int num_of_cases = 0;
  int caseCount = 0;

  char caseBlock[4][4];
  char temp;
  int colCount = 0;
  int rowCount = 0;

  results_e res;

  ifstream myfile( "A-small-attempt0.in" );

  ofstream output( "A-small1.out" , ios_base::app );

  if ( myfile.is_open() && myfile.good() )
  {
	  getline( myfile , line );
	  istringstream iss(line);

	  iss >> num_of_cases;

	  cout << "Case count: " << num_of_cases << endl;

	if( num_of_cases > 0 )
	{
		while( myfile.good() && caseCount < num_of_cases )
		{
			getline( myfile , line );

			if( line.empty() )
			{
				caseCount++;
				rowCount = 0;

				// analyse case
				res = analyseCaseBlock( caseBlock );

				if( output.is_open() && output.good() )
				{
					switch( res )
					{
					case	OUTPUT_X_WON		:
						output << "Case #" << caseCount << ": " << "X won" << endl;
						break;
					case	OUTPUT_O_WON		:
						output << "Case #" << caseCount << ": " << "O won" << endl;
						break;
					case	OUTPUT_DRAW			:
						output << "Case #" << caseCount << ": " << "Draw" << endl;
						break;
					case	OUTPUT_INCOMPLETE	:
						output << "Case #" << caseCount << ": " << "Game has not completed" << endl;
						break;
					}
				}

				cout << "res: " << res << endl;

				

				memset( caseBlock , 0 , sizeof( caseBlock ) );

				cout << "empty" << endl;
			}
			else
			{
				istringstream iss(line);

				while( iss.get( temp ) )
				{
					caseBlock[ rowCount ][ colCount++ ] = temp;
				}

				colCount = 0;
				rowCount++;

				cout << line << endl;
			}

		}
	}
    
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}

results_e analyseCaseBlock( char caseBlockPtr[][4] )
{
	int vIndex = 0, hIndex = 0;
	int xCount = 0, oCount = 0;
	bool spaceFound = false , xFound = false , oFound = false , tFound = false;
	char temp;

	// horizontal

	for( vIndex = 0; vIndex < 4; vIndex++ )
	{
		for( hIndex = 0; hIndex < 4; hIndex++ )
		{
			temp = caseBlockPtr[ vIndex ][ hIndex ];

			if( temp == 'X' && !oFound )
			{
				xFound = true;
				xCount++;
			}
			else if( temp == 'O' && !xFound )
			{
				oFound = true;
				oCount++;
			}
			else if( temp == '.' )
			{
				spaceFound = true;
				break;
			}
			else if( temp == 'T' )
			{
				tFound = true;
			}
			else
			{
				break;
			}
		}

		if( xFound || oFound )
		{
			if( ( xCount == 3 && tFound ) || xCount == 4 )
			{
				return OUTPUT_X_WON;
			}
			else if( ( oCount == 3 && tFound ) || oCount == 4 )
			{
				return OUTPUT_O_WON;
			}
		}

		tFound = false;
		oCount = 0;
		oFound = false;
		xCount = 0;
		xFound = false;
	}

	// vertical

	for( hIndex = 0; hIndex < 4; hIndex++ )
	{
		for( vIndex = 0; vIndex < 4; vIndex++ )
		{
			temp = caseBlockPtr[ vIndex ][ hIndex ];

			if( temp == 'X' && !oFound )
			{
				xFound = true;
				xCount++;
			}
			else if( temp == 'O' && !xFound )
			{
				oFound = true;
				oCount++;
			}
			else if( temp == '.' )
			{
				spaceFound = true;
				break;
			}
			else if( temp == 'T' )
			{
				tFound = true;
			}
			else
			{
				break;
			}
		}

		if( xFound || oFound )
		{
			if( ( xCount == 3 && tFound ) || xCount == 4 )
			{
				return OUTPUT_X_WON;
			}
			else if( ( oCount == 3 && tFound ) || oCount == 4 )
			{
				return OUTPUT_O_WON;
			}
		}

		tFound = false;
		oCount = 0;
		oFound = false;
		xCount = 0;
		xFound = false;
	}

	// diagonal left top to right bottom

	for( int index = 0; index < 4; index++ )
	{
		temp = caseBlockPtr[ index ][ index ];

		if( temp == 'X' && !oFound )
		{
			xFound = true;
			xCount++;
		}
		else if( temp == 'O' && !xFound )
		{
			oFound = true;
			oCount++;
		}
		else if( temp == '.' )
		{
			spaceFound = true;
			break;
		}
		else if( temp == 'T' )
		{
			tFound = true;
		}
		else
		{
			break;
		}
	}

	if( xFound || oFound )
	{
		if( ( xCount == 3 && tFound ) || xCount == 4 )
		{
			return OUTPUT_X_WON;
		}
		else if( ( oCount == 3 && tFound ) || oCount == 4 )
		{
			return OUTPUT_O_WON;
		}
	}

	tFound = false;
	oCount = 0;
	oFound = false;
	xCount = 0;
	xFound = false;

	// diagonal left bottom to right top

	for( int index = 0; index < 4; index++ )
	{
		temp = caseBlockPtr[ 3 - index ][ index ];

		if( temp == 'X' && !oFound )
		{
			xFound = true;
			xCount++;
		}
		else if( temp == 'O' && !xFound )
		{
			oFound = true;
			oCount++;
		}
		else if( temp == '.' )
		{
			spaceFound = true;
			break;
		}
		else if( temp == 'T' )
		{
			tFound = true;
		}
		else
		{
			break;
		}
	}

	if( xFound || oFound )
	{
		if( ( xCount == 3 && tFound ) || xCount == 4 )
		{
			return OUTPUT_X_WON;
		}
		else if( ( oCount == 3 && tFound ) || oCount == 4 )
		{
			return OUTPUT_O_WON;
		}
	}


	return spaceFound ? OUTPUT_INCOMPLETE : OUTPUT_DRAW;
}