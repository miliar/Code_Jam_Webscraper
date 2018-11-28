#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
	ofstream outfile("results.out");
	ifstream infile("A-small-attempt0.in");    // infile is a name of our choosing
	if (!infile)		        // Did opening the file fail?
	{
		cerr << "Error: Cannot open input file!" << endl;
		return (1);
	}
	if (!outfile)		   // Did the creation fail?
	{
		cerr << "Error: Cannot create output file!" << endl;
		return (1);
	}

	int numCases;
	infile >> numCases;
	//infile.ignore(10000, '\n');

	for (int caseNum = 0; caseNum < numCases; caseNum++)
	{
		int rowAns;
		infile >> rowAns;

		int numberKey[4];

		int rowCount = 0;
		for (int r = 0; r < 4; r++)
		{
			for (int c = 0; c < 4; c++)
			{
				if (r + 1 == rowAns)
				{
					infile >> numberKey[c];
				}
				else
				{
					int temp;
					infile >> temp;
				}
			}
		}

		int secondRowAns;
		infile >> secondRowAns;

		int numberOfAnsFound = 0; //check bad magician
		int ans;
		for (int r = 0; r < 4; r++)
		{
			for (int c = 0; c < 4; c++)
			{
				if (r + 1 == secondRowAns)
				{
					int num;
					infile >> num;
					for (int k = 0; k < 4; k++)
					{
						if (num == numberKey[k])
						{
							numberOfAnsFound++;
							ans = num;
						}
					}
				}
				else
				{
					int temp;
					infile >> temp;
				}
			}
		}


		if (numberOfAnsFound == 0)
		{
			outfile << "Case #" << caseNum + 1 << ": " << "Volunteer cheated!" << endl;
		}
		else if (numberOfAnsFound == 1)
		{
			outfile << "Case #" << caseNum + 1 << ": " << ans << endl;
		}
		else if (numberOfAnsFound > 1)
		{
			outfile << "Case #" << caseNum + 1 << ": " << "Bad magician!" << endl;
		}


	}

	return 0;
}