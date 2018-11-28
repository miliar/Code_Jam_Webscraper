#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

const char inputFile[] = "A-small-attempt0.in";
//const char inputFile[] = "A-big.in";
const char outputFile[] = "results.out";

int main()
{
	ifstream input;
	input.open(inputFile);
	
	ofstream output;
	output.open(outputFile);
	
	int N = 0;
	input >> N;
	int data1[4][4];
	int data2[4][4];
	
	for (int i = 0; i < N; i++)
	{
		int row1 = 0;
		input >> row1;
		row1--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				input >> data1[j][k];
			}
		}
		int row2 = 0;
		input >> row2;
		row2--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				input >> data2[j][k];
			}
		}
		int result = 0;
		int number = -1;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (data1[row1][k] == data2[row2][j])
				{
					if (number == -1)
					{
						number = data1[row1][k];
						result = 1; 
					}
					else
						result = 2;
				}
			}
		}

		output << "Case #" << i + 1 << ": ";
		if (result == 0)
			output << "Volunteer cheated!\n";
		else if (result == 1)
			output << number << endl;
		else
			output << "Bad magician!\n";
		
	}


	return 0;
}












