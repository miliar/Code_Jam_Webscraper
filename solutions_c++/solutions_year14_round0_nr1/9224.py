#include <iostream>
#include <fstream>
#include <stdlib.h>

#define HEIGHT 4
#define WIDTH 4
#define SETSIZE 16
#define NROWS 2

using namespace std;

ifstream input;

void inline readCards(int cardSet[SETSIZE])
{
	for (int i = 0; i < HEIGHT; ++i)
	{
		for (int j = 0; j < WIDTH; ++j)
		{
			input >> cardSet[i * WIDTH + j];
		}
	}
}

void inline setPickedRow(const int cardSet[SETSIZE], int pickedRow[WIDTH], const int row)
{
	for (int i = 0; i < WIDTH; ++i)
	{
		pickedRow[i] = cardSet[(row - 1) * WIDTH + i];
	}
}

void setRows(int cardSet[SETSIZE], int rows[NROWS][WIDTH])
{	
	int nRowPickedByVolunteer;

	for (int i = 0; i < NROWS; ++i) // number of rows == number of questions
	{
		input >> nRowPickedByVolunteer;
		readCards(cardSet);
		setPickedRow(cardSet, rows[i], nRowPickedByVolunteer);
	}
}

int evaluatePicks(const int firstRow[WIDTH], const int secondRow[WIDTH], int* answer)
{
	int answerCase = 0;
	*answer = -1;

	for (int i = 0; i < HEIGHT; ++i)
	{
		for (int j = 0; j < WIDTH; ++j)
		{
			if (firstRow[i] == secondRow[j])
			{
				answerCase += 1;
				if (*answer == -1)
				{
					*answer = firstRow[i];
				}
			}
		}
	}

	return answerCase;
}

int trick(const char* filename)
{
	input.open(filename);

	if (!input.is_open())
	{
		cout << "Something went very bad when reading the file :(" << endl;
		exit(EXIT_FAILURE);
	}


	int nNumberOfTests;
	int nCardSet[SETSIZE];	
	int nRows[NROWS][WIDTH];
	int nAnswerCase;
	int answer;
	ofstream output;
	output.open("output");
	input >> nNumberOfTests;

	for (int i = 1; i <= nNumberOfTests; ++i)
	{
		setRows(nCardSet, nRows);
		nAnswerCase = evaluatePicks(nRows[0], nRows[1], &answer);
		
		switch(nAnswerCase)
		{
			case 0:
				output << "Case #" << i << ": Volunteer cheated!";
				break;
			case 1:
				output << "Case #" << i << ": " << answer;
				break;
			default:
				output << "Case #" << i << ": Bad magician!";
				break;
		}
		output << endl;
	}

	// finally
	input.close();

	return 0;
}

int main(int argc, char const *argv[])
{
	
	if( argc != 2)   
  { 
   cout <<" Usage: magician <<input>>" << endl;
   exit(EXIT_FAILURE);
  }

  trick(argv[1]);

	return 0;
}