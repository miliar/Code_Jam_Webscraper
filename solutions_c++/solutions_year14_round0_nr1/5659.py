#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <typeinfo>

using namespace std;

/*void main()
{
	fstream dataExtractor;
	string currentLine;
	int lineCounter = -1;
	int numberOfCases;

	int finalLayoutColumnPlaceThingy;

	//int badMagician;
	//int	badVolunteer;

	int Answers = 0;
	int initialLayout[3][3];
	int initialRow;
	int finalLayout[3][3];
	int finalRow;

	int rowpos = 0;

	dataExtractor.open("read.txt");
	while (getline(dataExtractor, currentLine))
	{
		if (lineCounter == -1)
		{
			lineCounter = 0;
			continue;
		}

		if (lineCounter == 0)
		{
			istringstream(currentLine) >> initialRow;
			cout << "in row: " << initialRow;
			lineCounter += 1;
		}

		if ((lineCounter >= 1) && (lineCounter <= 4))
		{
			for (int i = 0; i < 4; i++)
			{
				dataExtractor >> initialLayout[rowpos][i];
				istringstream(initialLayout[rowpos][i]) >> initialLayout[rowpos][i];
				cout << initialLayout[rowpos][i];
			}
			rowpos += 1;
			lineCounter += 1;
			cout << "\n";
			//cout << "lncn: " << lineCounter << endl;
			continue;

		}

		if (lineCounter == 5)
		{
			rowpos = 0;
			dataExtractor >> finalRow;
			istringstream(finalRow) >> finalRow;
			cout << "final type " << finalRow << endl;
			lineCounter += 1;
		}

		if ((lineCounter >= 6) && (lineCounter < 10))
		{
			for (int i = 0; i < 4; i++)
			{
				dataExtractor >> finalLayout[rowpos][i];
				istringstream(initialLayout[rowpos][i]) >> initialLayout[rowpos][i];
				//cout << finalLayout[rowpos][i];
			}
			rowpos += 1;
			lineCounter += 1;
			//cout << "\n";
			//cout << "lncn: " << lineCounter << endl;
			continue;

		}

		if (lineCounter == 10)
		{
			cout << "INITITITITIIT" << initialRow;
			for (int initialRowValue = 0; initialRowValue < 4; initialRowValue++)
			{
				for (int finalRowValue = 0; finalRowValue < 4; finalRowValue++)
				{
					cout << "initial Row Value    " << initialRowValue << endl;
					cout << "initial Row    " << initialRow << endl;
					cout << initialLayout[initialRow][initialRowValue];
					/*if (initialLayout[initialRow][initialRowValue] == finalLayout[finalRow][finalRowValue])
					{
						cout << "match fond at : " << finalLayout[finalRow][finalRowValue];
						Answers = -1;
						cout << "no.of answeres:" << Answers;
					}
				}

			}

			if (Answers == -1)
			{
				cout << "bad volunteer";
			}
			if (Answers == 0)
			{
				cout << "answer";
			}
			if (Answers > 1)
			{
				cout << "\n" << Answers << endl;
				cout << "Bad mufic";
			}

			lineCounter = 0;
			cout << "\n";
			continue;

			/*if (lineCounter == -1)
			{
			istringstream(currentLine) >> numberOfCases;
			lineCounter = 1;
			continue;
			}

			else
			{
			if (lineCounter == 1)
			{
			istringstream(currentLine) >> initialRow;
			cout << "initial ans: " << initialRow << endl;
			lineCounter = 2;
			continue;
			}

			if ((lineCounter > 1) && (lineCounter <= 5))
			{
			for (int i = 0; i < 4; i++)
			{
			dataExtractor >> initialLayout[rowpos][i];
			cout << initialLayout[rowpos][i];
			}
			cout << "\n";
			lineCounter = lineCounter + 1;
			rowpos += 1;
			continue;
			}

			if (lineCounter == 6)
			{
			rowpos = 0;
			istringstream(currentLine) >> finalRow;
			cout << "final ans: " << finalRow << endl;
			cout << "\n";
			lineCounter = 7;
			continue;
			}

			if ((lineCounter >= 7) && (lineCounter <= 10))
			{
			for (int i = 0; i < 4; i++)
			{
			dataExtractor >> finalLayout[rowpos][i];
			cout << initialLayout[rowpos][i];
			}
			cout << "\n"
			lineCounter = lineCounter + 1;
			continue;
			}
			if (lineCounter == 10)
			{
			for (int initialRowValue = 0; initialRowValue < 4; initialRowValue++)
			{
			for (int finalRowValue = 0; finalRowValue < 4; finalRowValue++)
			{
			if (initialLayout[initialRow][initialRowValue] == finalLayout[finalRow][finalRowValue])
			{
			finalLayoutColumnPlaceThingy = finalRowValue;
			numberOfAnswers += 1;
			}
			}

			}

			if (numberOfAnswers == -1)
			{
			cout << "bad volunteer";
			}
			if (numberOfAnswers == 0)
			{
			cout << "answer is: " << finalLayout[finalRow][finalLayoutColumnPlaceThingy];
			}
			if (numberOfAnswers > 1)
			{
			cout << "Bad mufic";
			}

			lineCounter = 1;
			continue;
			}

			}
		}
	}
	dataExtractor.close();


	cin.get();
	
}*/



