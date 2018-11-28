//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

void arrangeCards(int arr[][4])
{
	int temp = 0, x = 0, y = 0, iter = 0;

	iter = rand()%10+1;
	while(iter > 0)
	{
		x = rand()%3, y = rand()%3;
		temp = arr[x][y];
		if(x < 3 && y < 3)
		{
			arr[x][y] = arr[x+1][y+1];  
			arr[x+1][y+1] = arr[x][y]; 
		}
		else if(x > 0 && y > 0)
		{
			arr[x][y] = arr[x+1][y+1];  
			arr[x+1][y+1] = arr[x][y];
		}
		iter--;
	}
}

void printCards(int arr[][4])
{
	for(int x = 0; x <= 3; x++)
	{
		cout << endl;
		for(int y = 0; y <= 3; y++)
			cout << arr[x][y] << " ";
	}
}

void setDeck(int arr[][4])
{
	int val = 1;

	for(int x = 0; x <= 3; x++)
	{
		for(int y = 0; y <= 3; y++)
		{
			arr[x][y] = val;
			val++;
		}
	}
}

void getRow(int arr[][4], int rowArr[], int row)
{
	for(int x = 0; x <= 3; x++)
		rowArr[x] = arr[row][x];
}

int magic(int row1[], int row2[]) // -1; bad, -2; cheat
{
	int numMatches = 0, match = 0;
	for(int x = 0; x < 4; x++)
		for(int y = 0; y < 4; y++)
		{
			if(row1[x] == row2[y])
			{
				match = row1[x];
				if(numMatches == 0)
					numMatches++;
				else
					return -1; // more than 1 match, bad magician
			}
		}
	if(numMatches == 0)
       		return -2;	// No matches found; cheated	
	return match;
}

int main()
{
	int cardDeck[4][4], row1[4] = {0}, row2[4] = {0};
	int testCase = 1, numTest = 0, ans = 0;

	fstream fin("A-small-attempt0.in", fstream::in);
	fstream fout("output.txt", fstream::out | fstream::trunc);

	//cout << "Enter num test cases: ";
	cin >> numTest;
	while(numTest > 0)
	{
		cout << endl << "Test case: " << testCase;

		cout << endl << "Enter ans num1; ";
		cin >> ans;
		for(int x = 0; x < 4; x++)
		{
			//cout << endl << "Enter Row " << x+1 << ": ";
			for(int y = 0; y < 4; y++)
				cin >> cardDeck[x][y];
			// Ignores space, or return key, grabs 4
			//cin >> cardDeck[x][0] >> cardDeck[x][1] >> cardDeck[x][2] >> cardDeck[x][3];
		}
		//printCards(cardDeck);
		getRow(cardDeck, row1, ans-1);
		cout << endl << "Enter ans num2; ";
		cin >> ans;
		for(int x = 0; x < 4; x++)
		{
			//cout << endl << "Enter Row " << x+1 << ": ";
			for(int y = 0; y < 4; y++)
				cin >> cardDeck[x][y];
			// Ignores space, or return key, grabs 4
			//cin >> cardDeck[x][0] >> cardDeck[x][1] >> cardDeck[x][2] >> cardDeck[x][3];
		}
		getRow(cardDeck, row2, ans-1);
		
		ans = magic(row1, row2);
		cout << "Case #"<< testCase << ": ";
		fout << "Case #"<< testCase << ": ";
		if(ans == -1)
		{
			fout << "Bad magician!" << endl;
			cout << "Bad magician!" << endl;
		}
		else if(ans == -2)
		{
			fout << "Volunteer cheated!" << endl;
			cout << "Volunteer cheated!" << endl;
		}
		else
		{
			cout << ans << endl;
			fout << ans << endl;
		}
		/*
		cout << endl << "Enter row num1; ";
		cin >> ans;
		printCards(cardDeck);	
		getRow(cardDeck, row1, ans-1);	
		arrangeCards(cardDeck);
		cout << endl << "Enter row num2; ";
		cin >> ans;
		printCards(cardDeck);
		getRow(cardDeck, row2, ans-1);	


		cout << "Rows 1, 2" << endl;
		for(int x = 0; x < 4; x++)
			cout << row1[x] << " ";
		cout << endl;
		for(int x = 0; x < 4; x++)
			cout << row1[x] << " ";
*/
		numTest--;
		testCase++;
	}
	//Case #1: 7
//Case #2: Bad magician!
//Case #3: Volunteer cheated!
	fout.close();
	getchar();
	return 0;
}

/*	while(numTest > 0)
	{
		cout << endl << "Test case: " << numTest;
		setDeck(cardDeck);
		printCards(cardDeck);
		cout << endl << "Enter row num1; ";
		cin >> ans;
		printCards(cardDeck);
		getRow(cardDeck, row1, ans-1);
		arrangeCards(cardDeck);
		cout << endl << "Enter row num2; ";
		cin >> ans;
		printCards(cardDeck);
		getRow(cardDeck, row2, ans-1);


		cout << "Rows 1, 2" << endl;
		for(int x = 0; x < 4; x++)
			cout << row1[x] << " ";
		cout << endl;
		for(int x = 0; x < 4; x++)
			cout << row1[x] << " ";

		numTest--;
		fout << "Case #"<< numTest << ": ";
		fout << "Bad magician!" << endl;
		fout << "Volunteer cheated!" << endl;
	}
*/

