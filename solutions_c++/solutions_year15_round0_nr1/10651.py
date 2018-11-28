

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <fstream>
#define toDigit(c) (c-'0')
using namespace std;



int main()
{

	int T = 0;
	
	// open a file in read mode.
	ifstream infile;
	infile.open("A-small-attempt2.in");

	cout << "Reading from the file" << endl;
	infile >> T;

	int SMax = 0;

	char S[1000000]; //char S[1000];

	std::vector<int> tempAnswer(T);

	ofstream myfile;
	myfile.open("output.txt");


	for (size_t i = 0; i < T; i++)
	{
		infile >> SMax;
		infile >> S;

		int Sint[1000] = { 0 };
		int Cummulative[1000] = { 0 };
		//int tempAnswer[T] = { 0 };
		int tempAnswerVal = 0;
		int cumValue = 0;

		for (int j = 0; j < SMax + 1; j++)
		{
			Sint[j] = (int)toDigit(S[j]); // (S[j] - '0');

			if (j == 0)
			{
				cumValue = Sint[j];
			}

			if ((cumValue < j) && (Sint[j] != 0)) //When handclapper is needed
			{
				tempAnswerVal = tempAnswerVal + (j - cumValue);
				cumValue = cumValue + (j - cumValue) + Sint[j];
			}
			else //When handclapper is NOT needed
			{
				if (j > 0)
				{
					cumValue = cumValue + Sint[j];
				}

			}

		}
		tempAnswer[i] = tempAnswerVal;
	}

	for (size_t i = 0; i < T; i++)
	{
		cout << "Case #" << (i + 1) << ": " << tempAnswer[i] << endl;
		myfile << "Case #" << (i + 1) << ": " << tempAnswer[i] << endl;

	}

	// close the opened file.
	myfile.close();
	infile.close();

	return 0;
}


