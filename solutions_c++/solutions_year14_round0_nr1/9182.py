// Magic_Trick.cpp : Defines the entry point for the console application.
//
#pragma warning(disable : 4996)

#include "stdafx.h"
#include <fstream> // You should include this library
#include <iostream>

#define case1 "Case #1: "
#define case2 "Case #2: Bad magician!"
#define case3 "Case #3: Volunteer cheated!"

using namespace std;

int main()
{
	cout << "______________input file____________" << endl;

	int T, TestCaseCounter = 0, caseNumber = 0, cardNumber = 0;
	int rowNumber;
	int square_grid[4][4];
	int row1[4], row2[4];

	freopen("D:\\My works\\GoogleJam\\input.in","r",stdin); // For reading input

	cin >> T;
	if (T < 1 || T > 100)
		return 1;

	//cout << T << endl;
	T = T*2;

	int counter = 1;

	ofstream out("D:\\My works\\GoogleJam\\output.out");

	do
	{
		if (TestCaseCounter == 2)
			TestCaseCounter = 0;

		TestCaseCounter++;

		cin >> rowNumber;
		if (rowNumber < 1 || rowNumber > 16)
			return 1;

		//cout << rowNumber << endl;

		 for (int i = 0; i < 4; i++)
		 {
			 for (int j = 0; j < 4; j++)
			 {
				 cin >> square_grid[i][j];
				// cout << square_grid[i][j] << " ";
			 }
			//cout << endl;
		 }

		 if( TestCaseCounter == 1 )
		 {
			 for (int j = 0; j < 4; j++)
			 {
				 row1[j] = square_grid[rowNumber - 1][j];
			 }
		 }

		 else if( TestCaseCounter == 2 )
		 {
			 for (int j = 0; j < 4; j++)
			 {
				 row2[j] = square_grid[rowNumber - 1][j];
			 }

			 for (int i = 0; i < 4; i++)
			 {
				 for (int j = 0; j < 4; j++)
				 {
					 if(row1[i] == row2[j] && cardNumber == 0)
					 {
						 cardNumber = row1[i];
						 caseNumber = 1;
					 }
					 else if (row1[i] == row2[j] && cardNumber != 0)
						 caseNumber = 2;
				 }
			 }

			 if (caseNumber == 0)
				 caseNumber = 3;

			 if (caseNumber == 1)
			 {
				 cout << "Case #" << counter << ": " << cardNumber << endl;
				 out << "Case #" << counter << ": " << cardNumber << endl;
			 }
			 else if (caseNumber == 2)
			 {
				 cout << "Case #" << counter << ": Bad magician!" << endl;
				 out << "Case #" << counter << ": Bad magician!" << endl;
			 }
			 else if (caseNumber == 3)
			 {
				 cout << "Case #" << counter << ": Volunteer cheated!" << endl;
				 out << "Case #" << counter << ": Volunteer cheated!" << endl;

			 }

			 caseNumber = 0;
			 cardNumber = 0;
			 counter++;
		 }

		 T--;
	} while (T != 0);

	out.close();

	return 0;
}

