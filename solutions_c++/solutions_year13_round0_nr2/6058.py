// reading a text file
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

//small
#define MAX_N 10
#define MAX_M 10

using namespace std;

enum results_e
{
	OUTPUT_NO		= 0,
	OUTPUT_YES		= 1
};

results_e analyseLawnPattern( int lawnPatternPtr[ MAX_N ][ MAX_M ] , int minIndexPtr[ MAX_N ] , int minIndexPosXPtr[ MAX_N ] , bool duplicateMinIndexPtr[ MAX_N ][ MAX_M ] , int N , int M );

int main () {

  string line;
  int num_of_cases = 0;
  int caseCount = 0;

  int lawnPattern[ MAX_N ][ MAX_M ];
  int minIndexArr[ MAX_N ];
  int minIndexPosX[ MAX_N ];
  bool duplicateMinIndex[ MAX_N ][ MAX_M ];

  memset( duplicateMinIndex , 0 , sizeof( duplicateMinIndex ) );

  char temp;
  int colCount = 0;
  int rowCount = 0;

  int N = 0, M = 0;
  int nIndex = 0 , mIndex = 0;

  int tempMin = 100 , tempPosX = 0;

  results_e res = OUTPUT_NO;

  ifstream myfile( "B-small-attempt1.in" );

  ofstream output( "B-small2.out" , ios_base::app );

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

			// read N and M
			getline( myfile , line );
			istringstream iss(line);

			iss >> N >> M;
			cout << "N: " << N << " M: " << M << endl;
			

			if( N == 1 || M == 1 )
			{
				caseCount++;
				//just read a line
				int readCount = 0;
				while( readCount < N )
				{
					getline( myfile , line );
					readCount++;
				}

				if( output.is_open() && output.good() )
				output << "Case #" << caseCount << ": " << "YES" << endl;
			}
			else if( N >= 1 && M >= 1 )
			{
				// read N x M matrix
				for( nIndex = 0; nIndex < N; nIndex++ )
				{
					getline( myfile , line );
					istringstream iss(line);

					tempMin = 10;

					for( mIndex = 0; mIndex < M; mIndex++ )
					{
						iss >> lawnPattern[ nIndex ][ mIndex ];

						cout << lawnPattern[ nIndex ][ mIndex ] << " ";

						if( lawnPattern[ nIndex ][ mIndex ] < tempMin )
						{
							tempMin = lawnPattern[ nIndex ][ mIndex ];
							tempPosX = mIndex;

							memset( duplicateMinIndex[ nIndex ] , 0 , sizeof( duplicateMinIndex[ nIndex ] ) );
						}
						else if( lawnPattern[ nIndex ][ mIndex ] == tempMin )
						{
							// record duplicate positions as well

							duplicateMinIndex[ nIndex ][ mIndex ] = true;
						}
					}

					minIndexArr[ nIndex ] = tempMin;
					minIndexPosX[ nIndex ] = tempPosX;

					cout << " min: " << tempMin << " pos: " << tempPosX;

					cout << endl;

					/*for( int i = 0; i < N; i++ )
					{
						for( int j = 0; j < M; j++ )
						{
							if( duplicateMinIndex[ i ][ j ] )
							{
								cout << "d at i: " << i << " j: " << j << endl;
							}
						}
					}*/

				}

				caseCount++;

				// analyse case
				res = analyseLawnPattern( lawnPattern , minIndexArr , minIndexPosX , duplicateMinIndex , N , M );

				if( output.is_open() && output.good() )
				{
					switch( res )
					{
					case	OUTPUT_NO		:
						output << "Case #" << caseCount << ": " << "NO" << endl;
						break;
					case	OUTPUT_YES		:
						output << "Case #" << caseCount << ": " << "YES" << endl;
						break;
					}
				}

				cout << "res: " << res << endl;

			}

			memset( lawnPattern , 0 , sizeof( lawnPattern ) );
			memset( minIndexArr , 0 , sizeof( minIndexArr ) );
			memset( minIndexPosX , 0 , sizeof( minIndexPosX ) );
			memset( duplicateMinIndex , 0 , sizeof( duplicateMinIndex ) );
			
		}
	}
    
    myfile.close();
	output.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}

results_e analyseLawnPattern( int lawnPatternPtr[ MAX_N ][ MAX_M ] , int minIndexPtr[ MAX_N ] , int minIndexPosXPtr[ MAX_N ] , bool duplicateMinIndexPtr[ MAX_N ][ MAX_M ] , int N , int M )
{
	
	bool pathBlocked = false;

	for( int row = 0; row < N; row++ )
	{
		for( int col = 0; col < M; col++ )
		{
			if( col == minIndexPosXPtr[ row ] || duplicateMinIndexPtr[ row ][ col ] )
			{
				// search up and down plus duplicates

				//			|
				//			|
				//----------O-------------
				//			|
				//			|
				//			|

				// search between ( 0 , col ) to ( N , col )
				// search between ( row , 0 ) to ( row , M )
				// for a number bigger than min for that path

				// search vertical
				for( int i = 0; i < N; i++ )
				{
					if( lawnPatternPtr[ i ][ col ] > minIndexPtr[ row ] )
					{
						pathBlocked = true;
					}
				}
				// search horizontal
				for( int j = 0; j < M; j++ )
				{
					if( lawnPatternPtr[ row ][ j ] > minIndexPtr[ row ] && pathBlocked )
					{
						return OUTPUT_NO;
					}
				}

				pathBlocked = false;

				// do the same for duplicates for confirmation
			}
		}
	}

	return OUTPUT_YES;
}