#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream inputFile("A-small-attempt0.in");
	ofstream outputFile("output.txt");
	int T, ans1, ans2;
	int Cards1[4][4], Cards2[4][4];
	int FirstCards[4], SecondCards[4];
	int nbCardFound = 0, cardFound;

	inputFile >> T;

	for(int i = 0; i < T; i++)
	{
		nbCardFound = 0;

		// Get info from input file
		inputFile >> ans1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				inputFile >> Cards1[i][j];
		inputFile >> ans2;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				inputFile >> Cards2[i][j];

		// Play with the info
		ans1--;
		ans2--;
		for(int i = 0; i < 4; i++)
		{
			FirstCards[i] = Cards1[ans1][i];
			SecondCards[i] = Cards2[ans2][i];
		}

		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
				if(FirstCards[i] == SecondCards[j])
				{
					nbCardFound++;
					cardFound = FirstCards[i];
				}
		}

		outputFile << "Case #" << i+1 << ": ";
		switch(nbCardFound)
		{
		case 1:
			outputFile << cardFound;
			break;
		case 0:
			outputFile << "Volunteer cheated!";
			break;
		default:
			outputFile << "Bad magician!";
		}
		outputFile << endl;
	}

}
