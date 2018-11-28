
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream reader; reader.open("A-small.in");
	ofstream writer; writer.open("result.out");

	char inputValues[20]={'\0'};
	int numOfTestCases = 0, MAX_INPUT_SIZE = 20;
	reader.getline(inputValues, MAX_INPUT_SIZE, '\n');
	numOfTestCases = atoi(inputValues);


	string badRun = "Bad magician!", cheated = "Volunteer cheated!";
	for(int testNo = 1; testNo <= numOfTestCases; testNo++)
	{
		int first = 0, second = 0, actualCard = 0;
		int grid[4][4] = {0}, tempValues[4] = {0};
		memset(inputValues, '\0', MAX_INPUT_SIZE);
		reader.getline(inputValues, MAX_INPUT_SIZE, '\n');
		first = atoi(inputValues)-1;

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<3;j++)
			{
				memset(inputValues, '\0', MAX_INPUT_SIZE);
				reader.getline(inputValues, MAX_INPUT_SIZE, ' ');
				grid[i][j]=atoi(inputValues);
			}
			memset(inputValues, '\0', MAX_INPUT_SIZE);
			reader.getline(inputValues, MAX_INPUT_SIZE, '\n');
			grid[i][3]=atoi(inputValues);
		}
		for(int i=0;i<4;i++)
			tempValues[i] = 0;
		for(int j=0;j<4;j++)
			tempValues[j] = grid[first][j];

		memset(inputValues, '\0', MAX_INPUT_SIZE);
		reader.getline(inputValues, MAX_INPUT_SIZE, '\n');
		second = atoi(inputValues)-1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<3;j++)
			{
				memset(inputValues, '\0', MAX_INPUT_SIZE);
				reader.getline(inputValues, MAX_INPUT_SIZE, ' ');
				grid[i][j]=atoi(inputValues);
			}
			memset(inputValues, '\0', MAX_INPUT_SIZE);
			reader.getline(inputValues, MAX_INPUT_SIZE, '\n');
			grid[i][3]=atoi(inputValues);
		}
		
		int guessValue[4] ={0}, count = 0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(grid[second][j] == tempValues[i])
					if(count < 4)
						guessValue[count++] = tempValues[i];

		string outString = "Case #";
		memset(inputValues, '\0', MAX_INPUT_SIZE);
		itoa(testNo, inputValues, 10);
		outString.append(inputValues);
		outString.append(": ");
		
		if(count == 0)
			outString.append(cheated);
		else if(count > 1)
			outString.append(badRun);
		else	
		{
			memset(inputValues, '\0', MAX_INPUT_SIZE);
			itoa(guessValue[0], inputValues, 10);
			outString.append(inputValues);
		}

		outString.append("\n");
		writer.write(outString.c_str(), outString.length());
	}

	writer.close();
	reader.close();
	return 1;
}