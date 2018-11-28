#include <iostream>
#include <limits.h>
#include <string.h>
#include <queue>
#include <fstream>
#include <climits>
#include <vector>
#include <stdio.h>

using namespace std;


int main()
{
    int N;
    // Get Input
	cin >> N;

	vector<vector<int> > firstLook;
	vector<vector<int> > secondLook;
	int firstguess, secondguess;
	
	// Algorithm variables
	vector<int> firstGuessedRow;
	vector<int> secondGuessedRow;

	vector<int> answers;

	for(int i = 0; i < N; i++)
	{

		cin >> firstguess;
		firstguess -= 1;
		for(int j = 0; j < 4; j++)
		{
			vector<int> temp;
			for(int k = 0; k < 4; k++)
			{
				int x;
				cin >> x;
				temp.push_back(x);
			}
			firstLook.push_back(temp);
		}
		cin >> secondguess;
		secondguess -= 1;

		for(int j = 0; j < 4; j++)
		{
			vector<int> temp;
			for(int k = 0; k < 4; k++)
			{
				int x;
				cin >> x;
				temp.push_back(x);
			}
			secondLook.push_back(temp);
		}
		
		// Get First Guessed Row
		for(int j = 0; j < 4; j++)
		{
			firstGuessedRow.push_back(firstLook[firstguess][j]);
		}
		// Get Second Guessed Row
		for(int j = 0; j < 4; j++)
		{
			secondGuessedRow.push_back(secondLook[secondguess][j]);
		}
				
		bool volunteerCheated = false;
		bool valueFound = false;
		bool badMagician = false;
		int value;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				//cout << firstGuessedRow[j] << " == " << secondGuessedRow[k] << " " << !valueFound << endl;
				if(firstGuessedRow[j] == secondGuessedRow[k] && !valueFound)
				{
					valueFound = true;
					value = firstGuessedRow[j];
					//cout << "asdas " << value;
				}
			
				else if(firstGuessedRow[j] == secondGuessedRow[k] && valueFound)
				{
					badMagician = true;
				}
			}
		}
		
		
		
		if(badMagician) 	 { answers.push_back(-1); }
		else if(valueFound)  { answers.push_back(value); }
		else 				 { answers.push_back(-2); }
	
	
		firstLook.clear();
		secondLook.clear();
		firstGuessedRow.clear();
		secondGuessedRow.clear();
	}
	
	for(int i = 0; i < answers.size(); i++)
	{
		cout << "Case #" << i+1 << ": ";
		if(answers[i] == -1) cout << "Bad magician!"	<< endl;
		if(answers[i] >  0 ) cout << answers[i]			<< endl;
		if(answers[i] == -2) cout << "Volunteer cheated!"<< endl;
		
		
	}
	
	/*
	cout << "First Matrix: Guess " <<  secondguess << endl;
	for(int i = 0; i < firstLook.size(); i++)
	{
		for(int j = 0; j < firstLook[i].size(); j++)
		{
				cout << firstLook[i][j] << " ";
		}
		cout << endl;
	}

	cout << "Second Matrix: Guess " <<  firstguess << endl;
	for(int i = 0; i < secondLook.size(); i++)
	{
		for(int j = 0; j < secondLook[i].size(); j++)
		{
				cout << secondLook[i][j] << " ";
		}
		cout << endl;
	}	
	*/
	
}

