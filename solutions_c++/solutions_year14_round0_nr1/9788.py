#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdio.h>
#include <string.h>
using namespace std;
typedef int InputArray[4][4];
typedef int PossibleAnswer[4];

int main(const int argc, const char* argv[]) {

  int testCases = 0, answerLineOne = 0, answerLineTwo = 0,goodCardCount = 0, card = 0;
  InputArray inputArray;
  PossibleAnswer possibleAnswers, possibleAnswersTwo,goodCards;
  
  cin >> testCases;
  for(int i = 0; i < testCases; i++)
  {
	goodCardCount = 0;
	cin >> answerLineOne;
	for(int x = 0; x < 4; x++)
	{
		for(int y = 0; y < 4; y++)
		{			
			cin>>inputArray[x][y];
		}
	}
	possibleAnswers[0] = inputArray[answerLineOne-1][0];
	possibleAnswers[1] = inputArray[answerLineOne-1][1];
	possibleAnswers[2] = inputArray[answerLineOne-1][2];
	possibleAnswers[3] = inputArray[answerLineOne-1][3];
	cin >> answerLineTwo;
	for(int x = 0; x < 4; x++)
	{
		for(int y = 0; y < 4; y++)
		{
			cin>>inputArray[x][y];
		}
	}
	possibleAnswersTwo[0] = inputArray[answerLineTwo-1][0];
	possibleAnswersTwo[1] = inputArray[answerLineTwo-1][1];
	possibleAnswersTwo[2] = inputArray[answerLineTwo-1][2];
	possibleAnswersTwo[3] = inputArray[answerLineTwo-1][3];
	for(int v = 0; v < 4; v++)
	{
		for(int p = 0; p < 4; p++)
		{
			if(possibleAnswers[v] == possibleAnswersTwo[p])
			{
				goodCards[v] = 1;
				goodCardCount++;
				if(goodCardCount == 1)
				{
					card = possibleAnswers[v];
				}
			}
			else
			{
				goodCards[v] = 0;
			}
			
		}
	}
	
	if(goodCardCount == 1)
	{
		cout<<"Case #"<< (i+1)<<": "<<card<<endl;
	}
	else if(goodCardCount > 1)
	{
		cout<<"Case #"<< (i+1)<<": Bad magician!"<<endl;
	}
	else
	{
		cout<<"Case #"<< (i+1)<<": Volunteer cheated!"<<endl;
	}
  }

  return 0;
}