void main()
{
	fstream data;
	fstream write;
	int lineNo = -1;

	int firstDecision;
	int lastDecision;
	int caseNumber = 1;

	string currentLine;

	int initialLayout[4][4];
	int finalLayout[4][4];



	data.open("read.txt");
	write.open("output.txt");
	while (getline(data, currentLine))
	{
		switch (lineNo)
		{

		case -1:
			lineNo = 0;
			continue;


		case(0) :
			istringstream(currentLine) >> firstDecision;
			lineNo += 1;
			for (int i = 0; i < 4; ++i)
			{
				data >> initialLayout[0][i];
			}
			continue;

		case(1) :
			for (int i = 0; i < 4; ++i)
			{
				data >> initialLayout[1][i];
			}
			lineNo += 1;
			continue;

		case(2) :
			for (int i = 0; i < 4; i++)
			{
				data >> initialLayout[2][i];
			}
			lineNo += 1;
			continue;

		case(3) :
			for (int i = 0; i < 4; i++)
			{
				data >> initialLayout[3][i];
			}
			lineNo += 1;
			continue;

		case(4) :
			data >> lastDecision;
			lineNo += 1;
			cout << "\n";
			continue;

		case(5) :
			for (int i = 0; i < 4; i++)
			{
				data >> finalLayout[0][i];
			}
			lineNo += 1;
			continue;


		case(6) :
			for (int i = 0; i < 4; i++)
			{
				data >> finalLayout[1][i];
			}
			lineNo += 1;
			continue;

		case(7) :
			for (int i = 0; i < 4; i++)
			{
				data >> finalLayout[2][i];
			}
			lineNo += 1;
			continue;

		case(8) :
			for (int i = 0; i < 4; i++)
			{
				data >> finalLayout[3][i];
			}
			lineNo += 1;
			continue;

		case(9) :

			int answers = -1;
			int answerPos;

			for (int m = 0; m < 4; m++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (initialLayout[firstDecision-1][m] == finalLayout[lastDecision-1][j])
					{
						answerPos = j;
						answers += 1;
					}
				}
			}

			if (answers == 0)
			{
				write << "Case #" << caseNumber << ": " << finalLayout[lastDecision - 1][answerPos] <<"\n";
				caseNumber += 1;
			}

			if (answers > 0)
			{
				write << "Case #" << caseNumber << ": " << "Bad magician!" << "\n";
				caseNumber += 1;
			}

			if (answers < 0)
			{
				write << "Case #" << caseNumber << ": " << "Volunteer cheated!" << "\n";
				caseNumber += 1;
			}
			
			lineNo = 0;
			cout << "\n";
			continue;
		}
	}
	data.close();

	cin.get();
}