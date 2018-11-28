#include <iostream>
#include <fstream>

using namespace std;

int grid[4][4];
int rows[2][4];

int main()
{
	int number_of_test;
	int answer[2];
	int j, k;
	int count=0, result=0;
	ifstream input;
	ofstream output;

	input.open("A-small-attempt1.in");
	output.open("output");

	input>>number_of_test;

	for (int i=0; i<number_of_test; i++)
	{
		for (j=0; j<2; j++)
		{
			input>>answer[j];

			for (k=0; k<4; k++)
			{
				input>>grid[k][0];
				input>>grid[k][1];
				input>>grid[k][2];
				input>>grid[k][3];
			}

			for (k=0; k<4; k++)
				rows[j][k]=grid[answer[j]-1][k];
		}

		for (j=0; j<4; j++)
			for (k=0; k<4; k++)
				if (rows[0][j]==rows[1][k])
				{
					result=rows[0][j];
					count++;
				}

		switch (count)
		{
		case 0:
			output<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
			break;
		case 1:
			output<<"Case #"<<i+1<<": "<<result<<endl;
			break;
		default:
			output<<"Case #"<<i+1<<": Bad magician!"<<endl;
			break;
		}

		count=0;
	}

	input.close();
	output.close();

	system("PAUSE");
	return 0;
}