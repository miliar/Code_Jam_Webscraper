#include <stdio.h>
#include <iostream>

using namespace std;
int determineMatch();

int match = 0;

int main()
{
	int numTests;
	int numMatches = 0;
	
	cin >> numTests;
	
	for(int i = 0; i < numTests; i++)
	{
		numMatches = determineMatch();
		if(i > 0)
		{
			cout << endl;
		}
		switch(numMatches)
		{
			case 0: cout << "Case #" << i+1 << ": Volunteer cheated!";
				break;
			case 1: cout << "Case #" << i+1 << ": " << match;
				break;
			default: cout << "Case #" << i+1 << ": Bad magician!";
		}
	}
	return 0;
}

int determineMatch()
{
	int numMatches = 0;
	int firstChosenRow = 0;
	int secondChosenRow = 0;
	int row1[4];
	int row2[4];
	int temp;
	int listOfMatches[4];
	
	cin >> firstChosenRow;
	for(int i = 0; i < ((firstChosenRow-1) * 4); i++) 
		cin >> temp;//skip unimportant ones
	for(int i = 3; i >= 0; i--)
		cin >> row1[i];//store first row
	for(int i = (firstChosenRow) * 4; i < 16; i++) 
		cin >> temp;//skip remaining unimportant ones
		
	cin >> secondChosenRow;	
	for(int i = 0; i < ((secondChosenRow-1) * 4); i++) 
		cin >> temp;//skip unimportant ones
	for(int i = 3; i >= 0; i--)
		cin >> row2[i];//store first row
	for(int i = (secondChosenRow) * 4; i < 16; i++) 
		cin >> temp;//skip remaining unimportant ones	
	
	
	for(int i = 3; i >= 0; i--)
		for(int j = 3; j >= 0; j--)
			if(row1[i] == row2[j])
			{
				numMatches++;
				match = row1[i];
			}
	
	return numMatches;
}