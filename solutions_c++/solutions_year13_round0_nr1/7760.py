#include <iostream>
#include <string>
#include <fstream>

using namespace std;

#define ROWS 4
#define COLS 4

int main()
{
	int T, flagDraw, seqLength;
	char input[ROWS][COLS], current;
	string output;
	ifstream inFile;
	ofstream oFile;
	inFile.open("input.txt");
	inFile >> T;
	
	for(int test=0; test<T; test++)
	{
		flagDraw = 0;

		for(int i=0; i<ROWS; i++)
		{
			for(int j=0; j<COLS; j++)
			{
				inFile >> input[i][j];
				if(input[i][j] == '.')	
					flagDraw = 1;
			}
		}

		//Check Diagonal 1
		if(input[0][0] == 'T')
			current = input[1][1];
		else
			current = input[0][0];

		seqLength = 0;
		for(int i=0; i<ROWS; i++)
		{
			if(input[i][i] == '.')
				break;
			else if(input[i][i] == current || input[i][i] == 'T')
				seqLength++;
			else
				break;
		}
		if(seqLength == 4)
		{
			if(current == 'X')
				output = "X won";
			else
				output = "O won";
			goto OUT;
		}

		//Check Diagonal 2
		if(input[0][COLS-1] == 'T')
			current = input[1][COLS-1];
		else
			current = input[0][COLS-1];

		seqLength = 0;
		for(int i=0; i<ROWS; i++)
		{
			if(input[i][COLS-1-i] == '.')
				break;
			else if(input[i][COLS-1-i] == current || input[i][COLS-1-i] == 'T')
				seqLength++;
			else
				break;
		}
		if(seqLength == 4)
		{
			if(current == 'X')
				output = "X won";
			else
				output = "O won";
			goto OUT;
		}

		//Check Rows
		for(int i=0; i<ROWS; i++)
		{
			if(input[i][0] == 'T')
				current = input[i][1];
			else
				current = input[i][0];

			seqLength = 0;
			for(int j=0; j<COLS; j++)
			{
				if(input[i][j] == '.')
					break;
				else if(input[i][j] == current || input[i][j] == 'T')
					seqLength++;
				else
					break;
			}
			if(seqLength == 4)
			{
				if(current == 'X')
				output = "X won";
			else
				output = "O won";
				goto OUT;
			}
		}

		//Check Columns
		for(int i=0; i<COLS; i++)
		{
			if(input[0][i] == 'T')
				current = input[1][i];
			else
				current = input[0][i];

			seqLength = 0;
			for(int j=0; j<ROWS; j++)
			{
				if(input[j][i] == '.')
					break;
				else if(input[j][i] == current || input[j][i] == 'T')
					seqLength++;
				else
					break;
			}
			if(seqLength == 4)
			{
				if(current == 'X')
				output = "X won";
			else
				output = "O won";
				goto OUT;
			}
		}

		if(flagDraw)
		{
			output = "Game has not completed";
			goto OUT;
		}
		else
		{
			output = "Draw";
			goto OUT;
		}
OUT:
		oFile.open ("output.txt", ios::out | ios::app);
		oFile<<"Case #"<<test+1<<": "<<output<<endl;
		oFile.close();
	}
		inFile.close();

		return 0;
}