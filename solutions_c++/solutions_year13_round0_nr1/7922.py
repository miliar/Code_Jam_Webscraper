#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main( int argc, char** argv )
{
	unsigned int numCases(0), iCase(0);
	bool xwon, ywon, notfinished;
	char squares[4][4];

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
		xwon = ywon = notfinished = false;

		//discard emtpy line if needed
		if( iCase > 1 )
		{
			getline( inputFile, line );
			outputFile << endl;
		}

		//fill squares from file
		for( int i = 0; i < 4; ++i )
		{
			getline( inputFile, line );

			for( int j = 0; j < 4; ++j )
			{
				squares[i][j] = line[j];
			}
		}

		//check rows
		for( int row = 0; row < 4; ++row )
		{
			//check Xs
			if( (squares[row][0] == 'X' || squares[row][0] == 'T') &&
				(squares[row][1] == 'X' || squares[row][1] == 'T') &&
				(squares[row][2] == 'X' || squares[row][2] == 'T') &&
				(squares[row][3] == 'X' || squares[row][3] == 'T') )
			{
				//XWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
				outputFile << "Case #" << iCase << ": X won";
				xwon = true;
			}

			//check Ys
			if( (squares[row][0] == 'O' || squares[row][0] == 'T') &&
				(squares[row][1] == 'O' || squares[row][1] == 'T') &&
				(squares[row][2] == 'O' || squares[row][2] == 'T') &&
				(squares[row][3] == 'O' || squares[row][3] == 'T') )
			{
				//YWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
				outputFile << "Case #" << iCase << ": O won";
				ywon = true;
			}

		}

		//check columns
		if( !xwon && !ywon ){
		for( int col = 0; col < 4; ++col )
		{
			//check Xs
			if( (squares[0][col] == 'X' || squares[0][col] == 'T') &&
				(squares[1][col] == 'X' || squares[1][col] == 'T') &&
				(squares[2][col] == 'X' || squares[2][col] == 'T') &&
				(squares[3][col] == 'X' || squares[3][col] == 'T') )
			{
				//XWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
				outputFile << "Case #" << iCase << ": X won";
				xwon = true;
			}

			//check Ys
			if( (squares[0][col] == 'O' || squares[0][col] == 'T') &&
				(squares[1][col] == 'O' || squares[1][col] == 'T') &&
				(squares[2][col] == 'O' || squares[2][col] == 'T') &&
				(squares[3][col] == 'O' || squares[3][col] == 'T') )
			{
				//YWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
				outputFile << "Case #" << iCase << ": O won";
				ywon = true;
			}

		}}

		//check diagonals

		//check Xs
		if( !xwon && !ywon ){
		if( (squares[0][0] == 'X' || squares[0][0] == 'T') &&
			(squares[1][1] == 'X' || squares[1][1] == 'T') &&
			(squares[2][2] == 'X' || squares[2][2] == 'T') &&
			(squares[3][3] == 'X' || squares[3][3] == 'T') )
		{
			//XWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
			outputFile << "Case #" << iCase << ": X won";
			xwon = true;
		}}

		if( !xwon && !ywon ){
		if( (squares[0][3] == 'X' || squares[0][3] == 'T') &&
			(squares[1][2] == 'X' || squares[1][2] == 'T') &&
			(squares[2][1] == 'X' || squares[2][1] == 'T') &&
			(squares[3][0] == 'X' || squares[3][0] == 'T') )
		{
			//XWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
			outputFile << "Case #" << iCase << ": X won";
			xwon = true;
		}}

		//check Ys
		if( !xwon && !ywon ){
		if( (squares[0][0] == 'O' || squares[0][0] == 'T') &&
			(squares[1][1] == 'O' || squares[1][1] == 'T') &&
			(squares[2][2] == 'O' || squares[2][2] == 'T') &&
			(squares[3][3] == 'O' || squares[3][3] == 'T') )
		{
			//YWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
			outputFile << "Case #" << iCase << ": O won";
			ywon = true;
		}}

		if( !xwon && !ywon ){
		if( (squares[0][3] == 'O' || squares[0][3] == 'T') &&
			(squares[1][2] == 'O' || squares[1][2] == 'T') &&
			(squares[2][1] == 'O' || squares[2][1] == 'T') &&
			(squares[3][0] == 'O' || squares[3][0] == 'T') )
		{
			//YWON!!!!!!!!!!!!!!!!!!!!!!!!!!!11
			outputFile << "Case #" << iCase << ": O won";
			ywon = true;
		}}

		if( !ywon && !xwon )
		{
			for( int i = 0; i < 3; ++i )
			{
				for( int j = 0; j < 3; ++j )
				{
					if( squares[i][j] == '.' )
					{
						notfinished = true;
					}
				}
			}

			if( !notfinished )
			{
				outputFile << "Case #" << iCase << ": Draw";
			}else
			{
				outputFile << "Case #" << iCase << ": Game has not completed";
			}

		}

	}

}