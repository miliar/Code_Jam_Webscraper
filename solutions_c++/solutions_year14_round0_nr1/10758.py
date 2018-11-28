#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>

using namespace std;

int main()
{
	string line;
	char input[20];
	int counter = 0;
	int rowCounter = 1;
	int rowNumber = 0;
	int caseNumber = 1;
	int numberCounter = 0;
	int cardCounter = 0;
	int card = 0;
	int number1[4];
	int number2[4];

	ifstream file;
	ofstream outputFile;
	file.open("A-small-attempt2.in");
	outputFile.open("OutputFile.txt");


	if (!file.is_open())
	{
		cout << "fucked" << endl;
	}
	
	else
	{
		getline(file, line);
		while (getline(file,line))
		{
			if (line.size() == 1)
			{
				if (counter == 2)
				{
					counter = 0;
					caseNumber++;
				}
				rowNumber = atoi(line.c_str());
				rowCounter = 1;
				counter++;
			}
				
			else if ((line.size() > 1)&&(counter == 1))
			{
				if (rowCounter == rowNumber)
				{
					stringstream s(line);
					s >> number1[0] >> number1[1] >> number1[2] >> number1[3];
					/*cout << "s1 = ";
					for (int i = 0; i < 4; i++)
					{
						cout << number1[i];
					}
					cout << endl;*/
				}
				rowCounter++;
			}

			else if ((line.size() > 1) && (counter == 2))
			{
				if (rowCounter == rowNumber)
				{
					stringstream s(line);
					s >> number2[0] >> number2[1] >> number2[2] >> number2[3];
					/*cout << "s2 = ";
					for (int i = 0; i < 4; i++)
					{
						cout << number2[i];
					}
					cout << endl;*/
				}
				rowCounter++;

				if (rowCounter == 5)
				{
					for (int i = 0; i < 4; i++)
					{
						for (int j = 0; j < 4; j++)
						{
							if (number1[i] == number2[j])
							{
								cardCounter++;
								card = number1[i];
							}
						}
					}
					if (cardCounter == 1)
					{
						cardCounter = 0;
						outputFile << "Case #" << caseNumber <<":  " << card << "\n";
					}
					else if (cardCounter > 1)
					{
						cardCounter = 0;
						outputFile << "Case #" << caseNumber << ":  Bad magician!" << "\n";
					}
					else if (cardCounter == 0)
					{
						cardCounter = 0;
						outputFile << "Case #" << caseNumber << ":  Volunteer cheated!" << "\n";
					}
					
				}
			}

			
		}
		outputFile.close();
		file.close();
	}
	system("pause");
	return 0;
}