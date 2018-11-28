#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main( int argc, char** argv )
{
	unsigned int numCases(0), iCase(0);

	string inputFileName = argv[1];
	int length = inputFileName.length();

	string outputFileName = inputFileName.substr(0,length - 2);
	outputFileName += "out";

	ifstream inputFile(inputFileName);
	ofstream outputFile(outputFileName);

	if( !inputFile )
	{
		cout << "RW: Error opening input file - exiting..." << endl;
		int temp;
		cin >> temp;
		exit(0);
	}

	string line;

	getline( inputFile, line );
	numCases = int(atof( line.c_str() ));

	iCase = 0;

	while( iCase < numCases )
	{
		++iCase;

		getline( inputFile, line );
		stringstream lineStream( line );

		int ** squares;
		int *rowMax, *rowMin, *colMax, *colMin;
		int numRows, numCols;
		string temp;
		
		getline( lineStream, temp, ' ' );
		numRows = int(atof( temp.c_str() ));
		getline( lineStream, temp, ' ' );
		numCols = int(atof( temp.c_str() ));

		squares = new int*[numRows];
		for( int i = 0; i < numRows; ++i )
		{
			squares[i] = new int[numCols];
		}
		

		//fill squares from file
		for( int i = 0; i < numRows; ++i )
		{
			getline( inputFile, line );
			stringstream lineStream( line );

			for( int j = 0; j < numCols; ++j )
			{
				getline( lineStream, temp, ' ' );
				squares[i][j] = int(atof( temp.c_str() ));
			}
		}

		rowMax = new int[numRows];
		for( int i = 0; i < numRows; ++i ) rowMax[i] = 0; 
		colMax = new int[numCols];
		for( int i = 0; i < numCols; ++i ) colMax[i] = 0;

		rowMin = new int[numRows];
		for( int i = 0; i < numRows; ++i ) rowMin[i] = 101; 
		colMin = new int[numCols];
		for( int i = 0; i < numCols; ++i ) colMin[i] = 101;

		//traverse rows
		for( int row = 0; row < numRows; ++row )
		{
			for( int col = 0; col < numCols; ++col )
			{
				if( squares[row][col] > rowMax[row] ) rowMax[row] = squares[row][col];
				if( squares[row][col] < rowMin[row] ) rowMin[row] = squares[row][col];
			}
		}

		//traverse cols
		for( int col = 0; col < numCols; ++col )
		{
			for( int row = 0; row < numRows; ++row )
			{
				if( squares[row][col] > colMax[col] ) colMax[col] = squares[row][col];
				if( squares[row][col] < colMin[col] ) colMin[col] = squares[row][col];
			}
		}

		//now go through squares to check
		bool possible = true;

		for( int row = 0; row < numRows; ++row )
		{
			for( int col = 0; col < numCols; ++col )
			{
				if( squares[row][col] > rowMin[row] && squares[row][col] > colMin[col] )
				{
					//possible
				}
				else if( squares[row][col] == rowMin[row] && squares[row][col] == rowMax[row] )
				{
					//possible
				}else if( squares[row][col] == colMin[col] && squares[row][col] == colMax[col] )
				{
					//possible
				}else
				{
					//not possible
					possible = false;
				}

			}

		}

		//output
		if( possible )
		{
			outputFile << "Case #" << iCase << ": YES" << endl;
		}else
		{
			outputFile << "Case #" << iCase << ": NO" << endl;
		}

		delete [] rowMax;
		delete [] rowMin;
		delete [] colMax;
		delete [] colMin;

		for( int i = 0; i < numRows; ++i )
		{
			delete [] squares[i];
		}

		delete [] squares;

	}

}