#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
	int numOfTrials = 0;

	int firstSet[4][4];
	int secondSet[4][4];

	int possibleAnswers[4];

	int firstRow = 0;
	int secondRow = 0;

	int answer = 0;

	int answerTotal = 0;

	fstream testCase;
	testCase.open("test.in", ios_base::in);

	if(testCase.is_open())
	{
		testCase >> numOfTrials;
		for (int trials = 0; trials< numOfTrials; trials++)
		{
			//Gets the row of the person's card in the first set.
			testCase >> firstRow;
			firstRow--;
			//Store first arrangement.
			for(int x = 0; x < 4; x++)
			{
				for(int y = 0; y < 4; y++)
				{
					testCase >> firstSet[x][y];
				}
			}
			//Gets the row of the person's card in the second set.
			testCase >> secondRow;
			secondRow--;
			//Store second arrangement.
			for(int x = 0; x < 4; x++)
			{
				for(int y = 0; y < 4; y++)
				{
					testCase >> secondSet[x][y];
				}
			}
			//Gets the answers in the first set.
			for(int i = 0; i < 4; i++)
			{
				possibleAnswers[i] = firstSet[firstRow][i];
			}
			//Gets the answers that match in the second set.
			for(int i = 0; i < 4; i++)
			{
				for(int j = 0; j < 4; j++)
				{
					if(possibleAnswers[j] == secondSet[secondRow][i])
					{
						answer = secondSet[secondRow][i];
						answerTotal++;
					}
					
				}
			}
			if(answerTotal > 1)
			{
				cout << "Case #" << trials + 1 << ": " <<"Bad magician!" << endl;
			}
			else if(answerTotal == 0)
			{
				cout << "Case #" << trials + 1 << ": " <<"Volunteer cheated!" << endl;
			}
			else if(answerTotal == 1)
			{
				cout << "Case #" << trials + 1 << ": " << answer << endl;
			}
			answerTotal = 0;
		}
	}
	system("pause");
	return 0;
}