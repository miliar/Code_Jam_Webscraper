#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream inputfile;
	ofstream outputfile;
	int T, rownumber, temp, row1[4], row2[4];

	//Open input and output file
	inputfile.open("input.in");
	outputfile.open("output.out");
	
	//Read number of tests
	inputfile >> T;

	//Read all tests and perform check
	for (int i = 0; i < T; i++)
	{
		//Read question 1
		inputfile >> rownumber;
		rownumber--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				inputfile >> temp;
				if (j == rownumber)
				{
					row1[k] = temp;
				}
			}
		}
		
		//Read question 2
		inputfile >> rownumber;
		rownumber--;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				inputfile >> temp;
				if (j == rownumber)
				{
					row2[k] = temp;
				}
			}
		}

		//Find matching element if any
		int result = -1;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (row1[j] == row2[k])
				{
					if (result == -1)
					{
						result = row1[j];
					}
					else
					{
						result = -2;
					}
				}

			}
		}

		//Print result
		if (result > -1)
		{
			outputfile << "Case #" << i +1<< ": " << result<<'\n';
		}
		else
		{
			if (result == -1)
			{
				outputfile << "Case #" << i + 1 << ": Volunteer cheated!" << '\n';
			}
			else
			{
				if (result == -2)
				{
					outputfile << "Case #" << i + 1 << ": Bad magician!" << '\n';
				}
			}
		}
	}
	inputfile.close();
	outputfile.close();
	
	return 0;
}