// Author: Bret Aston
// Project: Google Code Jam: Problem A
// -----------------------------------

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//The openFile function
//Purpose: To collect and open a valid source file via user input
//Parameters: A reference to the in-filestream to be used
//Returns: Nothing
void openFile(ifstream&);

int main()
{
	const int ROW_WIDTH = 4;
	const int SAMPLE_SIZE = 16;

	int cards[SAMPLE_SIZE];
	int chosenRow1[ROW_WIDTH], chosenRow2[ROW_WIDTH], matches[ROW_WIDTH];

	ofstream out;
	out.open("A-small.txt");
	ifstream in;
	openFile(in);
	cout << endl;

	int testCases;
	int answer1, answer2;
	int caseCount = 1;

	in >> testCases;
	while (in >> answer1)
	{
		for (int i = 0; i < SAMPLE_SIZE; ++i)
		{
			in >> cards[i];
			if (i >= answer1 * ROW_WIDTH - ROW_WIDTH && i < answer1 * ROW_WIDTH)
			{
				if (i == 0)
					chosenRow1[i] = cards[i];
				else
					chosenRow1[i % ROW_WIDTH] = cards[i];
			}
		}

		in >> answer2;
		for (int i = 0; i < SAMPLE_SIZE; ++i)
		{
			in >> cards[i];

			if (i >= answer2 * ROW_WIDTH - ROW_WIDTH && i < answer2 * ROW_WIDTH)
			{
				if (i == 0)
					chosenRow2[i] = cards[i];
				else
					chosenRow2[i % ROW_WIDTH] = cards[i];
			}
		}

		int matchCount = 0;
		for (int i = 0; i < ROW_WIDTH; ++i)
		{
			for (int j = 0; j < ROW_WIDTH; ++j)
			{
				if (chosenRow1[i] == chosenRow2[j])
				{
					matches[matchCount] = chosenRow1[i];
					++matchCount;
				}
			}
		}
		//
		cout << "Case #" << caseCount << ": ";
		if (matchCount == 1)
			cout << matches[0] << endl;
		else if (matchCount > 1)
			cout << "Bad magician!" << endl;
		else if (matchCount == 0)
			cout << "Volunteer cheated!" << endl;
		//
		out << "Case #" << caseCount++ << ": ";
		if (matchCount == 1)
			out << matches[0] << endl;
		else if (matchCount > 1)
			out << "Bad magician!" << endl;
		else if (matchCount == 0)
			out << "Volunteer cheated!" << endl;
	}
	cout << endl;

	system("PAUSE");
	return 0;
}

void openFile(ifstream& in)
{
	cout << "Enter the file name: ";
	string dataFile;
	getline(cin, dataFile);
	in.open(dataFile);

	while (!in)														//Repeats until user enters valid file name or quits
	{
		cout << "\nFile not found. Try again or 0 to quit: ";
		getline(cin, dataFile);

		if (dataFile == "0")										//Abort option if valid file name can't be provided
		{
			cout << "\nProgram ending. Good Bye!\n" << endl;
			system("PAUSE");
			exit(1);
		}
		in.open(dataFile);
	}
}